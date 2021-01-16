class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def add_summary(self, summary: str) -> None:
        self.summary = summary

    def get_dict(self) -> dict:
        if not self.book_dict:
            self.book_dict = {
                "title": self.title,
                "author": self.author,
                "year": self.year
            }
        return self.book_dict

    def __str__(self):
        return f"{self.title}, by {self.author} {self.year}"


class BookCase:
    def __init__(self):
        self.bookcase = []

    def add_book(self, book: Book):
        self.bookcase.append(book)

    def get_titles(self) -> list:
        return [book.title for book in self.bookcase]


if __name__ == '__main__':
    book1 = Book("Start With Why", "Simon Sinek", 2011)
    book2 = Book("The Salt Fix", "James DiNicolantonio", 2017)
    print(book1)
    print(book2)
    read_books = BookCase()
    read_books.add_book(book1)
    read_books.add_book(book2)
    read_books.add_book(
        Book(
            title="Find Your Why",
            author="Simon Sinek",
            year=2017
        )
    )
    print(read_books.get_titles())
