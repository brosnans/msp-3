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
    return render_template("incidents.html", 
    incidents=mongo.db.incidents.find())

@app.route('/add_incident')
def add_task():
    return render_template("addincident.html", 
    categories=mongo.db.categories.find())

@app.route('/insert_incident', methods=['POST'])
def insert_incident():
    incidents = mongo.db.incidents
    incidents.insert_one(request.form.to_dict())
    return redirect(url_for('get_incidents'))

@app.route('/edit_incident/<incident_id>')
def edit_incident(incident_id):
    the_incident =  mongo.db.incidents.find_one({"_id": ObjectId(incident_id)})
    all_categories =  mongo.db.categories.find()
    return render_template("editincident.html", incident=the_incident,
                           categories=all_categories)

@app.route('/update_incident/<incident_id>', methods=["POST"])
def update_incident(incident_id):
    incident = mongo.db.incident
    incident.update( {'_id': ObjectId(incident_id)},
    {
        'category_name':request.form.get('category_name'),
        'affected_person':request.form.get('affected_person'),
        'incident_description': request.form.get('incident_description'),
        'investigation_due': request.form.get('investigation_due'),
        'first_aid_required':request.form.get('first_aid_required')
    })
    return redirect(url_for('get_incidents'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())

if __name__ == '__main__':
    app.run(host=(os.environ.get('IP', '0.0.0.0')),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
