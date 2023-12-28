from tkinter import *
from datetime import datetime
from Database.Models import Show
from Database.Commands import create_show


def insert_show():
    name = name_entry.get()
    rating = float(rating_entry.get())
    imdb = imdb_entry.get()
    last_episode = int(last_episode_entry.get())
    date_last_watched = date_last_watched_entry.get()
    snoozed = snoozed_var.get()

    show_instance = Show(
        name=name,
        rating=rating,
        imdb=imdb,
        last_episode=last_episode,
        date_last_watched=datetime.strptime(date_last_watched, '%Y-%m-%d'),
        snoozed=snoozed
    )

    create_show(show_instance)


root = Tk()
root.title("Insert a show Instance")

name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

rating_label = Label(root, text="Rating:")
rating_label.grid(row=1, column=0)
rating_entry = Entry(root)
rating_entry.grid(row=1, column=1)

imdb_label = Label(root, text="IMDB:")
imdb_label.grid(row=2, column=0)
imdb_entry = Entry(root)
imdb_entry.grid(row=2, column=1)

last_episode_label = Label(root, text="Last Episode:")
last_episode_label.grid(row=3, column=0)
last_episode_entry = Entry(root)
last_episode_entry.grid(row=3, column=1)

date_last_watched_label = Label(root, text="Date Last Watched (YYYY-MM-DD):")
date_last_watched_label.grid(row=4, column=0)
date_last_watched_entry = Entry(root)
date_last_watched_entry.grid(row=4, column=1)

snoozed_label = Label(root, text="Snoozed:")
snoozed_label.grid(row=5, column=0)
snoozed_var = BooleanVar()
snoozed_checkbox = Checkbutton(root, variable=snoozed_var)
snoozed_checkbox.grid(row=5, column=1)

submit_button = Button(root, text="Submit", command=insert_show)
submit_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
