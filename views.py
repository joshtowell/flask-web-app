from flask import Blueprint, render_template, request, jsonify
import json

views = Blueprint(__name__, "views")

# Example: http://127.0.0.1:8000/
@views.route("/")
def home():
    return render_template("index.html", project = "Flask Web App")

# Example: http://127.0.0.1:8000/user/Joshua
@views.route("/user/<username>")
def profile(username):
    return render_template("profile.html", name = username)

# Example: http://127.0.0.1:8000/projects?category=Electronics
@views.route("/projects")
def projects():
    args = request.args
    category = args.get('category')
    return render_template("projects.html", category = category)

# Example: http://127.0.0.1:8000/json?user=Joshua
@views.route("/json")
def getJson():
    args = request.args
    user = args.get('user')
    users = readJson("users")
    for u in users:
        print(u, user)
        if u == user:
            return jsonify(users[u])
    return f'No records could be found for "{user}"!'


def readJson(filename):
    file = open(f"{filename}.json")
    data = json.load(file)
    file.close()
    return data