import os
import pymongo
import datetime


MONGO_DB_PASSWORD = os.environ.get("MONGODB_PASSW")
client = pymongo.MongoClient(f"mongodb+srv://ihaveread:{MONGO_DB_PASSWORD}@cluster0.1qdqn.mongodb.net/<dbname>?retryWrites=true&w=majority")

# Creating a database with the name 'test'
db = client.books
wanted_db = db.wanted
read_db = db.read

post = {
    "author": "Mike Snow",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow(),
    "reason": "Sounds awesome"
}

# inserting the variable books into a collection name post. Use "."-notation.
id = wanted_db.insert_one(post).inserted_id
print(id)
