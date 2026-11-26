"""Functions to plot the results of the SUPPORT2 analysis."""

import matplotlib.pyplot as plt


def plot_mortality_by_group(table, title, filename=None):
    """Draw a horizontal bar chart of the mortality rate of each group.

    Args:
        table (pandas.DataFrame): output of the function mortality_by_group.
        title (str): title of the chart.
        filename (str): if given, the chart is also saved to this file.
         
    Returns:
        matplotlib.figure.Figure: the figure with the chart.
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(table.index.astype(str),
            table["mortality_rate"], color="steelblue")
    ax.invert_yaxis()
    ax.set_xlim(0, table["mortality_rate"].max() + 8)
    ax.set_xlabel("In-hospital mortality (%)")
    ax.set_title(title)

    for i, rate in enumerate(table["mortality_rate"]):
        ax.text(rate + 0.5, i, f"{rate}%", va="center")

    plt.tight_layout()
    if filename is not None:
        fig.savefig(filename, dpi=150)

    return fig


def plot_survived_vs_died(df, column, label, filename=None):
    """Draw two boxplots to compare a numeric column between the two groups.

    Args:
        df (pandas.DataFrame): the cleaned dataset.
        column (str): name of the numeric column to compare.
        label (str): description of the column, used for the axis.
        filename (str): if given, the chart is also saved to this file.
        
    Returns:
        matplotlib.figure.Figure: the figure with the chart.
    """
    survived = df.loc[df["hospdead"] == 0, column].dropna()
    died = df.loc[df["hospdead"] == 1, column].dropna()

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.boxplot([survived, died], tick_labels=["Survived", "Died"])
    ax.set_ylabel(label)
    ax.set_title(f"{label}: survived vs died")

    plt.tight_layout()
    if filename is not None:
        fig.savefig(filename, dpi=150)

    return fig
