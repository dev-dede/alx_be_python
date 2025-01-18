class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self._is_checked_out = False
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        if isinstance (book, Book):
            self._books.append(book)
        else:
            print("Only instances of class Book can be added")
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return
                else:
                    print("Book is already checked out")
                    return
        print(f"There is no book with the title {title}")
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                return
        print("We don't have this book in our collection")
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")
    
    