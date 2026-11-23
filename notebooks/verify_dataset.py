
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw/m5")

required_files = [
    "calendar.csv",
    "sales_train_validation.csv",
    "sales_train_evaluation.csv",
    "sell_prices.csv",
    "sample_submission.csv"
]

print("WALMART M5 DATASET VERIFICATION")
print("-" * 40)

for filename in required_files:
    file_path = DATA_DIR / filename

    if file_path.exists():
        size = file_path.stat().st_size / (1024 * 1024)
        print(f"FOUND: {filename} ({size:.2f} MB)")
    else:
        print(f"MISSING: {filename}")

print("\nLoading smaller datasets...")

calendar = pd.read_csv(DATA_DIR / "calendar.csv")
prices = pd.read_csv(DATA_DIR / "sell_prices.csv")

print("\nCALENDAR DATA")
print("Shape:", calendar.shape)
print(calendar.head())

print("\nSELL PRICES DATA")
print("Shape:", prices.shape)
print(prices.head())

print("\nVerification completed!")
