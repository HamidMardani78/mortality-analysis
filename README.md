# In-Hospital Mortality Analysis (SUPPORT2)

Exploratory analysis of the factors associated with in-hospital mortality
in seriously ill hospitalized adults.

Project for the Python module of *Coding for Data Science and Data Management*,
University of Milan, A.Y. 2026/27.

## Research question

Which factors (disease type, age, cancer status, sex, income, severity of illness)
are associated with dying in hospital?

## Dataset

**SUPPORT2** (Study to Understand Prognoses Preferences Outcomes and Risks of Treatment):
9105 seriously ill adults hospitalized in 5 US medical centers between 1989 and 1994.

- Source: Vanderbilt University, Department of Biostatistics - https://hbiostat.org/data/
  (file `support2csv.zip`)
- Description of the variables: https://hbiostat.org/data/repo/Csupport2.html
- Target variable: `hospdead` (1 = died in hospital, 0 = survived to discharge)

The CSV file is included in the `data/` folder (about 3 MB).

## Project structure

```
mortality-analysis/
├── data/
│   └── support2.csv          # raw dataset
├── figures/                  # charts saved by the notebooks
├── src/
│   ├── data_loader.py        # load the dataset
│   ├── cleaning.py           # data cleaning functions
│   ├── analysis.py           # statistics (pandas, numpy, scipy)
│   └── plots.py              # charts (matplotlib)
├── 01_exploration.ipynb      # first exploration of the data
├── 02_presentation.ipynb     # final presentation of the results
├── app.py                    # Streamlit dashboard
├── requirements.txt
└── README.md
```

## Installation

Requires Python 3.13.

```bash
git clone https://github.com/HamidMardani78/mortality-analysis.git
cd mortality-analysis
python -m venv .venv
```

Activate the virtual environment:

- Windows: `.venv\Scripts\activate`
- macOS / Linux: `source .venv/bin/activate`

Install the libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the interactive dashboard from the project folder:

```bash
streamlit run app.py
```

The app opens in the browser at http://localhost:8501. It has three tabs:
mortality by group (with a chi-square test), survived vs died (boxplots and
summary statistics), and the cleaned data (with a filter and a CSV download).

The same analysis is also available as a notebook:

```bash
jupyter notebook 02_presentation.ipynb
```

## Main findings

- Coma (60.7%) and multiple organ failure (52.7%) are the most lethal conditions.
- Mortality increases with age after 50 (from 22.7% to 31.2% for patients over 80).
- The APACHE III severity score clearly separates survivors from non-survivors.
- Sex and income are not associated with mortality.
- Patients with metastatic cancer have low in-hospital mortality but very high mortality after discharge.

## Libraries

pandas, numpy, scipy, matplotlib, jupyter, streamlit (see `requirements.txt` for versions).

## Author

Hamidreza Mardani