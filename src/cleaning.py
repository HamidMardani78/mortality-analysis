"""Functions to clean the SUPPORT2 dataset."""

import numpy as np


def drop_mostly_missing(df, threshold=0.5):
    """Drop the columns that have too many missing values.

    Args:
        df (pandas.DataFrame): the dataset.
        threshold (float): maximum fraction of missing values allowed.

    Returns:
        pandas.DataFrame: the dataset without those columns.
    """
    missing_fraction = df.isna().mean()
    to_drop = missing_fraction[missing_fraction > threshold].index
    print(f"Dropped columns: {list(to_drop)}")
    return df.drop(columns=to_drop)


def zeros_to_nan(df, columns):
    """Replace the zeros with NaN in the given columns.

    Args:
        df (pandas.DataFrame): the dataset.
        columns (list): names of the columns where 0 is impossible.

    Returns:
        pandas.DataFrame: the dataset with NaN instead of 0.
    """
    df = df.copy()  # avoid modifying the original dataframe
    for col in columns:
        n_zeros = (df[col] == 0).sum()
        df[col] = df[col].replace(0, np.nan)
        print(f"{col}: {n_zeros} zeros replaced with NaN")
    return df


def fill_income(df):
    """Fill the missing values of income with the category 'unknown'.

    Args:
        df (pandas.DataFrame): the dataset.

    Returns:
        pandas.DataFrame: the dataset with no missing income.
    """
    df = df.copy()  # avoid modifying the original dataframe
    df["income"] = df["income"].fillna("unknown")
    return df


def clean_data(df):
    """Apply all the cleaning steps to the SUPPORT2 dataset.

    Args:
        df (pandas.DataFrame): the raw dataset.

    Returns:
        pandas.DataFrame: the cleaned dataset.
    """
    df = drop_mostly_missing(df)
    df = zeros_to_nan(df, ["hrt", "resp", "meanbp"])
    df = fill_income(df)
    return df
