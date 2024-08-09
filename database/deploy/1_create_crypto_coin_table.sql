-- Deploy crypto_news:1_create_crypto_coin_table to mysql

BEGIN;

CREATE TABLE crypto_coin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    crypto_key VARCHAR(255) UNIQUE NOT NULL,
    detail VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
