import logging
from imdb import IMDb, IMDbError

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
ia = IMDb()


def extract_episode_info(imdb_url):
    """
    Extracts the episode info from an IMDb link.
    :param imdb_url: The IMDb link for an episode.
    :return: The episode number, season number, TV show name, and IMDb link of the show, not episodes.
    """
    logging.info(f"Extracting episode info from {imdb_url}")
    try:
        imdb_id = imdb_url.split("/")[-2][2:]
        tv_show = ia.get_movie(imdb_id)
        tv_show_name = tv_show.get("series title")
        season_number = tv_show.get("season")
        episode_number = tv_show.get("episode")
        series = ia.search_movie(tv_show_name)
        imdb_link = ""
        for result in series:
            if result["kind"] == "tv series":
                series_id = result.movieID
                imdb_link = f"https://www.imdb.com/title/tt{series_id}/"
                break
        logging.info(f"Extracted episode info: {tv_show_name} - {episode_number}")
        return episode_number, season_number, tv_show_name, imdb_link
    except IMDbError as e:
        logging.error(f"Error fetching TV show name: {e}")
        return None


def extract_show_seasons(imdb_link):
    """
    Extracts the number of seasons of a TV show.
    :param imdb_link: The IMDb link of the TV show.
    :return: The number of seasons of the TV show.
    """
    logging.info(f"Extracting show info from {imdb_link}")
    imdb_id = imdb_link.split("/")[-2][2:]
    try:
        movie = ia.get_movie(imdb_id)
        seasons = movie.get("seasons")
        return seasons
    except IMDbError as e:
        logging.error(f"Error fetching TV show name: {e}")
        return None


def extract_show_info(imdb_link):
    """
    Extracts the name and IMDb link of a TV show.
    :param imdb_link:
    :return: The title and IMDb link of the TV show.
    """
    logging.info(f"Extracting show info from {imdb_link}")
    imdb_id = imdb_link.split("/")[-2][2:]
    try:
        movie = ia.get_movie(imdb_id)
        title = movie.get("title")
        link = f"https://www.imdb.com/title/tt{imdb_id}/"
        return title, link
    except IMDbError as e:
        logging.error(f"Error fetching TV show name: {e}")
        return None


def check_link_type(imdb_link):
    """
    Checks the type of the IMDb link.
    :param imdb_link:
    :return:
    series - if the link is to a TV show,
    episode - if the link is to an episode,
    other - if the link is to something else.
    None - if the link does not exist.
    """
    logging.info(f"Checking link type for {imdb_link}")
    imdb_id = imdb_link.split("/")[-2][2:]
    try:
        result = ia.get_movie(imdb_id)
        if result:
            movie_type = result.get("kind")
            if movie_type == "tv series":
                return "series"
            elif movie_type == "episode":
                return "episode"
            else:
                return "other"
        else:
            logging.info(f"Link {imdb_link} does not exist")
            return None
    except IMDbError as e:
        logging.error("Error accessing IMDb data:", e)
        return None
