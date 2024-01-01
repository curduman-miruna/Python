import logging
import requests
from bs4 import BeautifulSoup
from imdb import IMDb

from Scrapper.ImdbScrapper import extract_show_seasons

ia = IMDb()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/58.0.3029.110 Safari/537.3"
}
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_episodes_per_season(imdb_link):
    logging.info(f"Getting episodes per season for {imdb_link}")
    print(imdb_link)
    seasons = int(extract_show_seasons(imdb_link))+1
    episodes_per_season = {}
    for index in range(1, seasons):
        season_number = index
        link = f"https://www.imdb.com/title/{imdb_link.split('/')[-2]}/episodes?season={season_number}"
        number_episodes = get_episodes_of_season(link)
        episodes_per_season[season_number] = number_episodes
    return episodes_per_season


def get_episodes_of_season(imdb_link):
    response = requests.get(imdb_link, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        episode_section = soup.find("section", class_="sc-58f3e8aa-0 cLMIyf")
        if episode_section:
            episodes = episode_section.find_all(
                "article", class_="sc-282bae8e-1 dSEzwa episode-item-wrapper"
            )
            num_episodes = len(episodes)
            return num_episodes
        else:
            logging.error("Episodes section not found.")
    else:
        logging.error("Failed to fetch the page.")
