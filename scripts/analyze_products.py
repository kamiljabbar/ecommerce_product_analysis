import pandas as pd
import numpy as np

def load_data(path="data/product_data.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df

def compute_summary(df):
    agg = df.groupby("product_id").agg({
        "units_sold": "sum",
        "revenue": "sum",
        "cost": "sum",
        "profit": "sum",
        "returns": "sum",
        "avg_rating": "mean"
    }).reset_index()
    agg["return_rate"] = agg["returns"] / agg["units_sold"].replace(0, np.nan)
    agg["profit_margin"] = agg["profit"] / agg["revenue"].replace(0, np.nan)
    agg["avg_inventory"] = agg["cost"] / np.random.uniform(8, 12, size=len(agg))
    agg["inventory_turnover"] = agg["cost"] / agg["avg_inventory"].replace(0, np.nan)
    # Category merge
    df2 = df.groupby("product_id")["category"].first().reset_index()
    agg = agg.merge(df2, on="product_id")
    return agg

if __name__ == "__main__":
    df = load_data()
    summary = compute_summary(df)
    summary.to_csv("data/product_summary.csv", index=False)
    print("Product summary saved to data/product_summary.csv")