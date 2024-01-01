import logging
from sqlalchemy.exc import SQLAlchemyError
from Database.Models import connect, Show, Notification


logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def create_show(show):
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
    try:
        session, engine = connect()
        shows = session.query(Show).all()
        session.close()
        return shows
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_show_by_id(id_show):
    try:
        session, engine = connect()
        show = session.query(Show).filter(Show.id_show == id_show).first()
        session.close()
        return show
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def search_show_by_name(name):
    try:
        session, engine = connect()
        show = session.query(Show).filter(Show.name == name).first()
        session.close()
        return show
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_notifications():
    try:
        session, engine = connect()
        notifications = session.query(Notification).all()
        session.close()
        return notifications
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def select_notification_by_show_id(id_show):
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
    try:
        session, engine = connect()
        shows = session.query(Show).filter(Show.snoozed == True).all()
        return shows
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def list_new_episodes_per_show(id_show):
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
    try:
        session, engine = connect()
        session.query(Show).filter(Show.id_show == show.id_show).update(
            {
                Show.last_episode: show.last_episode,
                Show.episode_season: show.episode_season,
                Show.date_last_watched: show.date_last_watched,
                Show.snoozed: show.snoozed,
            }
        )
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def update_show_rating(show):
    try:
        session, engine = connect()
        session.query(Show).filter(Show.id_show == show.id_show).update(
            {Show.rating: show.rating}
        )
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def update_show_snoozed(show):
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
    try:
        session, engine = connect()
        session.query(Show).filter(Show.id_show == id_show).delete()
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")


def delete_notification(id_notif):
    try:
        session, engine = connect()
        session.query(Notification).filter(Notification.id_notif == id_notif).delete()
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        logging.error(f"An error occurred: {e}")

