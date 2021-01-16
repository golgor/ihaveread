import os
import pymongo
import datetime
from books import Book

# API-keys from WSL-environment
MONGODB_API_KEY = os.environ.get("MONGODB_API_KEY")
GOOGLE_BOOKS_API_KEY = os.environ.get("GOOGLE_BOOKS_API_KEY")

# Creating client to be used with PyMongo.
client = pymongo.MongoClient(
    f"mongodb+srv://ihaveread:{MONGODB_API_KEY}@cluster0.1qdqn.mongodb.net/ihaveread?retryWrites=true&w=majority")

# Creating a database with the name 'test'
db = client.books

# TODO: https://medium.com/@chanyamhung/apis-books-data-via-isbn-d29285572683
# TODO: https://www.bokus.com/cgi-bin/product_search.cgi?show_advanced=1
# TODO: https://isbndb.com/apidocs/v2
# TODO: https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data
# TODO: https://openlibrary.org/dev/docs/api/books
# TODO: https://en.wikipedia.org/wiki/International_Standard_Book_Number


def add_to_wanted(book):
    _add(book, db.wanted)


def add_to_finished(book):
    _add(book, db.finished)


def _add(book, db):
    if isinstance(book, Book):
        id = db.insert_one(book.get_dict())
        return id
    else:
        raise TypeError


def main():
    pass


def get_data_from_isbn():
    """Used to fetch data about a book from the ISBN,
    either ISBN API or OpenLibrary. Might be placed in another
    .py-file for data fetching.
    """
    pass


if __name__ == "__main__":
    main()
