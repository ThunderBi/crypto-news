-- Verify crypto_news:2_create_crypto_hot_news_table on mysql

BEGIN;

SELECT 1 FROM crypto_hot_news LIMIT 1;

ROLLBACK;
