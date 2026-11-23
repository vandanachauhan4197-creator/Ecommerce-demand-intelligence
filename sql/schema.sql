
-- E-commerce Demand Intelligence
-- Database Schema

CREATE TABLE calendar (
    date DATE PRIMARY KEY,
    wm_yr_wk INTEGER,
    week_day TEXT,
    w_day INTEGER,
    month INTEGER,
    year INTEGER,
    event_name_1 TEXT,
    event_type_1 TEXT,
    event_name_2 TEXT,
    event_type_2 TEXT,
    snap_ca INTEGER,
    snap_tx INTEGER,
    snap_wi INTEGER
);

CREATE TABLE xgboost_forecast (
    date DATE PRIMARY KEY,
    actual_sales REAL,
    forecast_sales REAL
);

CREATE TABLE model_comparison (
    model TEXT PRIMARY KEY,
    mae REAL,
    rmse REAL,
    wmape REAL
);

CREATE TABLE inventory_recommendations (
    item_id TEXT,
    store_id TEXT,
    cat_id TEXT,
    dept_id TEXT,
    state_id TEXT,
    simulated_on_hand_stock INTEGER,
    reorder_point REAL,
    target_stock REAL,
    replenishment_status TEXT,
    recommended_order_qty INTEGER,
    total_sales INTEGER,
    avg_daily_demand REAL,
    demand_std REAL,
    safety_stock REAL,
    PRIMARY KEY (item_id, store_id)
);

CREATE TABLE price_demand_analysis (
    price_range TEXT PRIMARY KEY,
    total_units INTEGER,
    weekly_records INTEGER,
    avg_weekly_demand REAL
);
