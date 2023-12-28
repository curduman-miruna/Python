import logging
import tkinter as tk
from tkinter import messagebox

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def on_manage_shows():
    messagebox.showinfo("Manage Shows", "Placeholder: Manage Shows Logic")


def on_search_trailer_uploads():
    messagebox.showinfo("Search Trailer and Uploads", "Placeholder: Search Trailer and Uploads Logic")


def on_show_notifications():
    messagebox.showinfo("Show Notifications", "Placeholder: Show Notifications Logic")


def start_app():

    start_menu = tk.Tk()
    start_menu.geometry(f"{500}x{400}")
    start_menu.title("Show Management App")
    start_menu.iconbitmap('video-camera.ico')
    img = tk.PhotoImage(file="background-title.png")
    background_label = tk.Label(start_menu, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_menu.img = img

    btn_manage_shows = tk.Button(start_menu, text="Manage Shows", command=on_manage_shows, font=("Lato", 18), width=23)
    btn_manage_shows.pack(pady=(120, 10))

    btn_search_trailer_uploads = tk.Button(start_menu, text="Search Trailer and Uploads",
                                           command=on_search_trailer_uploads, font=("Lato", 18), width=23)
    btn_search_trailer_uploads.pack(pady=10)

    btn_show_notifications = tk.Button(start_menu, text="Show Notifications",
                                       command=on_show_notifications, font=("Lato", 18), width=23)
    btn_show_notifications.pack(pady=10)

    btn_exit = tk.Button(start_menu, text="Exit", command=start_menu.quit, font=("Lato", 18), width=20)
    btn_exit.pack(pady=10)

    try:
        logging.info("Starting the application.")
        start_menu.mainloop()
        logging.info("Application closed successfully.")
    except KeyboardInterrupt:
        start_menu.destroy()
        logging.error("Application closed by user.")
