import asyncio
import schedule
import time
from model.crypto_coin import get_crypto_coins
from scrapper.detik import scrape_detik
from scrapper.kompas import scrape_kompas


def job():
    print("Running job")
    asyncio.run(run_scrapper())


async def run_scrapper():
    crypto_coins = get_crypto_coins()
    crypto_terms = []
    for row in crypto_coins:
        detail_list = row['detail'].split(',')
        for detail in detail_list:
            crypto_terms.append(detail.strip())

    await asyncio.gather(
        scrape_detik(crypto_terms),
        scrape_kompas(crypto_terms)
    )


schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
