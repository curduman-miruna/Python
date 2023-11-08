class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def display_info(self):
        status = "Checked out" if self.checked_out else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}")

    def check_out(self, user):
        self.checked_out = True
        print(f"{self.title} checked out by {user}")

    def return_item(self):
        self.checked_out = False
        print(f"{self.title} returned")

class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}, Duration: {self.duration} minutes")

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, year):
        super().__init__(title, "", year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")



book1 = Book("Fundamentele algebrice ale informaticii", "Ferucio Laurențiu Țiplea", 2021, "Ştiinţe exacte / Informatică")
dvd1 = DVD("Inception", "Christopher Nolan", 2010, 148)
magazine1 = Magazine("National Geographic", 123, 2023)

book1.check_out("Ana")
dvd1.check_out("Marian")
magazine1.display_info()
book1.return_item()
book1.display_info()
