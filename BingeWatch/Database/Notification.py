
class Notification:
    def __init__(self, id_show, id_video, episode, season, link, date):
        self.id_show = id_show
        self.episode = episode
        self.season = season
        self.id_video = id_video
        self.link = link
        self.date = date

    def __str__(self):
        return f"{self.id_show} {self.episode} {self.link} {self.date}"
