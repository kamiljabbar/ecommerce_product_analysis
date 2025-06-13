import pandas as pd
import numpy as np

def generate_data(start_date="2024-01-01", end_date="2024-06-30", seed=42, output_path="data/product_data.csv"):
    np.random.seed(seed)
    date_range = pd.date_range(start=start_date, end=end_date, freq="D")
    products = [
        {"product_id": "SKU001", "category": "Widgets", "base_price": 20, "base_cost": 10},
        {"product_id": "SKU002", "category": "Widgets", "base_price": 25, "base_cost": 12},
        {"product_id": "SKU003", "category": "Gadgets", "base_price": 50, "base_cost": 30},
        {"product_id": "SKU004", "category": "Gadgets", "base_price": 60, "base_cost": 35},
        {"product_id": "SKU005", "category": "Accessories", "base_price": 15, "base_cost": 7},
        {"product_id": "SKU006", "category": "Accessories", "base_price": 18, "base_cost": 9},
        {"product_id": "SKU007", "category": "Devices", "base_price": 100, "base_cost": 60},
        {"product_id": "SKU008", "category": "Devices", "base_price": 120, "base_cost": 70}
    ]
    data = []
    for date in date_range:
        month = date.month
        season_factor = 1.0 + 0.2 * np.sin((month-1)/12 * 2*np.pi)
        for prod in products:
            cat_factor = {"Widgets": 5, "Gadgets": 3, "Accessories": 4, "Devices": 2}[prod["category"]]
            mean_sales = (cat_factor + np.random.uniform(-1, 1)) * season_factor
            units_sold = np.random.poisson(lam=max(mean_sales, 0.5))
            promo = np.random.choice([0, 0.1, 0.2], p=[0.8, 0.15, 0.05])
            price = prod["base_price"] * (1 - promo) * np.random.uniform(0.95, 1.05)
            revenue = units_sold * price
            cost = units_sold * prod["base_cost"]
            profit = revenue - cost
            returns = np.random.binomial(units_sold, p=0.05 + 0.01*np.random.randn()) if units_sold > 0 else 0
            num_ratings = np.random.poisson(lam=units_sold * 0.3)
            if num_ratings > 0:
                ratings = np.random.normal(loc=4.0, scale=0.6, size=num_ratings)
                ratings = np.clip(ratings, 1, 5)
                avg_rating = ratings.mean()
            else:
                avg_rating = np.nan
            data.append({
                "date": date,
                "product_id": prod["product_id"],
                "category": prod["category"],
                "units_sold": units_sold,
                "price": round(price, 2),
                "revenue": round(revenue, 2),
                "cost": round(cost, 2),
                "profit": round(profit, 2),
                "returns": returns,
                "avg_rating": round(avg_rating, 2) if not np.isnan(avg_rating) else np.nan
            })
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Synthetic product data saved to {output_path}")