# Product Review Analytics using Hadoop, Hive and Apache Mahout

A big-data analytics project that processes Amazon Books review data to calculate review statistics, identify frequently reviewed products, examine rating patterns, and group products using K-Means clustering.

## Highlights
- Dataset: Amazon Reviews 2023 – Books Review (`cogsci13/Amazon-Reviews-2023-Books-Review`)
- Reviews analyzed: **3,572,784**
- Product feature records: **1,244,476**
- Overall average rating: **4.41 / 5**
- Hive analytics: rating distribution, verified-purchase comparison, top-reviewed products
- Mahout K-Means: 3 clusters, up to 20 iterations, convergence delta 0.001

## Stack
Apache Hadoop 3.3.6 · Apache Hive 3.1.3 · Apache Mahout 0.13.0 · Python/Pandas · Java · HDFS · SequenceFile

## Architecture
```text
Amazon review Parquet files
          |
     JSONL conversion
          |
    +-----+----------------------+
    |                            |
 Apache Hive                Python/Pandas
    |                    product aggregation
    |                            |
    |                       normalization
    |                            |
    |                     SequenceFile vectors
    |                            |
    |                      Mahout K-Means
    |                            |
    +---------- Analytics -------+
```

## Results

### Rating distribution
| Rating | Reviews |
|---:|---:|
| 0.0 | 4 |
| 1.0 | 130,760 |
| 2.0 | 133,700 |
| 3.0 | 286,559 |
| 4.0 | 598,837 |
| 5.0 | 2,422,924 |

### Verified purchase comparison
| Verified | Reviews | Average rating |
|---|---:|---:|
| false | 932,350 | 4.19 |
| true | 2,640,434 | 4.49 |

This is a descriptive association, not evidence of causation.

### Top-reviewed products
| ASIN | Reviews | Average |
|---|---:|---:|
| B06Y1264PX | 4,789 | 4.46 |
| 0679805273 | 4,534 | 4.85 |
| 1780671067 | 4,198 | 4.65 |
| 0920668372 | 3,887 | 4.66 |
| B00L9B7IKE | 3,628 | 4.09 |
| B006LSZECO | 2,781 | 3.96 |
| 0803736800 | 2,641 | 4.33 |
| 1442450703 | 2,369 | 4.75 |
| 1338099132 | 2,206 | 3.83 |
| B00JO8PEN2 | 2,055 | 4.79 |

## Workflow
1. Download the source dataset and convert Parquet files to JSONL.
2. Load and clean review records with Hive.
3. Run aggregate Hive queries.
4. Aggregate product-level features with Python/Pandas.
5. Normalize numerical features.
6. Convert rows into Hadoop SequenceFile records (`Text` keys and Mahout `VectorWritable` values).
7. Run Mahout K-Means with `k=3`.
8. Inspect centroids and count final assignments.

## Repository layout
```text
Product-Review-Analytics/
├── dataset/       # Raw data is not committed
├── docs/          # Project documentation
├── hive/          # Hive SQL scripts
├── mahout/        # Feature engineering, conversion, clustering
├── mapreduce/     # MapReduce source/scripts
├── ml_models/     # Clustering methodology and interpretation
├── results/       # Small summaries/plots only
└── screenshots/   # Selected evidence
```

## Environment and execution notes
Developed on Ubuntu with Hadoop 3.3.6, Hive 3.1.3 and Mahout 0.13.0. Java 11 was used for Hadoop/Mahout; Java 8 was used for the Hive 3.1.3 local-mode setup.

**Execution clarification:** Mahout used Hadoop's `LocalJobRunner` in this environment. The full run processed 1,244,476 product vectors, but this was not a multi-node YARN cluster. Hive was also run in local mode.

## Scope and limitations
- The fields used from this Books Reviews dataset do not provide a reliable category attribute, so category-wise analytics are not claimed.
- K-Means is unsupervised clustering, not supervised prediction.
- Cluster IDs are arbitrary. Interpret them using centroid feature values and actual final assignment counts.
- Add the verified full-run cluster counts and centroid interpretation after final output inspection.

## Dataset
Source: `cogsci13/Amazon-Reviews-2023-Books-Review` on Hugging Face. The raw dataset and generated large files are intentionally excluded from Git. Check source licensing/terms before redistribution.

GitHub: [@myvgkarthikeya](https://github.com/myvgkarthikeya)
