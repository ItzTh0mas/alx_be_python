class Book:
    """
    Represents a book with a title and author.
    Tracks whether the book is checked out.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Book wasn't checked out

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Represents a library that manages a collection of books.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title.
        Returns True if successful, False if book not found or unavailable.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """
        Returns a book by title.
        Returns True if successful, False if book not found or wasn't checked out.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or wasn't checked out

    def list_available_books(self):
        """
        Prints all books in the library that are currently available.
        """
        for book in self._books:
            if book.is_available():
                print(book)
