# Machine Learning: K-Means Clustering

## Implemented method
Apache Mahout 0.13.0 K-Means is used to group products by review-derived numerical features. This is unsupervised learning; there are no target labels.

## Features
1. Average rating
2. Normalized total review count (log1p followed by min-max scaling)
3. Percentage of 1-star reviews
4. Percentage of 2-star reviews
5. Percentage of 3-star reviews
6. Percentage of 4-star reviews
7. Percentage of 5-star reviews

## Configuration
- `k = 3`
- Maximum iterations: `20`
- Convergence delta: `0.001`

Cluster IDs are arbitrary. Interpret centroids using the seven features. Use final `clusteredPoints` assignments for exact cluster sizes; do not treat a centroid's `n` field as the verified assignment count.

No supervised classification or regression model is claimed. The implemented ML component is product clustering.
