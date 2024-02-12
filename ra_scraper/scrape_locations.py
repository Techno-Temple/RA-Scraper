from scrape_tools import Scraper
from scrape_tools.constants import JSON_RESPONSE

from .constants import API_URL, POST_HEADERS
from .queries import LOCATIONS_QUERY

JSON_PARAMS = {
    "operationName": "GET_ALL_LOCATIONS_QUERY",
    "variables": {},
    "query": LOCATIONS_QUERY,
}


def scrape_locations(scraper: Scraper) -> None:
    scraper.scrape(
        cache_file_id="locations",
        method="POST",
        url=API_URL,
        headers=POST_HEADERS,
        json=JSON_PARAMS,
        response_type=JSON_RESPONSE,
    )
