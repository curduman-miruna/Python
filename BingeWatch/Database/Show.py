class Show:
    def __init__(
        self,
        name,
        rating,
        imdb,
        last_episode,
        episode_season,
        date_last_watched,
        snoozed,
        id_show=None,
    ):
        """
        Creates a new show
        :param name: The name of the TV show (unique).
        :param rating: The rating of the TV show.
        :param imdb: The IMDb link of the TV show.
        :param last_episode: The number of the last watched episode.
        :param episode_season: The season number of the last watched episode.
        :param date_last_watched: The date when the show was last watched.
        :param snoozed: Indicates if the show is snoozed or not.
        :param id_show: The unique identifier for the show.
        """
        if id_show:
            self.id_show = id_show
        self.name = name
        self.rating = rating
        self.imdb = imdb
        self.last_episode = last_episode
        self.episode_season = episode_season
        self.date_last_watched = date_last_watched
        self.snoozed = snoozed

    def __str__(self):
        """
        String representation of a show
        :return:
        """
        return f"{self.name} {self.rating} {self.imdb} {self.last_episode} {self.episode_season} {self.date_last_watched} {self.snoozed}"
