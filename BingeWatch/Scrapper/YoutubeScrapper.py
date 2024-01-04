import logging
from datetime import datetime

from youtubesearchpython import VideosSearch
from Database.Commands import select_show_by_id, create_notification, select_notification_by_video_id, select_shows
from Database.Notification import Notification
from Scrapper.BS4Scrapper import get_episodes_per_season


def add_notification_all_shows():
    """
    Adds notifications for all shows.
    :return:
    """
    logging.info("Searching for new episodes for all shows")
    shows = select_shows()
    for show in shows:
        add_notification_new_episodes(show.id_show)


def add_notification_new_episodes(id_show):
    """
    Adds notifications for new episodes of a show.
    :param id_show: The unique identifier of the show.
    :return:
    """
    show = select_show_by_id(id_show)
    show_name = show.name
    logging.info(f"Searching for new episodes for {show_name}")
    episodes_per_season = get_episodes_per_season(show.imdb)
    season = show.episode_season if show.episode_season != 0 else 1
    episode = show.last_episode + 1 if show.last_episode != 0 else 1
    for season_index in range(season, len(episodes_per_season) + 1):
        for episode_index in range(episode, episodes_per_season[season_index] + 1):
            search = (
                f"{show_name} episode {episode_index} season {season_index} trailer"
            )
            videos_search = VideosSearch(search, limit=3)
            result = videos_search.result()

            if result["result"]:
                for i in result["result"]:
                    new_notification = Notification(
                        show.id_show,
                        i["id"],
                        episode_index,
                        season_index,
                        i["link"],
                        datetime.now().strftime("%Y-%m-%d"),
                    )
                    print("Added new notification")
                    if select_notification_by_video_id(i["id"]):
                        logging.info("Notification already exists")
                    else:
                        create_notification(new_notification)
                logging.info(
                    f"New trailers found for {season_index} x {episode_index} of {show_name}"
                )
            else:
                logging.info(
                    f"No new trailers found for {season_index} x {episode_index} of {show_name}"
                )

        episode = 1
