# Define the Library class (or import it if it's in another file)
class Library:
	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def list_books(self):
		for book in self.books:
			print(book)

# Define the Book class
class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self):
		return f"{self.title} by {self.author}"

# Define the EBook class inheriting from Book
class EBook(Book):
	def __init__(self, title, author, file_size):
		super().__init__(title, author)
		self.file_size = file_size

	def __str__(self):
		return f"{self.title} by {self.author} (EBook, {self.file_size}KB)"

# Define the PrintBook class inheriting from Book
class PrintBook(Book):
	def __init__(self, title, author, pages):
		super().__init__(title, author)
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author} (PrintBook, {self.pages} pages)"

my_library = Library()

classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

my_library.add_book(classic_book)
my_library.add_book(digital_novel)
my_library.add_book(paper_novel)

my_library.list_books()
