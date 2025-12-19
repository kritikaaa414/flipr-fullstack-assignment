from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from config import MONGO_URI

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)
CORS(app)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return {"message": "Flipr backend running with MongoDB"}

# ---------------- PROJECTS ----------------
@app.route("/add-project", methods=["POST"])
def add_project():
    data = request.json
    mongo.db.projects.insert_one(data)
    return {"message": "Project added successfully"}

@app.route("/projects", methods=["GET"])
def get_projects():
    projects = list(mongo.db.projects.find({}, {"_id": 0}))
    return jsonify(projects)

# ---------------- CLIENTS ----------------
@app.route("/add-client", methods=["POST"])
def add_client():
    data = request.json
    mongo.db.clients.insert_one(data)
    return {"message": "Client added successfully"}

@app.route("/clients", methods=["GET"])
def get_clients():
    clients = list(mongo.db.clients.find({}, {"_id": 0}))
    return jsonify(clients)

# ---------------- CONTACT FORM ----------------
@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    mongo.db.contacts.insert_one(data)
    return {"message": "Contact form submitted"}

# ---------------- NEWSLETTER ----------------
@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    mongo.db.subscribers.insert_one(data)
    return {"message": "Subscribed successfully"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

