"""Streamlit dashboard for the in-hospital mortality analysis."""

import streamlit as st

from src.data_loader import load_data
from src.cleaning import clean_data
from src.analysis import add_age_group

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