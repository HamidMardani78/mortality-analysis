"""Streamlit dashboard for the in-hospital mortality analysis."""

import matplotlib.pyplot as plt
import streamlit as st

from src.data_loader import load_data
from src.cleaning import clean_data
from src.analysis import add_age_group, mortality_by_group, chi_square_test, compare_survived_died
from src.plots import plot_mortality_by_group, plot_survived_vs_died

st.set_page_config(page_title="In-Hospital Mortality", layout="wide")


@st.cache_data
def get_data():
    """Load, clean and prepare the SUPPORT2 dataset.

    Returns:
        pandas.DataFrame: the cleaned dataset with the age groups.
    """
    df = load_data()
    df = clean_data(df)
    df = add_age_group(df)
    return df


st.title("In-Hospital Mortality Analysis")
st.markdown(
    "Which factors are associated with dying in hospital? "
    "SUPPORT2 dataset: 9,105 seriously ill adults hospitalized "
    "in 5 US hospitals (1989-1994)."
)

df = get_data()

col1, col2, col3 = st.columns(3)
col1.metric("Patients", len(df))
col2.metric("Died in hospital", int(df["hospdead"].sum()))
col3.metric("In-hospital mortality", f"{df['hospdead'].mean() * 100:.1f}%")

tab1, tab2, tab3 = st.tabs(["Mortality by group", "Survived vs died", "Data"])

with tab1:
    group_options = {
        "Disease group": "dzgroup",
        "Disease class": "dzclass",
        "Age group": "age_group",
        "Cancer status": "ca",
        "Sex": "sex",
        "Income": "income",
    }
    choice = st.selectbox("Group patients by", list(group_options.keys()))
    column = group_options[choice]

    table = mortality_by_group(df, column)
    if column == "age_group":
        table = table.sort_index()

    left, right = st.columns([3, 2])

    with left:
        fig = plot_mortality_by_group(table, f"In-hospital mortality by {choice.lower()}")
        st.pyplot(fig)
        plt.close(fig)

    with right:
        st.dataframe(table)
        p = chi_square_test(df, column)
        if p < 0.001:
            st.write("Chi-square test: p-value < 0.001 (significant)")
        elif p < 0.05:
            st.write(f"Chi-square test: p-value = {p:.4f} (significant)")
        else:
            st.write(f"Chi-square test: p-value = {p:.4f} (not significant)")

with tab2:
    numeric_options = {
        "Severity score (APS)": "aps",
        "Coma score": "scoma",
        "Heart rate (beats/min)": "hrt",
        "Mean blood pressure (mmHg)": "meanbp",
        "Respiratory rate (breaths/min)": "resp",
        "Age (years)": "age",
    }
    label = st.selectbox("Variable", list(numeric_options.keys()))
    column = numeric_options[label]

    left, right = st.columns([2, 3])

    with left:
        fig = plot_survived_vs_died(df, column, label)
        st.pyplot(fig)
        plt.close(fig)

    with right:
        st.write("Mean, median and standard deviation for all variables:")
        st.dataframe(compare_survived_died(df, list(numeric_options.values())))

with tab3:
    diseases = st.multiselect(
        "Filter by disease group",
        sorted(df["dzgroup"].unique()),
    )
    if diseases:
        shown = df[df["dzgroup"].isin(diseases)]
    else:
        shown = df

    st.write(f"{len(shown)} patients")
    st.dataframe(shown)

    st.download_button(
        "Download the cleaned data (CSV)",
        shown.to_csv().encode("utf-8"),
        "support2_clean.csv",
        "text/csv",
    )