import logging
from sqlalchemy.exc import SQLAlchemyError
from Database.Models import connect, Show, Notification


def create_show(show):
    """
Creates a new show in the database
    :param show:
    :return:
    """
    logging.info(f"Creating show: {show.name}")
    print("Creating show")
    try:
        session, engine = connect()
        new_show = Show(
            name=show.name,
            rating=show.rating,
            imdb=show.imdb,
            last_episode=show.last_episode,
            episode_season=show.episode_season,
            date_last_watched=show.date_last_watched,
            snoozed=show.snoozed,
        )
        session.add(new_show)
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def create_notification(notification):
    """
    Creates a new notification in the database
    :param notification:
    :return:
    """
    logging.info(f"Creating notification: {notification.id_show}")
    try:
        session, engine = connect()
        new_notification = Notification(
            id_show=notification.id_show,
            id_video=notification.id_video,
            episode=notification.episode,
            season=notification.season,
            link=notification.link,
            date=notification.date,
        )
        session.add(new_notification)
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_shows():
    """
    Returns all shows in the database
    :return:
    """
    logging.info("Selecting all shows")
    try:
        session, engine = connect()
        shows = session.query(Show).all()
        session.close()
        return shows
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_show_by_id(id_show):
    """
    Returns the show with id == id_show
    :param id_show: unique identifier for the show
    :return:
    """
    logging.info(f"Selecting show with id: {id_show}")
    try:
        session, engine = connect()
        show = session.query(Show).filter(Show.id_show == id_show).first()
        session.close()
        return show
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def search_show_by_name(name):
    """
    Returns the show with the name == name (param)
    :param name: name of the show
    :return:
    """
    logging.info(f"Searching show with name: {name}")
    try:
        session, engine = connect()
        show = session.query(Show).filter(Show.name == name).first()
        session.close()
        return show
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_notifications():
    """
    Returns all notifications in the database
    :return:
    """
    logging.info("Selecting all notifications")
    try:
        session, engine = connect()
        notifications = session.query(Notification).all()
        session.close()
        return notifications
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_notification_by_show_id(id_show):
    """
    Returns all notifications with id_show == id_show (param)
    :param id_show: unique identifier for the show
    :return:
    """
    logging.info(f"Selecting notifications with show id: {id_show}")
    try:
        session, engine = connect()
        notifications = (
            session.query(Notification).filter(Notification.id_show == id_show).all()
        )
        session.close()
        return notifications
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_notification_new_episode():
    """
    Returns all notifications about episodes that are newer than the last watched episode
    :return:
    """
    logging.info("Selecting notifications about new episodes")
    session, engine = connect()
    shows = select_shows()
    shows_with_new_episodes = []
    for show in shows:
        if not show.snoozed:
            notifications = (
                session.query(Notification)
                .filter(Notification.episode > show.last_episode)
                .all()
            )
            if notifications:
                shows_with_new_episodes.append(notifications)
    return shows_with_new_episodes


def select_notification_by_video_id(id_video):
    """
    Returns the notification with id_video == id_video (param)
    :param id_video: unique identifier for the video
    :return:
    """
    logging.info(f"Selecting notification with video id: {id_video}")
    try:
        session, engine = connect()
        notification = (
            session.query(Notification)
            .filter(Notification.id_video == id_video)
            .first()
        )
        session.close()
        return notification
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_show_rating_none_unsnoozed_has_notification():
    """
    Returns all shows that have a notification and have no rating
    :return:
    """
    logging.info("Selecting shows with no rating and notifications")
    try:
        session, engine = connect()
        shows = (
            session.query(Show)
            .join(Show.notifications)
            .filter(Show.rating.is_(None))
            .filter(Show.snoozed == False)
            .all()
        )
        return shows
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def list_unsnoozed_shows_notifications():
    """
    Returns all shows that have a notification and are not snoozed
    :return:
    """
    logging.info("Selecting shows with notifications and are not snoozed")
    try:
        session, engine = connect()
        shows = (
            session.query(Show)
            .join(Show.notifications)
            .filter(Show.snoozed == False)
            .all()
        )
        return shows
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def list_snoozed_shows():
    """
    Returns all shows that are snoozed
    :return:
    """
    logging.info("Selecting shows that are snoozed")
    try:
        session, engine = connect()
        shows = session.query(Show).filter(Show.snoozed == True).all()
        return shows
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def list_new_episodes_per_show(id_show):
    """
    Returns all notifications of new episodes for a certain show
    :param id_show: unique identifier for the show
    :return:
    """
    logging.info(f"Selecting notifications for show with id: {id_show}")
    try:
        session, engine = connect()
        episodes = (
            session.query(Notification.episode, Notification.season)
            .join(Show, Notification.id_show == Show.id_show)
            .filter(Notification.id_show == id_show)
            .filter(Notification.episode > Show.last_episode)
            .filter(Notification.season >= Show.episode_season)
            .distinct()
            .all()
        )
        return episodes
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def update_show(show):
    """
    Updates the show with the same id as show (param)
    :param show: the show to be updated
    :return:
    """
    logging.info(f"Updating show: {show.name}")
    print(f"Updating show {show.id_show}")
    try:
        session, engine = connect()
        existing_show = session.query(Show).filter(Show.id_show == show.id_show).one_or_none()
        print(existing_show)
        if existing_show:
            existing_show.last_episode = show.last_episode
            existing_show.episode_season = show.episode_season
            existing_show.date_last_watched = show.date_last_watched
            existing_show.snoozed = show.snoozed

            session.commit()
            session.close()
            print("Show updated")
        else:
            logging.error(f"An error occurred: Show not found")
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def update_show_rating(show):
    """
    Updates the rating of the show with the same id as show (param)
    :param show: the show to be updated
    :return:
    """
    logging.info(f"Updating rating for show: {show.name}")
    try:
        session, engine = connect()
        session.query(Show).filter(Show.id_show == show.id_show).update(
            {Show.rating: show.rating}
        )
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def update_show_last_episode(show):
    """
    Updates the last watched episode of the show with the same id as show (param)
    :param show: the show to be updated
    :return:
    """
    logging.info(f"Updating last episode for show: {show.name}")
    try:
        session, engine = connect()
        session.query(Show).filter(Show.id_show == show.id_show).update(
            {
                Show.last_episode: show.last_episode,
                Show.episode_season: show.episode_season,
                Show.date_last_watched: show.date_last_watched,
            }
        )
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def update_show_snoozed(show):
    """
    Updates the snoozed status of the show with the same id as show (param)
    :param show: the show to be updated
    :return:
    """
    logging.info(f"Updating snooze status for show: {show.name}")
    try:
        session, engine = connect()
        session.query(Show).filter(Show.id_show == show.id_show).update(
            {Show.snoozed: not show.snoozed}
        )
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def update_notification(notification):
    """
    Updates the notification with the same id as notification (param)
    :param notification: the notification to be updated
    :return:
    """
    logging.info(f"Updating notification: {notification.id_notif}")
    try:
        session, engine = connect()
        session.query(Notification).filter(
            Notification.id_notif == notification.id_notif
        ).update(
            {
                Notification.episode: notification.episode,
                Notification.season: notification.season,
                Notification.link: notification.link,
            }
        )
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def delete_show(id_show):
    """
    Deletes the show with the same id as id_show (param) and the notifications as well
    :param id_show: identifier for the show
    :return:
    """
    logging.info(f"Deleting show with id: {id_show}")
    try:
        session, engine = connect()
        session.query(Notification).filter(Notification.id_show == id_show).delete()
        session.query(Show).filter(Show.id_show == id_show).delete()
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def delete_notification(id_notif):
    """
    Deletes the notification with the same id as id_notif (param)
    :param id_notif: identifier for the notification
    :return:
    """
    logging.info(f"Deleting notification with id: {id_notif}")
    try:
        session, engine = connect()
        session.query(Notification).filter(Notification.id_notif == id_notif).delete()
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")
