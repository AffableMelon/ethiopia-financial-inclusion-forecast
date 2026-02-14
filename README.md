# Forecasting Financial Inclusion in Ethiopia

A forecasting system that tracks Ethiopia's digital financial transformation using time series methods.

## 📋 Project Overview

This project builds a forecasting system that predicts Ethiopia's progress on the two core dimensions of financial inclusion as defined by the World Bank's Global Findex:

- **ACCESS** — Account Ownership Rate
- **USAGE** — Digital Payment Adoption Rate

### Business Context

Ethiopia is undergoing rapid digital financial transformation:
- Telebirr has grown to over 54 million users since launching in 2021
- M-Pesa entered the market in 2023 and now has over 10 million users
- Interoperable P2P digital transfers have surpassed ATM cash withdrawals
- Yet only 49% of Ethiopian adults have a financial account (2024 Global Findex)

## 🚀 Project Setup

### Prerequisites
- Python 3.10+
- pip or conda

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Forecasting-Financial-Inclusion.git
cd Forecasting-Financial-Inclusion
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Required Packages
```
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
jupyter
pytest
```

## 📁 Project Structure

```
Forecasting-Financial-Inclusion/
├── data/
│   ├── processed/
│   │   ├── ethiopia_fi_unified_data.csv
│   │   ├── event_indicator_matrix.csv
│   │   ├── forecast_results_2025_2027.csv
│   │   ├── impact_links.csv
│   │   ├── modeled_event_impacts.csv
│   │   ├── reference_codes.csv
│   ├── raw/
│   │   ├── enrichment_A_baselines.csv
│   │   ├── enrichment_B_direct.csv
│   │   ├── enrichment_C_indirect.csv
│   │   ├── enrichment_D_nuances.csv
│   │   ├── ethiopia_fi_unified_data.csv
│   │   ├── impact_links.csv
│   │   ├── README.md
│   │   ├── reference_codes.csv
├── notebooks/
│   ├── README.md
│   ├── task_1_exploration_enrichment.ipynb
│   ├── task_2_eda.ipynb
│   ├── task_3_modeling.ipynb
│   ├── task_4_forecasting.ipynb
├── src/
│   └── __init__.py
├── dashboard/
│   └── app.py
├── models/
├── reports/
│   └── figures/
├── tests/
│   └── __init__.py
├── context.md
├── data_enrichment_log.md
├── requirements.txt
└── README.md
```

## 📊 Task 1: Data Exploration and Enrichment

### Objective
Understand the starter dataset and enrich it with additional data useful for forecasting ACCESS and USAGE indicators.

### Key Findings

#### Dataset Structure
The unified schema uses `record_type` to categorize data:
| Record Type | Count | Description |
|-------------|-------|-------------|
| observation | 30 | Measured values from surveys, reports, operators |
| event | 10 | Policies, product launches, market entries, milestones |
| target | 3 | Official policy goals (NFIS-II targets) |
| impact_link | 14 | Modeled relationships between events and indicators |

#### Account Ownership Trajectory (Core ACCESS Indicator)
| Year | Rate | Change |
|------|------|--------|
| 2011 | 14% | — |
| 2014 | 22% | +8pp |
| 2017 | 35% | +13pp |
| 2021 | 46% | +11pp |
| 2024 | 49% | +3pp |

#### Data Enrichment Summary
| Addition Type | Count | Examples |
|---------------|-------|----------|
| New Observations | 3 | 2011 baseline, 2024 digital payment usage, wages via account |

### Outputs
- 📓 `notebooks/task_1_exploration_enrichment.ipynb` — Full exploration and enrichment code
- 📄 `data_enrichment_log.md` — Detailed documentation of all additions
- 📊 `data/processed/ethiopia_fi_unified_data.csv` — Enriched dataset

## 📈 Task 2: Exploratory Data Analysis

### Objective
Analyze patterns and factors influencing financial inclusion in Ethiopia.

### Key Insights

Based on the notebook code, the EDA explores:
- Dataset summary by record_type, pillar, source_type
- Temporal coverage
- Indicator uniqueness
- Account ownership trends
- Mobile money and digital payment patterns

### Outputs
- 📓 `notebooks/task_2_eda.ipynb` — Full EDA with visualizations

## 🎯 Task 3: Event Impact Modeling

### Objective
Model how events (policies, product launches, infrastructure investments) affect financial inclusion indicators.

### Methodology

The notebook loads impact_links and joins with events to build an event-indicator matrix.

### Outputs
- 📓 `notebooks/task_3_modeling.ipynb` — Full analysis notebook
- 📊 `data/processed/event_indicator_matrix.csv` — Event-indicator associations

## 📈 Task 4: Forecasting Access and Usage

### Objective
Forecast Account Ownership (ACCESS) and Digital Payment Usage for 2025-2027.

### Methodology
The notebook implements forecasting models using trend regression and event-augmented approaches.

### Outputs
- 📓 `notebooks/task_4_forecasting.ipynb` — Forecasting notebook
- 📊 `data/processed/forecast_results_2025_2027.csv` — Forecast table

## 📱 Task 5: Interactive Dashboard

### Objective
Create an interactive dashboard enabling stakeholders to explore data, understand event impacts, and view forecasts.

### Dashboard Features

The Streamlit dashboard (`dashboard/app.py`) includes sections:

#### 📊 Overview Page
- Key metrics summary cards
- P2P vs ATM crossover indicator

#### 📈 Trends Analysis Page
- Interactive time series plots

#### 🔮 Forecasts Page
- Forecast visualizations

#### 🎯 Event Impacts and Inclusion Projections Pages
- Additional analysis views

### Running the Dashboard Locally

1. **Ensure dependencies are installed**
```bash
pip install -r requirements.txt
```

2. **Start the dashboard**
```bash
cd /path/to/Forecasting-Financial-Inclusion
streamlit run dashboard/app.py
```

3. **Access the dashboard**
Open your browser to `http://localhost:8501`

## 👥 Team

**Tutors**: Kerod, Mahbubah, Filimon

## 📅 Key Dates

- Challenge Introduction: January 28, 2026
- Interim Submission: February 1, 2026
- Final Submission: February 3, 2026

## 📚 Data Sources

- [World Bank Global Findex](https://www.worldbank.org/en/publication/globalfindex)
- [IMF Financial Access Survey](https://data.imf.org/?sk=E5DCAB7E-A5CA-4892-A6EA-598B5463A34C)
- [GSMA Intelligence](https://www.gsma.com/intelligence/)
- National Bank of Ethiopia
- Ethio Telecom Reports
- EthSwitch Annual Reports

---

*Selam Analytics — Financial Technology Consulting for Emerging Markets*</content>
<parameter name="filePath">/home/marshy/FOSS/repos/tenx/w10/README.md