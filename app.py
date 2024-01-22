from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("localhost", 27017)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# MongoDB Database
db = client.flask_database

# Collection named "todos"
todos = db.todos


if __name__ == "__main__":
    app.run(debug=True)
