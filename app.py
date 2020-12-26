from flask import Flask, render_template

app = Flask(__name__)
# By default do not jsonify strings to ascii but Unicode
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def index():
    """Index with cards for a variety of recipies."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
