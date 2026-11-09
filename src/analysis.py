"""Functions to compute statistics on the SUPPORT2 dataset."""

import pandas as pd
from scipy import stats

def mortality_by_group(df, group_col):
    """Compute the in-hospital mortality rate for each group of patients.

    Args:
        df (pandas.DataFrame): the cleaned dataset.
        group_col (str): name of the column used to make the groups.

    Returns:
        pandas.DataFrame: number of patients, number of deaths and
            mortality rate (%) for each group, sorted by mortality rate.
    """
    result = df.groupby(group_col)["hospdead"].agg(["count", "sum", "mean"])
    result.columns = ["patients", "deaths", "mortality_rate"]
    result["mortality_rate"] = (result["mortality_rate"] * 100).round(1)
    return result.sort_values("mortality_rate", ascending=False)


def add_age_group(df):
    """Add a column with the age group of each patient.

    Args:
        df (pandas.DataFrame): the cleaned dataset.

    Returns:
        pandas.DataFrame: the dataset with the new column 'age_group'.
    """
    df = df.copy()
    bins = [0, 50, 60, 70, 80, 120]
    labels = ["<50", "50-59", "60-69", "70-79", "80+"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)
    return df


def chi_square_test(df, group_col):
    """Test if mortality depends on the groups of a categorical column.

    Args:
        df (pandas.DataFrame): the cleaned dataset.
        group_col (str): name of the categorical column.

    Returns:
        float: the p-value of the chi-square test.
    """
    table = pd.crosstab(df[group_col], df["hospdead"])
    chi2, p_value, dof, expected = stats.chi2_contingency(table)
    return p_value