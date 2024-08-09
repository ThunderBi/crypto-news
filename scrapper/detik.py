import aiohttp
import asyncio
from bs4 import BeautifulSoup
from model.crypto_hot_news import get_crypto_coins_by_detail
from scrapper.common import insert_articles_hot_news


async def scrape_detik(coin_terms):
    results = await scrape_hot_news_detik()
    insert_articles_hot_news(coin_terms, results)
    return results


async def fetch_detik(session, url):
    async with session.get(url) as response:
        return await response.text()


async def scrape_hot_news_detik():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.detik.com/'
        response = await fetch_detik(session, url)
        soup = BeautifulSoup(response, 'html.parser')

        popular_news = soup.find('div', class_='cb-mostpop')
        if not popular_news:
            print("Detik Could not find the popular news section.")
            return []

        articles = popular_news.find_all('article', class_='list-content__item')
        if not articles:
            print("Detik Could not find articles in the popular news section.")
            return []

        return await asyncio.gather(
            *(scrape_news_detail_detik(session, article.find('a', class_='media__link').text.strip(),
                                       article.find('a', class_='media__link')['href']) for article in articles)
        )


async def scrape_news_detail_detik(session, title, url):
    is_exists = get_crypto_coins_by_detail(url)
    if is_exists:
        return {}

    response = await fetch_detik(session, url)
    soup = BeautifulSoup(response, 'html.parser')

    detail_body = soup.find('div', class_='detail__body-text itp_bodycontent')
    if not detail_body:
        print(f"Detik Could not find the body content for {title}.")
        return {'title': title, 'url': url, 'body': '', 'channel': "detik.com"}

    body_paragraphs = detail_body.find_all('p', recursive=False)
    body = '\n'.join([p.get_text(strip=True) for p in body_paragraphs])

    return {'title': title, 'url': url, 'body': body, 'channel': "detik.com"}
