"""Functions to load the SUPPORT2 dataset."""

import os

import pandas as pd

# Columns used by the cleaning, the analysis and the app
REQUIRED_COLUMNS = [
    "hospdead", "age", "sex", "dzclass", "dzgroup", "ca", "income",
    "scoma", "aps", "hrt", "resp", "meanbp",
]


def load_data(path="data/support2.csv"):
    """Load the SUPPORT2 dataset from a CSV file.

    Args:
        path (str): path of the CSV file.

    Returns:
        pandas.DataFrame: the dataset, one row per patient.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the file cannot be read or misses a required column.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"File {path} not found. "
            "Download it from https://hbiostat.org/data/"
        )

    try:
        df = pd.read_csv(path, index_col=0)
    except Exception:
        raise ValueError(f"File {path} could not be read as a CSV file")

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Column {col} is missing in {path}")

    print(f"Loaded {df.shape[0]} patients and {df.shape[1]} columns")
    return df