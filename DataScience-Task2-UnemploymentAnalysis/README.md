# Oasis Infobyte – Data Science Internship

## Task 2: Unemployment Analysis with Python

### 📌 Project Overview

This project analyzes unemployment trends in India using **Exploratory Data Analysis (EDA)** and data visualization techniques.

The analysis focuses on regional unemployment differences, rural and urban unemployment, monthly trends, state-level unemployment patterns, and changes in employment conditions during the COVID-19 period.

---

## 🎯 Objective

The main objectives of this project are:

* Analyze unemployment rates across different regions of India.
* Compare unemployment between rural and urban areas.
* Identify monthly unemployment trends.
* Analyze unemployment trends for selected states.
* Identify the top 10 regions with the highest average unemployment rates.
* Study relationships between unemployment, employment, and labour participation.
* Compare employment conditions before and during the COVID-19 period.

---

## 📊 Dataset

The project uses the **Unemployment in India** dataset.

The dataset contains information about:

* Region
* Date
* Frequency
* Estimated Unemployment Rate (%)
* Estimated Employed
* Estimated Labour Participation Rate (%)
* Area

### Dataset Information

* **Initial records:** 768
* **Records after removing empty rows:** 740
* **Columns:** 7
* **Regions:** 28
* **Areas:** Rural and Urban
* **Time period:** May 2019 – June 2020
* **Missing values after cleaning:** 0
* **Duplicate rows:** 0

The dataset contains both pre-COVID observations and observations from the initial COVID-19 period. Therefore, this project uses **Pre-COVID vs COVID Period** rather than a post-COVID comparison.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 🔍 Data Preparation

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Removed completely empty rows.
3. Cleaned whitespace from column names.
4. Renamed columns for easier analysis.
5. Cleaned text columns.
6. Converted the `Date` column into datetime format.
7. Checked for missing values.
8. Checked for duplicate records.
9. Created year, month, and month-name features.
10. Verified the final dataset structure and data types.

---

## 📈 Exploratory Data Analysis

### 1. Average Unemployment Rate by Region

The average unemployment rate was calculated for each region and visualized using a bar chart.

**Key observation:**

* Tripura recorded the highest average unemployment rate at approximately **28.35%**.
* Meghalaya recorded the lowest average unemployment rate at approximately **4.80%**.
* The results show significant regional variation in unemployment.

---

### 2. Rural vs Urban Unemployment

The average unemployment rate was compared between rural and urban areas.

| Area  | Average Unemployment Rate |
| ----- | ------------------------: |
| Urban |                    13.17% |
| Rural |                    10.32% |

**Key observation:**

Urban areas recorded a higher average unemployment rate than rural areas in this dataset.

---

### 3. Month-Wise Unemployment Trend

Monthly average unemployment rates were analyzed to identify changes over time.

The most significant increase occurred in **April**, when the average unemployment rate reached approximately **23.64%**.

This sharp increase corresponds to the initial COVID-19 period represented in the dataset.

---

### 4. State-Level Time-Series Analysis

Unemployment trends were analyzed for:

* Tamil Nadu
* Maharashtra
* Karnataka

All three states experienced a significant increase in unemployment during the COVID-19 period.

Among these states, **Tamil Nadu showed the largest visible spike**, reaching approximately **49% in May 2020**.

---

### 5. Top 10 Regions with Highest Average Unemployment

The top 10 regions were:

| Rank | Region           | Average Unemployment |
| ---: | ---------------- | -------------------: |
|    1 | Tripura          |               28.35% |
|    2 | Haryana          |               26.28% |
|    3 | Jharkhand        |               20.59% |
|    4 | Bihar            |               18.92% |
|    5 | Himachal Pradesh |               18.54% |
|    6 | Delhi            |               16.50% |
|    7 | Jammu & Kashmir  |               16.19% |
|    8 | Chandigarh       |               15.99% |
|    9 | Rajasthan        |               14.06% |
|   10 | Uttar Pradesh    |               12.55% |

---

## 🔗 Correlation Analysis

Correlation analysis was performed between:

* Unemployment Rate
* Estimated Employed
* Labour Participation Rate

| Variables                                     | Correlation |
| --------------------------------------------- | ----------: |
| Unemployment Rate ↔ Employed                  |       -0.22 |
| Unemployment Rate ↔ Labour Participation Rate |        0.00 |
| Employed ↔ Labour Participation Rate          |        0.01 |

### Observation

There is a weak negative correlation between unemployment rate and estimated employment.

The other relationships show almost no linear correlation in this dataset.

> Correlation indicates association between variables and does not prove causation.

---

## 🦠 Pre-COVID vs COVID-Period Analysis

The dataset was divided into two periods:

* **Pre-COVID:** May 2019 – February 2020
* **COVID Period:** March 2020 – June 2020

### Unemployment Rate

| Period       | Average |
| ------------ | ------: |
| Pre-COVID    |   9.51% |
| COVID Period |  17.77% |

The average unemployment rate increased by approximately **8.27 percentage points** during the COVID period.

### Labour Participation Rate

| Period       | Average |
| ------------ | ------: |
| Pre-COVID    |  43.89% |
| COVID Period |  39.33% |

The average labour participation rate decreased by approximately **4.56 percentage points**.

### Estimated Employment

| Period       | Average Estimated Employment |
| ------------ | ---------------------------: |
| Pre-COVID    |                 7.47 million |
| COVID Period |                 6.52 million |

Estimated employment decreased by approximately **0.95 million** during the COVID period.

---

## 💡 Key Insights

* Unemployment varied considerably across Indian regions.
* Tripura had the highest average unemployment rate among the regions analyzed.
* Meghalaya had the lowest average unemployment rate.
* Urban unemployment was higher than rural unemployment.
* April recorded the highest monthly average unemployment rate.
* Tamil Nadu experienced the largest visible unemployment spike among the three selected states.
* The average unemployment rate increased substantially during the COVID period.
* Labour participation decreased during the COVID period.
* Estimated employment also decreased during the COVID period.
* The impact of COVID-19 was not uniform across different regions.

---

## 📁 Project Structure

```text
DataScience-Task2-UnemploymentAnalysis/
│
├── Unemployment_Analysis.ipynb
├── Unemployment in India.csv
├── README.md
└── screenshots/
    ├── region_unemployment.png
    ├── rural_vs_urban.png
    ├── monthly_trend.png
    ├── state_time_series.png
    ├── top_10_regions.png
    ├── correlation_heatmap.png
    ├── covid_unemployment.png
    ├── covid_labour_participation.png
    └── covid_employment.png
```

---

## 🚀 Conclusion

This project demonstrates how Python-based Exploratory Data Analysis can be used to understand unemployment and employment patterns.

The analysis identified significant regional differences and temporal variations in unemployment. The COVID period represented in the dataset showed a substantial increase in unemployment along with decreases in labour participation and estimated employment.

Overall, the project demonstrates the importance of data analysis and visualization in identifying employment trends and understanding major changes in labour-market conditions.

---

## 👨‍💻 Author

**Madesh P**

B.Tech Artificial Intelligence and Data Science
CARE College of Engineering

### Skills Demonstrated

* Python
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Statistical Analysis
* Matplotlib
* Seaborn

---

## 📌 Internship

**Oasis Infobyte – Data Science Internship**

**Task 2: Unemployment Analysis with Python**
