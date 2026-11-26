# E-commerce Demand Intelligence & Inventory Optimization Platform

An end-to-end Data Science and Business Intelligence project focused on historical retail demand analysis, time-series forecasting, model evaluation, inventory optimization, and API development.

The project uses the **Walmart M5 Forecasting dataset** to explore retail sales patterns, build forecasting models, generate product-store-level replenishment recommendations, and translate analytical results into business insights through Power BI and a FastAPI backend.

## Project Objectives

- Analyse historical retail sales data.
- Identify trends, seasonality, and demand patterns.
- Perform statistical time-series analysis.
- Build and evaluate 90-day aggregate demand forecasts.
- Compare statistical and machine learning forecasting models.
- Generate product-store-level inventory recommendations using simulated inventory assumptions.
- Develop an interactive Power BI dashboard.
- Build REST API endpoints using FastAPI.
- Perform SQL-based business analysis.

## Technology Stack

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Time-Series Analysis:** Statsmodels
- **Forecasting Models:** ARIMA, SARIMA, Prophet, XGBoost
- **Business Intelligence:** Power BI
- **Backend Development:** FastAPI, Uvicorn
- **Database:** SQLite, SQL
- **Testing:** Pytest, HTTPX
- **Development Tools:** Jupyter Notebook, Git, GitHub

## Project Structure

```text
ecommerce-demand-intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_time_series_analysis.ipynb
│   ├── 05_stationarity_and_decomposition.ipynb
│   ├── 06_arima_sarima.ipynb
│   ├── 07_prophet_forecasting.ipynb
│   ├── 08_xgboost_forecasting.ipynb
│   ├── 09_model_comaprison.ipynb
│   └── 10_inventory_optimization.ipynb
│
├── src/
│   ├── main.py
│   ├── data_collection.py
│   ├── feature_engineering.py
│   ├── forecasting.py
│   ├── preprocessing.py
│   ├── inventry_optimizer.py
│   └── load_sql_database.py
│
├── sql/
│   ├── analysis.sql
│   └── schema.sql
│
├── dashboard/
│   ├── E-commerce project report.pbix
│   └── E-commerce project.pdf
│
├── models/
├── reports/
├── tests/
│   └── test_api.py
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

The forecasting model predicts aggregate daily sales rather than individual product or store demand.

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

## SQL Analytics

SQLite was used to store and query the processed project datasets.

The database contains five analytical tables:

- `calendar`
- `xgboost_forecast`
- `model_comparison`
- `inventory_recommendations`
- `price_demand_analysis`

SQL queries were developed to analyse:

- Inventory and replenishment summaries
- Model performance rankings
- Category-wise replenishment requirements
- Store-wise inventory status
- Top products requiring replenishment
- Monthly actual sales
- Price-band demand patterns
- Forecast accuracy

## FastAPI Application

A REST API was developed using **FastAPI** to expose the project's forecasting, inventory, and business analytics results.

### Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| GET | `/api/overview` | Overall project metrics |
| GET | `/api/forecast` | 90-day actual vs forecast data |
| GET | `/api/inventory` | Category-wise and store-wise inventory summaries |
| GET | `/api/replenishment` | Paginated replenishment records with filters |
| GET | `/api/business-insights` | Price-demand insights and forecast accuracy |

The replenishment endpoint supports:

- Pagination using `limit` and `offset`
- Category filtering
- Store filtering
- Replenishment status filtering

### Running the API Locally

1. Clone the repository:

```bash
git clone https://github.com/vandanachauhan4197-creator/Ecommerce-demand-intelligence.git
cd Ecommerce-demand-intelligence
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure the processed CSV files are available in `data/processed/`.

4. Create the SQLite database:

```bash
python src/load_sql_database.py
```

5. Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

6. Open the interactive