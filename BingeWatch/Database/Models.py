import logging

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()
logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def connect():
    try:
        connection_string = 'postgresql://postgres:postgres@localhost:5432/BingeWatch'
        engine = create_engine(connection_string)
        session = sessionmaker(bind=engine)
        db_session = session()
        return db_session, engine
    except OperationalError as e:
        logging.error(f"Failed to connect to the database: {str(e)}")


class Show(Base):
    __tablename__ = 'shows'
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
    __tablename__ = 'notifications'
    id_notif = Column(Integer, primary_key=True, autoincrement=True)
    id_show = Column(Integer, ForeignKey('shows.id_show'))
    id_video = Column(String, unique=True)
    episode = Column(Integer)
    season = Column(Integer)
    link = Column(String)
    date = Column(Date, nullable=False)


if __name__ == '__main__':
    logging.info("Creating new database...")
    session, engine = connect()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.close()
