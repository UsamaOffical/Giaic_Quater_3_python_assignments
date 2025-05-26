class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

# Usage
b1 = Book("Python 101")
b2 = Book("Data Science")
print(f"Total Books: {Book.total_books}")
