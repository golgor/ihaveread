class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def add_summary(self, summary: str) -> None:
        self.summary = summary

    def get_dict(self) -> dict:
        if not hasattr(self, "book_dict"):
            self.book_dict = {
                "title": self.title,
                "author": self.author,
                "isbn": self.isbn
            }
        return self.book_dict

    def __str__(self):
        return f"{self.title}, by {self.author}"


class BookCase:
    def __init__(self):
        self.bookcase = []

    def add_book(self, book: Book):
        self.bookcase.append(book)

    def get_titles(self) -> list:
        return [book.title for book in self.bookcase]


def validate_isbn_10():
    # Prefix – alla ISBN inleds med prefixet 978.
    # Områdesbeteckning – för nationellt, geografiskt eller
    #   språkligt bestämda områden (Sverige har till exempel 91).
    # Förlagsbeteckning – vilket förlag boken ges ut genom.
    # identifikationssiffror
    # En kontrollsiffra
    pass


def validate_isbn_13():
    pass


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
            isbn="12451341241"
        )
    )
    print(read_books.get_titles())
    print(book1.get_dict())
