-- Deploy crypto_news:3_insert_crypto_coin to mysql

BEGIN;

INSERT INTO crypto_coin (crypto_key, detail)
VALUES
    ('BTC', 'btc,bitcoin'),
    ('BNB', 'bnb,binance'),
    ('ETH', 'eth,ethereum'),
    ('LUNA', 'luna,terra'),
    ('DOGE', 'doge,dogecoin'),

COMMIT;
