import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkcalendar import DateEntry
from Database.Commands import create_show
from Database.Models import Show
from Scrapper.ImdbScrapper import extract_episode_info


def insert_show_imdb(insert_imdb, imdb_link, rating, date_last_watched, snoozed_var):
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to insert this show?")
    if not confirmation:
        insert_imdb.destroy()
    episode_number, season_number, tv_show_name, imdb_show = extract_episode_info(imdb_link)
    show_instance = Show(
        name=tv_show_name,
        rating=rating,
        imdb=imdb_show,
        last_episode=episode_number,
        episode_season=season_number,
        date_last_watched=datetime.strptime(date_last_watched, '%Y-%m-%d'),
        snoozed=snoozed_var
    )
    create_show(show_instance)
    insert_imdb.destroy()


def open_insert_imdb_window():
    insert_imdb = tk.Tk()
    insert_imdb.geometry(f"{500}x{400}")
    insert_imdb.title("Show Management App")
    insert_imdb.iconbitmap('video-camera.ico')

    rating_label = tk.Label(insert_imdb, text="Rating:", font=("Lato", 18))
    rating_label.grid(row=1, column=0)
    rating_entry = tk.Entry(insert_imdb, font=("Lato", 18))
    rating_entry.grid(row=1, column=1)

    imdb_label = tk.Label(insert_imdb, text="IMDB LINK:", font=("Lato", 18))
    imdb_label.grid(row=2, column=0)
    imdb_entry = tk.Entry(insert_imdb, font=("Lato", 18))
    imdb_entry.grid(row=2, column=1)

    date_last_watched_label = tk.Label(insert_imdb, text="Date Last Watched (YYYY-MM-DD):", font=("Lato", 18))
    date_last_watched_label.grid(row=4, column=0)
    date_last_watched_entry = DateEntry(insert_imdb, date_pattern='yyyy-mm-dd', font=("Lato", 18))
    date_last_watched_entry.grid(row=4, column=1)

    snoozed_label = tk.Label(insert_imdb, text="Snoozed:", font=("Lato", 18))
    snoozed_label.grid(row=5, column=0)
    snoozed_var = tk.BooleanVar()
    snoozed_checkbox = tk.Checkbutton(insert_imdb, variable=snoozed_var, font=("Lato", 18))
    snoozed_checkbox.grid(row=5, column=1)

    submit_button = tk.Button(insert_imdb, text="Submit",
                              command=lambda: insert_show_imdb(
                                  insert_imdb,
                                  imdb_entry.get(),
                                  rating_entry.get(),
                                  date_last_watched_entry.get(),
                                  snoozed_var.get()
                                ), font=("Lato", 18))
    submit_button.grid(row=6, column=0, columnspan=2)
