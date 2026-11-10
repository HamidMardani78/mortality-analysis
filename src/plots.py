"""Functions to plot the results of the SUPPORT2 analysis."""

import matplotlib.pyplot as plt


def plot_mortality_by_group(table, title, filename=None):
    """Draw a horizontal bar chart of the mortality rate of each group.

    Args:
        table (pandas.DataFrame): output of the function mortality_by_group.
        title (str): title of the chart.
        filename (str): if given, the chart is also saved to this file.
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(table.index.astype(str), table["mortality_rate"], color="steelblue")
    ax.invert_yaxis()
    ax.set_xlim(0, table["mortality_rate"].max() + 8)
    ax.set_xlabel("In-hospital mortality (%)")
    ax.set_title(title)

    for i, rate in enumerate(table["mortality_rate"]):
        ax.text(rate + 0.5, i, f"{rate}%", va="center")

    plt.tight_layout()
    if filename is not None:
        fig.savefig(filename, dpi=150)
    plt.show()