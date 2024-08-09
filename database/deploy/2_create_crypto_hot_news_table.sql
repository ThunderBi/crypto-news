-- Deploy crypto_news:2_create_crypto_hot_news_table to mysql

BEGIN;

CREATE TABLE crypto_hot_news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url TEXT NOT NULL UNIQUE,
    body TEXT NOT NULL,
    channel VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
