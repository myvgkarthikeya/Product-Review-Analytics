USE amazon_analytics;

-- 1. Total number of reviews
SELECT COUNT(*) AS total_reviews
FROM amazon_reviews_clean;


-- 2. Overall average rating
SELECT ROUND(AVG(rating), 2) AS average_rating
FROM amazon_reviews_clean;


-- 3. Rating distribution
SELECT
    rating,
    COUNT(*) AS review_count
FROM amazon_reviews_clean
GROUP BY rating
ORDER BY rating;


-- 4. Verified vs unverified purchases
SELECT
    verified_purchase,
    COUNT(*) AS review_count
FROM amazon_reviews_clean
GROUP BY verified_purchase
ORDER BY verified_purchase;


-- 5. Average rating by purchase status
SELECT
    verified_purchase,
    COUNT(*) AS review_count,
    ROUND(AVG(rating), 2) AS average_rating
FROM amazon_reviews_clean
GROUP BY verified_purchase
ORDER BY verified_purchase;


-- 6. Top 10 most-reviewed products
SELECT
    asin,
    COUNT(*) AS review_count,
    ROUND(AVG(rating), 2) AS average_rating
FROM amazon_reviews_clean
GROUP BY asin
ORDER BY review_count DESC
LIMIT 10;
