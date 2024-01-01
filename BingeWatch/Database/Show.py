
class Show:
    def __init__(self, name, rating, imdb, last_episode, episode_season, date_last_watched, snoozed):
        self.name = name
        self.rating = rating
        self.imdb = imdb
        self.last_episode = last_episode
        self.episode_season = episode_season
        self.date_last_watched = date_last_watched
        self.snoozed = snoozed

    def __str__(self):
        return f"{self.name} {self.rating} {self.imdb} {self.last_episode} {self.episode_season} {self.date_last_watched} {self.snoozed}"
