-- Revert crypto_news:2_create_crypto_hot_news_table from mysql

BEGIN;

DROP TABLE IF EXISTS crypto_hot_news;

COMMIT;
