"""Functions to compute statistics on the SUPPORT2 dataset."""


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