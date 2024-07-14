# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

    def check_out(self):
        """Check out the book."""
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book."""
        if self.checked_out:
            self.checked_out = False
            return True
        return False

class Library:
    """A class representing a library."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        for book in self._books:
            if book.isbn == isbn:
                self._books.remove(book)
                return True
        return False

    def find_book(self, isbn):
        """Find a book in the library by its ISBN."""
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        """List all books in the library."""
        return [str(book) for book in self._books]

    def list_available_books(self):
        """List all available (not checked out) books in the library."""
        return [str(book) for book in self._books if not book.checked_out]

    def check_out_book(self, isbn):
        """Check out a book from the library by its ISBN."""
        book = self.find_book(isbn)
        if book and book.check_out():
            return True
        return False

    def return_book(self, isbn):
        """Return a book to the library by its ISBN."""
        book = self.find_book(isbn)
        if book and book.return_book():
            return True
        return False
