import logging
from datetime import datetime
from Database.Models import Show
from Scrapper.ImdbScrapper import (
    extract_episode_info,
    extract_show_info,
    check_link_type,
)
from colorama import Fore, Style

from Database.Commands import (
    create_show,
    search_show_by_name,
    delete_show,
    update_show_rating,
    update_show_snoozed,
    select_show_rating_none_unsnoozed_has_notification,
    list_unsnoozed_shows_notifications,
    list_new_episodes_per_show,
    list_snoozed_shows, update_show_last_episode, select_shows,
)
from Scrapper.YoutubeScrapper import (
    add_notification_all_shows,
)


logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def initialize():
    """
    Initializes the program
    :return:
    """
    logging.info("Initializing program")
    shows = select_show_rating_none_unsnoozed_has_notification()
    if shows:
        for show in shows:
            print(f"{Fore.RED}{show.name} has new episodes!{Style.RESET_ALL}")
    else:
        print("No new episodes found")


def command_add_notifications():
    """
    Adds notifications for all shows.
    :return:
    """
    print("Searching new episodes for all shows. This may take a while...")
    add_notification_all_shows()


def command_add_show(command_text):
    """
    Adds a new show to the database
    :param command_text: the input command containing the imdb link and rating
    :return: True if the show was added successfully, False otherwise
    """
    parts = command_text.split()
    if len(parts) > 3:
        if not parts[3]:
            score = None
        else:
            try:
                score = float(parts[3])
                print(score)
            except ValueError:
                logging.error(f"Invalid IMDb score: {parts[3]}")
                score = None
    else:
        score = None
        logging.error("Index out of bounds: parts[3] doesn't exist")

    imdb_link = parts[2]
    link_type = check_link_type(imdb_link)
    date_last_watched = datetime.now().strftime("%Y-%m-%d")

    if link_type == "episode":
        episode_number, season_number, tv_show_name, imdb = extract_episode_info(
            imdb_link
        )
        new_show = Show(
            name=tv_show_name,
            rating=score,
            imdb=imdb,
            last_episode=episode_number,
            episode_season=season_number,
            date_last_watched=date_last_watched,
            snoozed=False,
        )
        create_show(new_show)
        return True

    elif link_type == "series":
        imd_title, link = extract_show_info(imdb_link)
        new_show = Show(
            name=imd_title,
            rating=score,
            imdb=link,
            last_episode=0,
            episode_season=0,
            date_last_watched=date_last_watched,
            snoozed=False,
        )
        create_show(new_show)
        return True

    else:
        print("Invalid command. Please make sure is a link to a show and try again.")
        return False


def command_delete_show():
    """
    Deletes a show from the database
    :return: True if the show was deleted successfully, False otherwise
    """
    show = input("Enter the name of the show you want to delete: ")
    show_info = search_show_by_name(show)
    if show_info:
        confirmation = input(
            f"{Fore.RED}Are you sure you want to delete {show_info.name}? (y/n): {Style.RESET_ALL}"
        )
        if confirmation.lower() == "y":
            delete_show(show_info.id_show)
            print(f"{show_info.name} deleted successfully!")
            return True
        else:
            print("Delete cancelled")
            return True
    else:
        print(f"Show {show} does not exist. Try again.")
        return False


def command_snooze_show():
    """
    Snoozes/unsnoozes a show
    :return: True if the show was snoozed/unsnoozed successfully, False otherwise
    """
    snoozed_shows = list_snoozed_shows()
    if not snoozed_shows:
        print(f"{Fore.YELLOW}You don't have any snoozed shows{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTBLUE_EX}Snoozed shows:{Style.RESET_ALL}")
        for show in snoozed_shows:
            print(f"{show.name}")
    show = input("Enter the name of the show you want to snooze/unsnooze: ")
    show_info = search_show_by_name(show)
    if show_info:
        print(f"Snooze status: {show_info.snoozed}")
        confirmation = input(
            f"{Fore.RED}Are you sure you want to snooze/unsnooze {show_info.name}? (y/n): {Style.RESET_ALL}"
        )
        if confirmation.lower() == "y":
            update_show_snoozed(show_info)
            print(f"{show_info.name} snoozed/unsnoozed successfully!")
        else:
            print("Snooze cancelled")


def command_update_rating():
    """
    Updates the rating of a show
    :return:
    """
    show = input("Enter the name of the show you want to update: ")
    show_info = search_show_by_name(show)
    if show_info:
        print(f"Current rating: {show_info.rating}")
        new_rating = input(f"Enter new rating: ")
        new_rating = float(new_rating)
        confirmation = input(
            f"Are you sure you want to update {show_info.name}? (y/n): "
        )
        if confirmation.lower() == "y":
            show_info.rating = new_rating
            update_show_rating(show_info)
            print(f"{show_info.name} updated successfully!")
        else:
            print("Update cancelled")


def command_update_last_episode():
    """
    Updates the last watched episode of a show
    :return:
    """
    show = input("Enter the name of the show you want to update: ")
    show_info = search_show_by_name(show)
    if show_info:
        print(f"Current episode: {show_info.last_episode} SEASON: {show_info.episode_season}")
        new_episode = input(f"Enter new episode: ")
        new_season = input(f"Enter new season: ")
        show_info.last_episode = int(new_episode)
        show_info.episode_season = int(new_season)
        confirmation = input(
            f"Are you sure you want to update {show_info.name}? (y/n): "
        )
        if confirmation.lower() == "y":
            show_info.last_episode = new_episode
            update_show_last_episode(show_info)
            print(f"{show_info.name} updated successfully!")
        else:
            print("Update cancelled")


def command_list_shows():
    """
    Lists all shows
    :return:
    """
    shows = list_unsnoozed_shows_notifications()
    for show in shows:
        print(f"{show.name} has new episodes!")
        episodes = list_new_episodes_per_show(show.id_show)
        for episode in episodes:
            print(f"Season {episode.season} Episode {episode.episode}")


def command_list_all_shows():
    """
    Lists all shows
    :return:
    """
    shows = select_shows()
    for show in shows:
        print(f"{show.name} has the rating {show.rating}. "
              f"Last episode was {show.last_episode}, season {show.episode_season} on {show.date_last_watched}. "
              f"Snooze status: {show.snoozed}")


if __name__ == "__main__":
    """
    Main function
    """
    try:
        running = True
        initialize()
        while running:
            command = input(
                "Enter a command (or 'exit' to quit, 'help' to list commands): "
            )
            logging.info(f"Command entered: {command}")
            if command.lower() == "exit":
                running = False

            elif command.lower().startswith("adaugare serial"):
                response = command_add_show(command)

            elif command.lower().startswith("stergere serial"):
                response = command_delete_show()

            elif command.lower().startswith("modificare scor"):
                command_update_rating()

            elif command.lower().startswith("snooze/unsnooze"):
                command_snooze_show()

            elif command.lower().startswith("listare"):
                command_list_shows()

            elif command.lower().startswith("adaugare notificari"):
                command_add_notifications()

            elif command.lower().startswith("update last episode"):
                command_update_last_episode()

            elif command.lower().startswith("vizualizare seriale"):
                command_list_all_shows()

            elif command.lower() == "help":
                print(f"{Fore.BLUE}The commands are:{Style.RESET_ALL}")
                print(f"{Fore.GREEN}  adaugare serial{Style.RESET_ALL}")
                print(f"{Fore.GREEN}  stergere serial")
                print(f"{Fore.GREEN}  modificare scor")
                print(f"{Fore.GREEN}  snooze/unsnooze - modifica statusul snooze al unui serial")
                print(f"{Fore.GREEN}  listare - lista seriale cu episoade noi")
                print(f"{Fore.GREEN}  adaugare notificari - cauta noi episoade pentru toate serialele")
                print(f"{Fore.GREEN}  update last episode - modificare ultimul episod vazut")
                print(f"{Fore.GREEN}  vizualizare seriale - o lista detalii seriale")
                print(f"{Fore.GREEN}  exit{Style.RESET_ALL}")

        print("Goodbye!")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        logging.info("Keyboard interrupt")
