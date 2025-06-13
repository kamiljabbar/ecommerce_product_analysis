import pandas as pd
import matplotlib.pyplot as plt

def plot_all():
    summary = pd.read_csv("data/product_summary.csv")
    # plot revenue by product
    plt.figure(figsize=(10,6)); plt.bar(summary['product_id'], summary['revenue']); plt.title('Total Revenue by Product'); plt.xticks(rotation=45); plt.tight_layout(); plt.savefig('dashboards/revenue_by_product.png'); plt.close()
    # plot profit margin
    plt.figure(figsize=(10,6)); plt.bar(summary['product_id'], summary['profit_margin']); plt.title('Profit Margin by Product'); plt.xticks(rotation=45); plt.tight_layout(); plt.savefig('dashboards/profit_margin_by_product.png'); plt.close()
    # plot return rate vs revenue
    plt.figure(figsize=(8,6)); sizes = summary['units_sold']/summary['units_sold'].max()*200; plt.scatter(summary['return_rate'], summary['revenue'], s=sizes, alpha=0.6); 
    for _, r in summary.iterrows(): plt.text(r['return_rate'], r['revenue'], r['product_id'], fontsize=9)
    plt.title('Return Rate vs Total Revenue'); plt.xlabel('Return Rate'); plt.ylabel('Revenue'); plt.tight_layout(); plt.savefig('dashboards/return_rate_vs_revenue.png'); plt.close()
    # etc...
if __name__ == "__main__":
    plot_all()