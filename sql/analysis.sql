
-- E-commerce Demand Intelligence
-- Business Analysis Queries

-- 1. Overall Inventory Summary
SELECT
    COUNT(*) AS total_product_store_combinations,
    SUM(recommended_order_qty) AS total_recommended_orders,
    SUM(CASE
        WHEN replenishment_status = 'Reorder' THEN 1
        ELSE 0
    END) AS items_requiring_reorder,
    SUM(CASE
        WHEN replenishment_status = 'Sufficient' THEN 1
        ELSE 0
    END) AS sufficient_stock_items
FROM inventory_recommendations;


-- 2. Forecast Model Performance Ranking
SELECT
    model,
    mae,
    rmse,
    wmape
FROM model_comparison
ORDER BY wmape ASC;


-- 3. Category-wise Replenishment Analysis
SELECT
    cat_id,
    COUNT(*) AS total_items,
    SUM(CASE
        WHEN replenishment_status = 'Reorder' THEN 1
        ELSE 0
    END) AS reorder_items,
    SUM(recommended_order_qty) AS recommended_quantity
FROM inventory_recommendations
GROUP BY cat_id
ORDER BY recommended_quantity DESC;


-- 4. Store-wise Replenishment Analysis
SELECT
    store_id,
    COUNT(*) AS total_items,
    SUM(CASE
        WHEN replenishment_status = 'Reorder' THEN 1
        ELSE 0
    END) AS reorder_items,
    SUM(recommended_order_qty) AS recommended_quantity
FROM inventory_recommendations
GROUP BY store_id
ORDER BY recommended_quantity DESC;


-- 5. Top 10 Products Requiring Replenishment
SELECT
    item_id,
    store_id,
    cat_id,
    recommended_order_qty
FROM inventory_recommendations
WHERE recommended_order_qty > 0
ORDER BY recommended_order_qty DESC
LIMIT 10;


-- 6. Monthly Actual Sales
SELECT
    c.year,
    c.month,
    SUM(f.actual_sales) AS monthly_actual_sales
FROM xgboost_forecast f
JOIN calendar c
    ON f.date = c.date
GROUP BY c.year, c.month
ORDER BY c.year, c.month;


-- 7. Demand by Price Range
SELECT
    price_range,
    total_units,
    avg_weekly_demand
FROM price_demand_analysis
ORDER BY avg_weekly_demand DESC;


-- 8. Overall Forecast Accuracy
SELECT
    model,
    ROUND(wmape, 2) AS wmape_percentage,
    CASE
        WHEN wmape = (
            SELECT MIN(wmape)
            FROM model_comparison
        )
        THEN 'Best Performing Model'
        ELSE 'Other Model'
    END AS model_status
FROM model_comparison
ORDER BY wmape ASC;
