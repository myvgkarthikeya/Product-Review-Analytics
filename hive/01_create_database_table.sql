CREATE DATABASE IF NOT EXISTS amazon_analytics;

USE amazon_analytics;

CREATE EXTERNAL TABLE amazon_reviews (
    rating DOUBLE,
    title STRING,
    text STRING,
    asin STRING,
    parent_asin STRING,
    user_id STRING,
    review_time BIGINT,
    helpful_vote INT,
    verified_purchase BOOLEAN
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' WITH SERDEPROPERTIES (
    "columns"="rating,title,text,asin,parent_asin,user_id,timestamp,helpful_vote,verified_purchase",
    "columns.types"="double,string,string,string,string,string,bigint,int,boolean"
)
STORED AS TEXTFILE
LOCATION 'file:///home/bunny/Product-Review-Analytics/dataset/';
