# Project Overview

## Problem
E-commerce platforms receive large volumes of customer reviews. This project uses big-data tools to calculate aggregate review statistics and identify groups of products with similar rating patterns.

## Objectives
1. Process a large text-based review dataset.
2. Calculate review totals, average ratings and rating distributions.
3. Identify the most frequently reviewed products.
4. Compare descriptive statistics for verified and non-verified purchases.
5. Generate normalized product-level features.
6. Apply K-Means clustering to group products by review characteristics.

## Processing pipeline
Parquet source data is converted to JSONL. Hive is used for cleaning and aggregate analytics. Python/Pandas aggregates review data by ASIN and generates average rating, review count, and rating-share features. Features are normalized and converted to Mahout-compatible SequenceFiles. Mahout K-Means then groups the product vectors.

## Interpretation
The project describes review-derived patterns. It does not establish why a product received a rating or predict future sales.
