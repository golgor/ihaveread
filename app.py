from books import Book
import db

from flask import (
    Flask,
    render_template,
    redirect,
    url_for
)

app = Flask(__name__)
# By default do not jsonify strings to ascii but Unicode
app.config["JSON_AS_ASCII"] = False


# TODO: Read POST parameters
@app.route("/add/finished", methods=["POST", "GET"])
def add_to_finished():
    book2 = Book("The Salt Fix", "James DiNicolantonio", 2017)
    db.add_to_finished(book2)
    return redirect(url_for('index'))


# TODO: Read POST parameters
@app.route("/add/wanted", methods=["POST", "GET"])
def add_to_wanted():
    book2 = Book("The Salt Fix", "James DiNicolantonio", 2017)
    db.add_to_wanted(book2)
    return redirect(url_for('index'))


@app.route("/")
def index():
    """Index with cards for a variety of recipies."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
