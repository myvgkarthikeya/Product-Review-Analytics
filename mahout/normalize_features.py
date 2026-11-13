import pandas as pd
import numpy as np

input_file = "mahout/input/product_features.csv"
output_file = "mahout/input/product_features_normalized.csv"

feature_columns = [
    "average_rating",
    "total_reviews",
    "rating_1_pct",
    "rating_2_pct",
    "rating_3_pct",
    "rating_4_pct",
    "rating_5_pct"
]

# First pass: calculate global minimum and maximum
global_min = None
global_max = None

for chunk in pd.read_csv(input_file, chunksize=100000):
    features = chunk[feature_columns].copy()

    # Log transformation for review counts
    features["total_reviews"] = np.log1p(features["total_reviews"])

    chunk_min = features.min()
    chunk_max = features.max()

    if global_min is None:
        global_min = chunk_min
        global_max = chunk_max
    else:
        global_min = pd.concat([global_min, chunk_min], axis=1).min(axis=1)
        global_max = pd.concat([global_max, chunk_max], axis=1).max(axis=1)

# Avoid division by zero
feature_range = (global_max - global_min).replace(0, 1)

# Second pass: normalize and save
first_chunk = True
total_rows = 0

for chunk in pd.read_csv(input_file, chunksize=100000):
    features = chunk[feature_columns].copy()
    features["total_reviews"] = np.log1p(features["total_reviews"])

    chunk[feature_columns] = (features - global_min) / feature_range

    chunk.to_csv(
        output_file,
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    total_rows += len(chunk)
    first_chunk = False

print("Log transformation and normalization completed!")
print("Total products:", total_rows)
print("Output:", output_file)
