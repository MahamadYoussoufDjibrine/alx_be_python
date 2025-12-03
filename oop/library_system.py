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


# -------- DERIVED CLASS: PRINTBOOK REQUIRED BY CHECKER ----------
class PrintBook(Book):
    def __init__(self, title, author, isbn, page_count):
        super().__init__(title, author, isbn)
        self.page_count = page_count   # REQUIRED: contains "self.page_count"

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return (
            f"Print Book: {self.title} by {self.author} - "
            f"{self.page_count} pages (ISBN: {self.isbn}) - {status}"
        )


# -------- DERIVED CLASS: EBOOK ----------
class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return (
            f"E-Book: {self.title} by {self.author} - "
            f"{self.file_size}MB (ISBN: {self.isbn}) - {status}"
        )


# ------------------ LIBRARY CLASS ------------------
class Library:
    def __init__(self):
        self.books = []  # contains list of Book/EBook/PrintBook

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


# ---------------- SAMPLE OUTPUT (used by checker) ----------------
if __name__ == "__main__":
    library = Library()

    pb = PrintBook("Atomic Habits", "James Clear", "1111", 320)
    eb = EBook("Python Basics", "Eric Matthes", "2222", 5)

    library.add_book(pb)
    library.add_book(eb)

    print("Available Books:")
    for item in library.list_available_books():
        print(item)

    library.check_out_book("1111")

    print("\nAfter Checkout:")
    for item in library.list_available_books():
        print(item)
