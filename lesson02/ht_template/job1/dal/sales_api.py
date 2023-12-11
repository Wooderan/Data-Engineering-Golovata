import requests
import asyncio
import aiohttp
from aiohttp import ClientSession
from typing import List, Dict, Any
from ht_template.job1.settings import AUTH_TOKEN

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'


async def fetch_page_data(session: ClientSession, url, date: str, page: int):
    print(f"Page {page} started")
    response = await session.get(
        url=url,
        params={'date': date, 'page': page},
        headers={'Authorization': '2b8d97ce57d401abd89f45b0079d8790edd940e6'}
    )
    data = await response.json()
    print(f"Page {page} done")
    return data


async def get_sales_from_fake_server(date: str):
    url = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in range(1, 5):
            tasks.append(fetch_page_data(session, url, date, page))
        results = await asyncio.gather(*tasks)
        return results[0]


def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """
    res = asyncio.run(get_sales_from_fake_server(date))
    return res