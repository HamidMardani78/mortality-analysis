"""Functions to load the SUPPORT2 dataset."""

import os

import pandas as pd


def load_data(path="data/support2.csv"):
    """Load the SUPPORT2 dataset from a CSV file.

    Args:
        path (str): path of the CSV file.

    Returns:
        pandas.DataFrame: the dataset, one row per patient.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"File {path} not found. Download it from https://hbiostat.org/data/"
        )

    df = pd.read_csv(path, index_col=0)
    print(f"Loaded {df.shape[0]} patients and {df.shape[1]} columns")
    return df