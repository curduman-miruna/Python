import logging

from Database.Models import connect, Show, Notification


logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def create_show(show):
    session, engine = connect()
    new_show = Show(name=show.name, rating=show.rating, imdb=show.imdb, last_episode=show.last_episode,
                    date_last_watched=show.date_last_watched, snoozed=show.snoozed)
    session.add(new_show)
    session.commit()
    session.close()


def create_notification(notification):
    session, engine = connect()
    new_notification = Notification(id_show=notification.id_show, id_episode=notification.id_episode,
                                    episode=notification.episode, link=notification.link)
    session.add(new_notification)
    session.commit()
    session.close()


def select_shows():
    session, engine = connect()
    shows = session.query(Show).all()
    session.close()
    return shows


def select_show_by_id(id_show):
    session, engine = connect()
    show = session.query(Show).filter(Show.id_show == id_show).first()
    session.close()
    return show


def select_notifications():
    session, engine = connect()
    notifications = session.query(Notification).all()
    session.close()
    return notifications


def select_notification_by_show_id(id_show):
    session, engine = connect()
    notifications = session.query(Notification).filter(Notification.id_show == id_show).all()
    session.close()
    return notifications


def select_notification_by_video_id(id_video):
    session, engine = connect()
    notification = session.query(Notification).filter(Notification.id_video == id_video).first()
    session.close()
    return notification


def update_show(show):
    session, engine = connect()
    session.query(Show).filter(Show.id_show == show.id_show).update(
        {Show.last_episode: show.last_episode, Show.date_last_watched: show.date_last_watched,
         Show.snoozed: show.snoozed})
    session.commit()
    session.close()


def update_notification(notification):
    session, engine = connect()
    session.query(Notification).filter(Notification.id_notif == notification.id_notif).update(
        {Notification.link: notification.link})
    session.commit()
    session.close()
