import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'incident_manager'
app.config["MONGO_URI"] = 'mongodb+srv://user1:welcomeuser1@firstcluster-kacbb.mongodb.net/incident_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_incidents')
def get_incidents():
    return render_template("incidents.html", incidents=mongo.db.incidents.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
