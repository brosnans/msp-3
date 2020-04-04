import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'IncidentManager'
app.config["MONGO_URI"] = 'mongodb+srv://user1:welcomeuser1@firstcluster-kacbb.mongodb.net/IncidentManager?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
@app.route('/get_incidents')
def get_incidents():
    return render_template("incidents.html", incidents=mongo.db.incidents.find())

@app.route('/add_task')
def add_task():
    return render_template("addincident.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
