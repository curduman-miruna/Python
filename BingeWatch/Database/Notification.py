
class Notification:
    def __init__(self, id_show, id_video, episode, season, link, date):
        """
        Creates a new notification
        :param id_show: The ID of the associated show.
        :param id_video: The unique identifier for the video.
        :param episode: The episode number.
        :param season: The season number.
        :param link: The URL or link related to the notification.
        :param date: The date of the notification.
        """
        self.id_show = id_show
        self.episode = episode
        self.season = season
        self.id_video = id_video
        self.link = link
        self.date = date

    def __str__(self):
        """
        String representation of a notification
        :return:
        """
        return f"{self.id_show} {self.episode} {self.link} {self.date}"
