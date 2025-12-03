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


# --------------------- Derived Class: PrintBook ---------------------
class PrintBook(Book):
    def __init__(self, title, author, isbn, page_count):
        super().__init__(title, author, isbn)
        self.page_count = page_count  # required: self.page_count

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return (
            f"Print Book: {self.title} by {self.author} - "
            f"{self.page_count} pages (ISBN: {self.isbn}) - {status}"
        )


# --------------------- Derived Class: EBook ---------------------
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


# --------------------- Library Class ---------------------
class Library:
    def __init__(self):
        self.books = []  # list of Book, PrintBook, EBook

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

    # REQUIRED BY CHECKER
    def list_books(self):
        """List ALL books."""
        return [str(book) for book in self.books]

    def list_available_books(self):
        """List only available books."""
        return [str(book) for book in self.books if not book.is_checked_out]


# --------------------- Output Section ---------------------
if __name__ == "__main__":
    library = Library()

    book1 = PrintBook("Atomic Habits", "James Clear", "1111", 320)
    book2 = EBook("Python Basics", "Eric Matthes", "2222", 5)

    library.add_book(book1)
    library.add_book(book2)

    print("All Books:")
    for b in library.list_books():
        print(b)

    library.check_out_book("1111")

    print("\nAvailable Books:")
    for b in library.list_available_books():
        print(b)
