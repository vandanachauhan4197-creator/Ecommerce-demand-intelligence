import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "ecommerce_demand.db"

from fastapi import FastAPI, Query, HTTPException

app = FastAPI(
    title="E-commerce Demand Intelligence API",
    description="An API for demand forecasting, inventory optimization and business insights.",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "message": "E-commerce Demand Intelligence API is running!",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
@app.get("/api/overview")
def get_overview():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        inventory = conn.execute("""
            SELECT
                COUNT(*) AS total_items,
                SUM(CASE WHEN replenishment_status = 'Reorder'
                    THEN 1 ELSE 0 END) AS reorder_items,
                SUM(CASE WHEN replenishment_status = 'Sufficient'
                    THEN 1 ELSE 0 END) AS sufficient_items,
                SUM(recommended_order_qty) AS total_order_qty
            FROM inventory_recommendations
        """).fetchone()

        best_model = conn.execute("""
            SELECT model, wmape
            FROM model_comparison
            ORDER BY wmape ASC
            LIMIT 1
        """).fetchone()

    return {
        "total_items": inventory["total_items"],
        "reorder_items": inventory["reorder_items"],
        "sufficient_items": inventory["sufficient_items"],
        "total_recommended_order_qty": inventory["total_order_qty"],
        "best_model": best_model["model"],
        "best_model_wmape": best_model["wmape"]
    }
@app.get("/api/forecast")
def get_forecast():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        forecast_data = conn.execute("""
            SELECT
                date,
                "Actual" AS actual_sales,
                "XGBoost_Forecast" AS forecast_sales
            FROM xgboost_forecast
            ORDER BY date
        """).fetchall()

    return {
        "total_records": len(forecast_data),
        "forecast": [dict(row) for row in forecast_data]
    }
@app.get("/api/inventory")
def get_inventory():

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        category_data = conn.execute("""
            SELECT
                cat_id AS category,
                COUNT(*) AS total_items,
                SUM(CASE WHEN replenishment_status = 'Reorder'
                    THEN 1 ELSE 0 END) AS reorder_items,
                SUM(recommended_order_qty) AS recommended_order_qty
            FROM inventory_recommendations
            GROUP BY cat_id
            ORDER BY cat_id
        """).fetchall()

        store_data = conn.execute("""
            SELECT
                store_id,
                COUNT(*) AS total_items,
                SUM(CASE WHEN replenishment_status = 'Reorder'
                    THEN 1 ELSE 0 END) AS reorder_items,
                SUM(recommended_order_qty) AS recommended_order_qty
            FROM inventory_recommendations
            GROUP BY store_id
            ORDER BY store_id
        """).fetchall()

    return {
        "category_summary": [dict(row) for row in category_data],
        "store_summary": [dict(row) for row in store_data]
    }
@app.get("/api/replenishment")
def get_replenishment(
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
    category: str | None = None,
    store: str | None = None,
    status: str | None = None
):

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        total_records = conn.execute("""
    SELECT COUNT(*)
    FROM inventory_recommendations
    WHERE (? IS NULL OR cat_id = ?)
    AND (? IS NULL OR store_id = ?)
""", (category, category, store, store)).fetchone()[0]

        records = conn.execute("""
            SELECT
                item_id,
                store_id,
                simulated_on_hand_stock,
                reorder_point,
                target_stock,
                replenishment_status,
                recommended_order_qty
            FROM inventory_recommendations
            WHERE (? IS NULL OR cat_id = ?)
            AND (? IS NULL OR store_id = ?)
            AND (? IS NULL OR replenishment_status = ?)
            ORDER BY recommended_order_qty DESC
            LIMIT ? OFFSET ?
            
            """,(category, category, store, store, status, status, limit, offset)).fetchall()

    return {
        "total_records": total_records,
        "returned_records": len(records),
        "limit": limit,
        "offset": offset,
        "replenishment_data": [dict(row) for row in records]
    }
@app.get("/api/business-insights")
def get_business_insights():

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        price_data = conn.execute("""
            SELECT
                price_range,
                total_units,
                weekly_records,
                avg_weekly_demand
            FROM price_demand_analysis
            ORDER BY avg_weekly_demand DESC
        """).fetchall()

        forecast_accuracy = conn.execute("""
            SELECT
                COUNT(*) AS total_days,
                ROUND(AVG(ABS("Actual" - "XGBoost_Forecast")), 2) AS mae,
                ROUND(
                    SUM(ABS("Actual" - "XGBoost_Forecast"))
                    * 100.0 / SUM("Actual"), 2
                ) AS wmape
            FROM xgboost_forecast
        """).fetchone()

    return {
        "price_demand_insights": [dict(row) for row in price_data],
        "forecast_accuracy": dict(forecast_accuracy)
    }


        