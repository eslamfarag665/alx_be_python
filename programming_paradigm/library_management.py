class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

class Library:
    """A class representing a library."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def find_book(self, isbn):
        """Find a book in the library by its ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        """List all books in the library."""
        return [str(book) for book in self.books]