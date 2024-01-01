import tkinter as tk
from tkinter import messagebox, simpledialog
from Database.Commands import select_shows, delete_show

def delete_show():
    selected_index = listbox.curselection()
    if selected_index:
        idx = int(selected_index[0])
        confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {shows[idx].name}?")
        if not confirmation:
            return
        delete_show(idx)
        shows.pop(idx)

def edit_show():
    selected_index = listbox.curselection()
    if selected_index:
        idx = int(selected_index[0])
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Show Details")

        edit_frame = tk.Frame(edit_window, padx=20, pady=20)
        edit_frame.pack()

        selected_show = shows[idx]

        episode_label = tk.Label(edit_frame, text="Last Episode:")
        episode_label.grid(row=0, column=0)
        episode_entry = tk.Entry(edit_frame)
        episode_entry.insert(tk.END, selected_show.last_episode)
        episode_entry.grid(row=0, column=1)

        season_label = tk.Label(edit_frame, text="Episode Season:")
        season_label.grid(row=1, column=0)
        season_entry = tk.Entry(edit_frame)
        season_entry.insert(tk.END, selected_show.episode_season)
        season_entry.grid(row=1, column=1)

        date_label = tk.Label(edit_frame, text="Date Last Watched:")
        date_label.grid(row=2, column=0)
        date_entry = tk.Entry(edit_frame)
        date_entry.insert(tk.END, selected_show.date_last_watched)
        date_entry.grid(row=2, column=1)

        snoozed_label = tk.Label(edit_frame, text="Snoozed:")
        snoozed_label.grid(row=3, column=0)
        snoozed_entry = tk.Entry(edit_frame)
        snoozed_entry.insert(tk.END, selected_show.snoozed)
        snoozed_entry.grid(row=3, column=1)


def show_details():
    selected_index = listbox.curselection()
    if selected_index:
        idx = int(selected_index[0])
        selected_show = shows[idx]

        details_window = tk.Toplevel(root)
        details_window.title("Show Details")

        details_frame = tk.Frame(details_window, padx=20, pady=20)
        details_frame.pack()

        details = f"Name: {selected_show.name}\n" \
                  f"Rating: {selected_show.rating}\n" \
                  f"IMDB: {selected_show.imdb}\n" \
                  f"Last Episode: {selected_show.last_episode}\n" \
                  f"Episode Season: {selected_show.episode_season}\n" \
                  f"Date Last Watched: {selected_show.date_last_watched}\n" \
                  f"Snoozed: {selected_show.snoozed}"

        details_label = tk.Label(details_frame, text=details, justify=tk.LEFT)
        details_label.pack()
def display_shows():
    for show in shows:
        info = f"Name: {show.name} | Last seen: S.{show.episode_season} Ep.{show.last_episode}"
        listbox.insert(tk.END, info)


def populate_data():
    global shows
    shows = select_shows()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shows")
    root.geometry("500x400")

    shows = []
    populate_data()

    listbox = tk.Listbox(root, width=70, height=20)
    listbox.pack(padx=10, pady=10)

    display_shows()

    details_button = tk.Button(root, text="See Details", command=show_details)
    details_button.pack(side=tk.LEFT, padx=(30,10))

    delete_button = tk.Button(root, text="Delete", command=delete_show)
    delete_button.pack(side=tk.LEFT, padx=10)

    edit_button = tk.Button(root, text="Edit", command=edit_show)
    edit_button.pack(side=tk.LEFT, padx=10)



    root.mainloop()
