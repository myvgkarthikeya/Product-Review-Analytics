USE amazon_analytics;

CREATE TABLE amazon_reviews_clean AS
SELECT
    CAST(get_json_object(json_record, '$.rating') AS DOUBLE) AS rating,
    get_json_object(json_record, '$.asin') AS asin,
    get_json_object(json_record, '$.parent_asin') AS parent_asin,
    CAST(get_json_object(json_record, '$.timestamp') AS BIGINT) AS review_time,
    CAST(get_json_object(json_record, '$.helpful_vote') AS INT) AS helpful_vote,
    CAST(get_json_object(json_record, '$.verified_purchase') AS BOOLEAN) AS verified_purchase
FROM amazon_reviews_raw;
