import os
from typing import List, Dict, Any

import requests

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")


def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """

    results = []

    page = 0
    while True:
        page += 1
        response = requests.get(
            url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
            params={'date': date, 'page': page},
            headers={'Authorization': AUTH_TOKEN},
        )
        if response.status_code == 200:
            results.append(response.json())
        else:
            break

    return results
