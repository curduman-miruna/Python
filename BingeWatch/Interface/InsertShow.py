from datetime import datetime
from Database.Models import Show
from Database.Commands import create_show
import tkinter as tk
from tkinter import messagebox


def insert_show(
    insert_form,
    name_entry,
    rating_entry,
    imdb_entry,
    last_episode_entry,
    date_last_watched_entry,
    snoozed_var,
):
    confirmation = messagebox.askyesno(
        "Confirmation", "Are you sure you want to insert this show?"
    )
    if not confirmation:
        insert_form.destroy()
    show_instance = Show(
        name=name_entry,
        rating=rating_entry,
        imdb=imdb_entry,
        last_episode=last_episode_entry,
        date_last_watched=datetime.strptime(date_last_watched_entry, "%Y-%m-%d"),
        snoozed=snoozed_var,
    )
    create_show(show_instance)


def open_insert_window():
    insert_form = tk.Tk()
    insert_form.geometry(f"{500}x{400}")
    insert_form.title("Show Management App")
    insert_form.iconbitmap("video-camera.ico")

    name_label = tk.Label(insert_form, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(insert_form)
    name_entry.grid(row=0, column=1)

    rating_label = tk.Label(insert_form, text="Rating:")
    rating_label.grid(row=1, column=0)
    rating_entry = tk.Entry(insert_form)
    rating_entry.grid(row=1, column=1)

    imdb_label = tk.Label(insert_form, text="IMDB:")
    imdb_label.grid(row=2, column=0)
    imdb_entry = tk.Entry(insert_form)
    imdb_entry.grid(row=2, column=1)

    last_episode_label = tk.Label(insert_form, text="Last Episode:")
    last_episode_label.grid(row=3, column=0)
    last_episode_entry = tk.Entry(insert_form)
    last_episode_entry.grid(row=3, column=1)

    date_last_watched_label = tk.Label(
        insert_form, text="Date Last Watched (YYYY-MM-DD):"
    )
    date_last_watched_label.grid(row=4, column=0)
    date_last_watched_entry = tk.Entry(insert_form)
    date_last_watched_entry.grid(row=4, column=1)

    snoozed_label = tk.Label(insert_form, text="Snoozed:")
    snoozed_label.grid(row=5, column=0)
    snoozed_var = tk.BooleanVar()
    snoozed_checkbox = tk.Checkbutton(insert_form, variable=snoozed_var)
    snoozed_checkbox.grid(row=5, column=1)

    submit_button = tk.Button(
        insert_form,
        text="Submit",
        command=lambda: insert_show(
            insert_form,
            name_entry.get(),
            rating_entry.get(),
            imdb_entry.get(),
            last_episode_entry.get(),
            date_last_watched_entry.get(),
            snoozed_var.get(),
        ),
    )
    submit_button.grid(row=6, column=0, columnspan=2)
    insert_form.mainloop()
