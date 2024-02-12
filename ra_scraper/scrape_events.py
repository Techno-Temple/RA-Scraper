from scrape_tools import Scraper
from scrape_tools.constants import JSON_RESPONSE

from .constants import API_URL, POST_HEADERS
from .queries import EVENTS_QUERY


def scrape_events(
    scraper: Scraper,
    area_id: int,
    date_from: str,
    date_to: str,
    genres: str = None,
    nb_events: int = 10,
) -> None:
    scraper.scrape(
        cache_file_id=get_cache_file_id(area_id, date_from, date_to, genres),
        method="POST",
        url=API_URL,
        headers=POST_HEADERS,
        json=get_json_params(area_id, date_from, date_to, genres, nb_events),
        response_type=JSON_RESPONSE,
    )


def get_json_params(
    area_id: int,
    date_from: str,
    date_to: str,
    genres: str,
    nb_events: int,
) -> dict:
    return {
        "operationName": "GET_POPULAR_EVENTS",
        "variables": {
            "filters": {
                "areas": {"eq": area_id},
                "listingDate": {"gte": date_from, "lte": date_to},
                "listingPosition": {"eq": 1},
                "genre": {"any": genres},
            },
            "pageSize": nb_events,
        },
        "query": EVENTS_QUERY,
    }


def get_cache_file_id(
    area_id: int, date_from: str, date_to: str, genres: str
) -> str:
    if genres is not None:
        return f"events-{area_id}-{'_'.join(genres)}-{date_from}-{date_to}"
    else:
        return f"events-{area_id}-{None}-{date_from}-{date_to}"
