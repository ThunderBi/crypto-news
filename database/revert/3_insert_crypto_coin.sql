-- Revert crypto_news:3_insert_crypto_coin from mysql

BEGIN;

DELETE FROM crypto_coin
WHERE crypto_key IN ('BTC', 'BNB', 'ETH', 'LUNA', 'DOGE', 'SOL');

COMMIT;
