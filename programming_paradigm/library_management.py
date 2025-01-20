class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self._is_checked_out = False
    def check_out_book(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"Book {self.title} by {self.author} is already checked out")
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"Book {self.title} by {self.author} has already been returned")
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        # #User would need to create an object of the book class and pass it to add_book.
        # #Example, object_name.add_book(Book("Abyss", "Dede")) NOT object_name.add_book("Abyss", "Dede") to handle AttributeError
        if isinstance (book, Book):
            self._books.append(book)
        else:
            print("Only instances of class Book can be added")
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()
                return
        print(f"There is no book with the title {title} in our collection")
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"We don't have {title} in our collection")
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}") #To print list of book in human readable format instead of objects
        else:
            print("There are no available books in the library")
    
    