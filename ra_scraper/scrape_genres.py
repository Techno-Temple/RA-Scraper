from scrape_tools import Scraper
from scrape_tools.constants import JSON_RESPONSE

from .constants import API_URL, POST_HEADERS
from .queries import GENRES_QUERY

JSON_PARAMS = {
    "operationName": "GET_ALL_GENRES_QUERY",
    "variables": {},
    "query": GENRES_QUERY,
}


def scrape_genres(scraper: Scraper) -> None:
    scraper.scrape(
        cache_file_id="genres",
        method="POST",
        url=API_URL,
        headers=POST_HEADERS,
        json=JSON_PARAMS,
        response_type=JSON_RESPONSE,
    )
