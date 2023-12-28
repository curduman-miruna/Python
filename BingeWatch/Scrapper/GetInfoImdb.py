import logging

from imdb import IMDb, IMDbError

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
ia = IMDb()


def extract_episode_info(imdb_url):
    try:
        imdb_id = imdb_url.split('/')[-2][2:]
        tv_show = ia.get_movie(imdb_id)
        tv_show_name = tv_show.get('title')
        episode_number = int(imdb_url.split('_')[-1][2:])
        logging.info(f"Extracted episode info: {tv_show_name} - {episode_number}")
        return episode_number, tv_show_name
    except IMDbError as e:
        print(f"Error fetching TV show name: {e}")
        return None
