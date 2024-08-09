import aiohttp
import asyncio
from bs4 import BeautifulSoup
from model.crypto_hot_news import get_crypto_coins_by_detail
from scrapper.common import insert_articles_hot_news


async def scrape_kompas(coin_terms):
    results = await scrape_hot_news_kompas()
    insert_articles_hot_news(coin_terms, results)
    return results


async def fetch_kompas(session, url):
    async with session.get(url) as response:
        return await response.text()


async def scrape_hot_news_kompas():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.kompas.com/'
        response = await fetch_kompas(session, url)
        soup = BeautifulSoup(response, 'html.parser')

        popular_news = soup.find('div', class_='mostWrap')
        if not popular_news:
            print("Kompas Could not find the popular news section.")
            return []

        articles = popular_news.find_all('div', class_=lambda x: x == 'mostItem')
        if not articles:
            print("Kompas Could not find articles in the popular news section.")
            return []

        articles.pop(0)
        articles.pop(0)
        articles.pop(5)
        return await asyncio.gather(
            *(scrape_news_detail_kompas(session, article.find('h2', class_='mostTitle').text.strip(),
                                       article.find('a')['href']) for article in articles)
        )


async def scrape_news_detail_kompas(session, title, url):
    is_exists = get_crypto_coins_by_detail(url)
    if is_exists:
        return {}

    response = await fetch_kompas(session, url)
    soup = BeautifulSoup(response, 'html.parser')

    detail_body = soup.find('div', class_='read__content')
    if not detail_body:
        print(f"Kompas Could not find the body content for {title}.")
        return {'title': title, 'url': url, 'body': '', 'channel': "kompas.com"}

    detail_body = detail_body.find('div', class_='clearfix')
    if not detail_body:
        print(f"Kompas Could not find the body content for {title}.")
        return {'title': title, 'url': url, 'body': '', 'channel': "kompas.com"}

    body_paragraphs = detail_body.find_all('p', recursive=False)
    body = '\n'.join([p.get_text(strip=True) for p in body_paragraphs])

    return {'title': title, 'url': url, 'body': body, 'channel': "kompas.com"}
