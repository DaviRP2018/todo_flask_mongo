from bson import ObjectId
from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("localhost", 27017)

# MongoDB Database
db = client.flask_database

# Collection named "todos"
todos = db.todos


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["content"]
        degree = request.form["degree"]
        todos.insert_one({"content": content, "degree": degree})
        return redirect(url_for("index"))
    all_todos = todos.find()
    return render_template("index.html", todos=all_todos)


@app.post("/<id>/delete/")
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
