
import sqlite3
import pandas as pd
from pathlib import Path

# Project paths
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data" / "processed"
DB_PATH = ROOT_DIR / "ecommerce_demand.db"

# CSV files and their SQL table names
FILES = {
    "calendar_cleaned.csv": "calendar",
    "xgboost_forecast.csv": "xgboost_forecast",
    "final_model_comparison.csv": "model_comparison",
    "inventory_recommendations.csv": "inventory_recommendations",
    "price_demand_analysis.csv": "price_demand_analysis"
}

# Column name mappings
COLUMN_MAPPINGS = {
    "calendar": {
        "week day": "week_day",
        "event name 1": "event_name_1",
        "event type 1": "event_type_1",
        "event name 2": "event_name_2",
        "event type 2": "event_type_2"
    },
    "xgboost_forecast": {
        "dates": "date",
        "actual": "actual_sales",
        "xgboost_forecast": "forecast_sales"
    },
    "model_comparison": {
        "Model": "model",
        "MAE": "mae",
        "RMSE": "rmse",
        "WMAPE (%)": "wmape"
    },
    "price_demand_analysis": {
        "price range": "price_range",
        "total units": "total_units",
        "weekly records": "weekly_records",
        "avg weekly demands": "avg_weekly_demand"
    }
}

def load_database():

    print("Starting SQLite database creation...\n")

    with sqlite3.connect(DB_PATH) as connection:

        for filename, table_name in FILES.items():

            file_path = DATA_DIR / filename

            if not file_path.exists():
                raise FileNotFoundError(
                    f"Missing file: {file_path}"
                )

            df = pd.read_csv(file_path)

            # Standardize column names
            df.rename(
                columns=COLUMN_MAPPINGS.get(table_name, {}),
                inplace=True
            )

            # Standardize date columns
            if "date" in df.columns:
                df["date"] = pd.to_datetime(
                    df["date"]
                ).dt.strftime("%Y-%m-%d")

            # Import into SQLite
            df.to_sql(
                table_name,
                connection,
                if_exists="replace",
                index=False
            )

            print(
                f"Imported {filename} -> {table_name} "
                f"({len(df):,} rows)"
            )

        # Create useful indexes
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_forecast_date "
            "ON xgboost_forecast(date)"
        )

        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_inventory_category "
            "ON inventory_recommendations(cat_id)"
        )

        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_inventory_store "
            "ON inventory_recommendations(store_id)"
        )

        print("\nDatabase created successfully!")

    print(f"Database location: {DB_PATH}")


if __name__ == "__main__":
    load_database()
