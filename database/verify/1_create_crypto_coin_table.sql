-- Verify crypto_news:1_create_crypto_coin_table on mysql

BEGIN;

SELECT 1 FROM crypto_coin LIMIT 1;

ROLLBACK;
