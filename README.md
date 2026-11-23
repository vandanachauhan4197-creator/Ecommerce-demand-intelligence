# E-commerce Demand Intelligence & Inventory Optimization Platform

An end-to-end Data Science and Business Intelligence project focused on historical retail demand analysis, time-series forecasting, model evaluation, and inventory replenishment recommendations.

The project uses the **Walmart M5 Forecasting dataset** to explore retail sales patterns, build forecasting models, and translate analytical results into business insights through an interactive Power BI dashboard.

## Project Objectives

- Analyse historical retail sales data.
- Identify trends, seasonality, and demand patterns.
- Perform statistical time-series analysis.
- Build and evaluate 90-day aggregate demand forecasts.
- Compare statistical and machine learning forecasting models.
- Generate product-store-level inventory and replenishment recommendations using simulated inventory assumptions.
- Develop an interactive Power BI dashboard for business insights.

## Technology Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Time-Series Analysis:** Statsmodels
- **Forecasting Models:** ARIMA, SARIMA, Prophet, XGBoost
- **Business Intelligence:** Power BI
- **Additional Tools:** SQL, Git, GitHub

## Project Structure

```text
ecommerce-demand-intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection_and_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_time_series_analysis.ipynb
│   ├── 05_stationarity_and_decomposition.ipynb
│   ├── 06_arima_sarima.ipynb
│   ├── 07_prophet_forecasting.ipynb
│   ├── 08_xgboost_forecasting.ipynb
│   ├── 09_model_comparison.ipynb
│   └── 10_inventory_optimization.ipynb
│
├── src/
├── sql/
├── dashboard/
├── models/
├── reports/
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Forecasting Model Performance

Models were evaluated on a 90-day test period using MAE, RMSE, and WMAPE.

| Model | MAE | RMSE | WMAPE |
|---|---:|---:|---:|
| XGBoost | 2,615.99 | 3,452.68 | **6.25%** |
| Prophet | 2,805.37 | 3,575.99 | 6.70% |
| Seasonal Naive | 4,341.66 | 5,117.31 | 10.37% |
| SARIMA | 4,450.62 | 5,361.63 | 10.63% |
| ARIMA | 5,712.29 | 7,816.71 | 13.65% |

**Best-performing model: XGBoost**, based on the lowest WMAPE on the evaluated test period.

## Inventory Optimization

A product-store-level replenishment analysis was developed using historical demand statistics.

Key components:

- Average daily demand
- Demand standard deviation
- Safety stock
- Reorder point
- Target stock
- Recommended order quantity

**Illustrative simulation results:**

- Product-store combinations analysed: 30,490
- Items requiring reorder: 12,472
- Items with sufficient simulated stock: 18,018
- Total recommended order quantity: 121,648 units

Inventory levels and lead-time assumptions are simulated because the original dataset does not provide actual on-hand inventory or supplier lead times.

## Power BI Dashboard

The interactive Power BI report contains four pages:

### 1. Executive Overview

![Executive Overview](reports/executive_overview.png)

### 2. Demand Forecasting

![Demand Forecasting](reports/demand_forecasting.png)

### 3. Inventory Intelligence

![Inventory Intelligence](reports/inventory_intelligence.png)

### 4. Business Insights

![Business Insights](reports/business_insights.png)

## Key Insights

- XGBoost achieved the best forecasting performance among the evaluated models.
- Weekly seasonality plays an important role in historical retail demand.
- FOODS contributed the largest share of historical unit sales.
- Lower price bands showed higher average weekly demand in the descriptive price-band analysis.
- Inventory recommendations highlight replenishment requirements across product-store combinations.

## Data Source

**Primary Dataset:** Walmart M5 Forecasting Dataset.

The analysis uses historical retail sales, calendar information, and related dataset files.

## Limitations

- Forecasting is performed at an aggregate daily sales level, not at individual product or store level.
- Inventory recommendations are based on simulated stock levels and assumed lead times.
- The price-demand analysis is descriptive and does not establish a causal relationship.
- Forecast performance reflects the selected historical test period and may differ on future data.

## Project Status

**Completed:**
- Data collection and cleaning
- Exploratory data analysis
- Time-series analysis and decomposition
- ARIMA, SARIMA, Prophet and XGBoost modelling
- Model comparison and selection
- Inventory optimization analysis
- Four-page Power BI dashboard

**Further development:**
- SQL-based business analysis
- Streamlit dashboard
- Reproducible deployment and documentation

---

*Built as an end-to-end retail analytics project combining Data Science, forecasting, inventory intelligence, and business reporting.*