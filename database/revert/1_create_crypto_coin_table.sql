-- Revert crypto_news:1_create_crypto_coin_table from mysql

BEGIN;

DROP TABLE IF EXISTS crypto_coin;

COMMIT;
