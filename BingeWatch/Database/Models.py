import logging

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Date,
    Boolean,
    ForeignKey,
)
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def connect():
    """
    Connects to the database
    :return:
    """
    try:
        connection_string = "postgresql://postgres:postgres@localhost:5432/BingeWatch"
        engine = create_engine(connection_string)
        session = sessionmaker(bind=engine)
        db_session = session()
        return db_session, engine
    except OperationalError as e:
        logging.error(f"Failed to connect to the database: {str(e)}")


class Show(Base):
    """
    A class representing TV shows.

    This class defines the attributes related to TV shows, including the show's
    unique identifier, name, rating, IMDb ID, details about the last watched
    episode, date last watched, and whether the show is snoozed or not.

    Attributes:
        id_show (int): The unique identifier for the show.
        name (str): The name of the TV show (unique).
        rating (float): The rating of the TV show.
        imdb (str): The IMDb link of the TV show.
        last_episode (int): The number of the last watched episode.
        episode_season (int): The season number of the last watched episode.
        date_last_watched (Date): The date when the show was last watched.
        snoozed (bool): Indicates if the show is snoozed or not.

    Relationship:
        notifications (relationship): Relationship to the Notification class.
            It represents the notifications associated with this TV show.

    Table Name: shows
    """
    __tablename__ = "shows"
    id_show = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    rating = Column(Float)
    imdb = Column(String)
    last_episode = Column(Integer)
    episode_season = Column(Integer)
    date_last_watched = Column(Date)
    snoozed = Column(Boolean, default=False)
    notifications = relationship("Notification", backref="shows")


class Notification(Base):
    """A class representing notifications for shows.

    This class defines notifications related to TV shows. It stores information
    about each notification including its unique identifier, show ID, video ID,
    episode, season, link, and date.

    Attributes:
        id_notif (int): The unique identifier for the notification.
        id_show (int): The ID of the associated show.
        id_video (str): The unique identifier for the video.
        episode (int): The episode number.
        season (int): The season number.
        link (str): The URL or link related to the notification.
        date (Date): The date of the notification.

    Table Name: notifications
    """

    __tablename__ = "notifications"
    id_notif = Column(Integer, primary_key=True, autoincrement=True)
    id_show = Column(Integer, ForeignKey("shows.id_show"))
    id_video = Column(String, unique=True)
    episode = Column(Integer)
    season = Column(Integer)
    link = Column(String)
    date = Column(Date, nullable=False)


if __name__ == "__main__":
    """
    Creates the database
    """
    logging.info("Creating new database...")
    session, engine = connect()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.close()
