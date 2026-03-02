# COVID-19 Global Data Analysis (2020–2025)

## 📌 Project Overview

This project analyzes global COVID-19 data using Python and real-time open datasets from Our World in Data (OWID).

The analysis includes:

- Country-level comparisons (Italy, France, Germany, Spain)
- ICU patient trends (2022–2023)
- Yearly hospitalization aggregation (2021)
- New cases evolution in Italy (2022)
- Total case growth analysis
- Continental case distribution

The dataset is dynamically downloaded during execution.

---

## 🛠 Tech Stack

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🧠 Technical Approach

- Direct data extraction from OWID GitHub repository
- Data cleaning and preprocessing
- Date parsing and time-series handling
- Aggregation by year and continent
- Cross-country ICU comparison
- Visualization of trends and cumulative metrics

---

## 📊 Data Source

Official dataset:

https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv

---

## 📊 Visual Examples

### Italy – New Cases Trend (2022)
![Italy New Cases](screenshots/italy_new_cases_2022.jpeg)

### Italy – Total Cases Evolution
![Italy Total Cases](screenshots/italy_total_cases_evolution.jpeg)

### ICU Comparison (2022–2023)
![ICU Comparison](screenshots/icu_comparison_2022_2023.jpeg)

### Global Cases by Continent
![Cases by Continent](screenshots/cases_by_continent.jpeg)

---

## 📌 Key Insights

- Global COVID-19 cases peaked in 2022.
- ICU occupancy significantly decreased in 2023 compared to 2022.
- Asia and Europe recorded the highest cumulative case counts.
- Italy experienced high volatility in early 2022, followed by stabilization.
- Post-2022 data indicates reduced severe case pressure on healthcare systems.

---

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/tonyesse02/covid-global-data-analysis.git
   cd covid-global-data-analysis
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Launch the notebook**
```bash
   jupyter notebook notebooks/covid_global_analysis.ipynb
```

covid-global-data-analysis/
├── notebooks/
│   └── covid_global_analysis.ipynb
├── screenshots/
├── data/
├── requirements.txt
└── README.md

---

## 👤 Author

Antonio Spagnuolo
Junior Data Analyst
Python | Pandas | Data Visualization



