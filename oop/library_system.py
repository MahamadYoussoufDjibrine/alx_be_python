class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


# ------------------ DERIVED CLASS: EBOOK ------------------
class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"E-Book: {self.title} by {self.author} - {self.file_size}MB (ISBN: {self.isbn}) - {status}"


# ------------------ DERIVED CLASS: PRINTBOOK ------------------
class PrintBook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.pages = pages

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"Print Book: {self.title} by {self.author} - {self.pages} pages (ISBN: {self.isbn}) - {status}"


# ------------------ LIBRARY CLASS ------------------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.check_out()
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.return_book()
        return False

    def list_available_books(self):
        return [str(book) for book in self.books if not book.is_checked_out]


# ---------- SAMPLE OUTPUT (FOR TESTING PURPOSES ONLY) ----------
if __name__ == "__main__":
    library = Library()

    b1 = PrintBook("Atomic Habits", "James Clear", "1111", 320)
    b2 = EBook("Python Basics", "Eric Matthes", "2222", 5)

    l
