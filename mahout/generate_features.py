import pandas as pd
import numpy as np
import json
from collections import defaultdict

# Input and output paths
input_file = "dataset/amazon_reviews_1gb.jsonl"
output_file = "mahout/input/product_features.csv"

# Process JSONL in chunks
chunk_size = 100000

# Store product-level statistics
product_stats = defaultdict(lambda: {
    "total_reviews": 0,
    "rating_sum": 0,
    "rating_counts": {i: 0 for i in range(1, 6)}
})

print("Starting product feature generation...")

for chunk in pd.read_json(input_file, lines=True, chunksize=chunk_size):

    chunk = chunk[["asin", "rating"]].dropna()

    for asin, rating in zip(chunk["asin"], chunk["rating"]):

        try:
            rating = float(rating)

            if rating < 1 or rating > 5:
                continue

            stats = product_stats[asin]

            stats["total_reviews"] += 1
            stats["rating_sum"] += rating

            if rating.is_integer():
                stats["rating_counts"][int(rating)] += 1

        except (ValueError, TypeError):
            continue

print("Calculating product-level features...")

rows = []

for asin, stats in product_stats.items():

    total = stats["total_reviews"]

    if total == 0:
        continue

    average_rating = stats["rating_sum"] / total

    rows.append({
        "asin": asin,
        "average_rating": average_rating,
        "total_reviews": total,
        "rating_1_pct": stats["rating_counts"][1] / total * 100,
        "rating_2_pct": stats["rating_counts"][2] / total * 100,
        "rating_3_pct": stats["rating_counts"][3] / total * 100,
        "rating_4_pct": stats["rating_counts"][4] / total * 100,
        "rating_5_pct": stats["rating_counts"][5] / total * 100
    })

features = pd.DataFrame(rows)

features.to_csv(output_file, index=False)

print("\nFeature generation completed!")
print("Total products:", len(features))
print("Output file:", output_file)
print("\nSample records:")
print(features.head())
