CREATE EXTERNAL TABLE amazon_reviews_raw (
    json_record STRING
)
STORED AS TEXTFILE
LOCATION 'file:///home/bunny/Product-Review-Analytics/dataset/';
