from argparse import Namespace
import os
import yaml

from scrape_tools import AuthProxy, Scraper, Cache

from ra_scraper import scrape_events, scrape_locations, scrape_genres

from .constants import (
    MAIN,
    CACHE,
    AREA_ID,
    GENRES,
    MAX_TRIES,
    DATE,
    DATE_FROM,
    DATE_TO,
    NB_EVENTS,
    MODE,
    EVENTS,
    LOCATIONS,
)


def launch(args: Namespace) -> None:
    configs = read_config_yaml(args.config_file)
    scraper = get_scraper(
        cache_dir=os.path.join(configs[MAIN][CACHE], configs[MAIN][DATE]),
        max_tries=configs[MAIN][MAX_TRIES],
    )

    for config_name in list(configs.keys())[1:]:
        config = configs[config_name]
        if config[MODE] == EVENTS:
            scrape_events(
                scraper=scraper,
                area_id=config[AREA_ID],
                date_from=config[DATE_FROM],
                date_to=config[DATE_TO],
                genres=config[GENRES],
                nb_events=config[NB_EVENTS],
            )
        elif config[MODE] == GENRES:
            scrape_genres(scraper)
        elif config[MODE] == LOCATIONS:
            scrape_locations(scraper)


def read_config_yaml(file_path: str) -> dict:
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def get_scraper(cache_dir: str, max_tries: int) -> Scraper:
    cache = Cache(cache_dir)
    proxy = AuthProxy(
        host=os.getenv("PROXY_ADDRESS"),
        port=os.getenv("PROXY_PORT"),
        name=os.getenv("PROXY_USERNAME"),
        password=os.getenv("PROXY_PASSWORD"),
    )
    return Scraper(cache=cache, proxy=proxy, max_tries=max_tries)
