import logging
from datetime import datetime
from Database.Models import Show
from Scrapper.ImdbScrapper import (
    extract_episode_info,
    extract_show_info,
    check_link_type,
)
from colorama import Fore, Back, Style, init

from Database.Commands import (
    create_show,
    search_show_by_name,
    delete_show,
    update_show_rating,
    update_show_snoozed, select_show_rating_none_unsnoozed_has_notification, list_unsnoozed_shows_notifications,
    list_new_episodes_per_show, select_shows, list_snoozed_shows,
)
from Scrapper.YoutubeScrapper import add_notification_new_episodes, add_notification_all_shows


def initialize():

    shows = select_show_rating_none_unsnoozed_has_notification()
    if shows:
        for show in shows:
            print(f"{Fore.RED}{show.name} has new episodes!{Style.RESET_ALL}")
    else:
        print("No new episodes found")


def command_add_notifications():
    print("Searching new episodes for all shows. This may take a while...")
    add_notification_all_shows()


def command_add_show(command_text):
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
            return True
        else:
            print("Snooze cancelled")
            return True


def command_update_rating():
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
            return True
        else:
            print("Update cancelled")
            return True


def command_list_shows():
    shows = list_unsnoozed_shows_notifications()
    for show in shows:
        print(f"{show.name} has new episodes!")
        episodes = list_new_episodes_per_show(show.id_show)
        for episode in episodes:
            print(f"Season {episode.season} Episode {episode.episode}")
    return True


if __name__ == "__main__":
    try:
        running = True
        initialize()
        while running:
            command = input("Enter a command (or 'exit' to quit, 'help' to list commands): ")
            if command.lower() == "exit":
                running = False

            elif command.lower().startswith("adaugare serial"):
                response = command_add_show(command)

            elif command.lower().startswith("stergere serial"):
                response = command_delete_show()

            elif command.lower().startswith("modificare scor"):
                response = command_update_rating()

            elif command.lower().startswith("snooze/unsnooze"):
                response = command_snooze_show()

            elif command.lower().startswith("listare"):
                response = command_list_shows()

            elif command.lower().startswith("adaugare notificari"):
                response = command_add_notifications()

            elif command.lower() == "help":
                print(f"{Fore.BLUE}The commands are:{Style.RESET_ALL}")
                print(f"{Fore.GREEN}  adaugare serial{Style.RESET_ALL}")
                print(f"{Fore.GREEN}  stergere serial")
                print(f"{Fore.GREEN}  modificare scor")
                print(f"{Fore.GREEN}  snooze/unsnooze")
                print(f"{Fore.GREEN}  listare")
                print(f"{Fore.GREEN}  adaugare notificari")
                print(f"{Fore.GREEN}  exit{Style.RESET_ALL}")

        print("Goodbye!")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        logging.info("Keyboard interrupt")
