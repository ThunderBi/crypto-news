import pygame
from model.crypto_hot_news import insert_hot_news


pygame.mixer.init()


def insert_articles_hot_news(coin_terms, articles):
    for article in articles:
        title = article.get('title')
        url = article.get('url')
        body = article.get('body')
        channel = article.get('channel')

        if not title:
            continue

        content = f"{title} {body}".lower()
        if any(coin.lower() in content for coin in coin_terms):
            insert_hot_news(title, body, url, channel)
            sound = pygame.mixer.Sound('notification.wav')
            sound.play()
