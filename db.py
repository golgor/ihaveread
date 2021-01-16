import os
import pymongo
import datetime


# API-keys from WSL-environment
MONGODB_API_KEY = os.environ.get("MONGODB_API_KEY")
GOOGLE_BOOKS_API_KEY = os.environ.get("GOOGLE_BOOKS_API_KEY")

# Creating client to be used with PyMongo.
client = pymongo.MongoClient(
    f"mongodb+srv://ihaveread:{MONGODB_API_KEY}@cluster0.1qdqn.mongodb.net/ihaveread?retryWrites=true&w=majority")

# Creating a database with the name 'test'
db = client.books
wanted_db = db.wanted
read_db = db.read

# TODO: https://medium.com/@chanyamhung/apis-books-data-via-isbn-d29285572683
# TODO: https://www.bokus.com/cgi-bin/product_search.cgi?show_advanced=1
# TODO: https://isbndb.com/apidocs/v2
# TODO: https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data
# TODO: https://openlibrary.org/dev/docs/api/books
# TODO: https://en.wikipedia.org/wiki/International_Standard_Book_Number


def main():
    post = {
        "author": "Mike Snow",
        "isbn": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow(),
        "reason": "Sounds awesome"
    }

    # inserting the variable books into a collection name post.'
    # Use "."-notation.
    id = wanted_db.insert_one(post).inserted_id
    print(id)


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


def get_data_from_isbn():
    """Used to fetch data about a book from the ISBN,
    either ISBN API or OpenLibrary. Might be placed in another
    .py-file for data fetching.
    """
    pass


if __name__ == "__main__":
    main()
