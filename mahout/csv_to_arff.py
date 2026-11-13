import pandas as pd

input_file = "mahout/arff/sample.csv"
output_file = "mahout/arff/product_sample.arff"

df = pd.read_csv(input_file)

# Exclude ASIN because it is an identifier, not a clustering feature
feature_columns = [
    "average_rating",
    "total_reviews",
    "rating_1_pct",
    "rating_2_pct",
    "rating_3_pct",
    "rating_4_pct",
    "rating_5_pct"
]

with open(output_file, "w") as file:

    file.write("@RELATION product_reviews\n\n")

    for column in feature_columns:
        file.write(f"@ATTRIBUTE {column} NUMERIC\n")

    file.write("\n@DATA\n")

    for row in df[feature_columns].itertuples(index=False, name=None):
        file.write(",".join(map(str, row)) + "\n")

print("ARFF conversion completed!")
print("Product records:", len(df))
print("Features:", len(feature_columns))
print("Output:", output_file)
