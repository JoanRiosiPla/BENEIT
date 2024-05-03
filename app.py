# Joan Rios i Pla contact.joanrios@gmail.com 2024

import os

from flask import Flask, request, jsonify, render_template
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

import werkzeug.exceptions

print("Declaring app...")
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'

print("Connecting to database...")
databaseUrl = os.environ.get("DATABASE_URL")
print("DatabaseUrl: " + databaseUrl)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseUrl
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
print("Connected to database")

print("Creating tables if they don't exist...")
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	hash = db.Column(db.String)
	email = db.Column(db.String)
	firstTime = db.Column(db.Boolean)

# Define Project model
class Insult(db.Model):
	__tablename__ = 'insults'
	id = db.Column(db.Integer, primary_key=True)
	insult = db.Column(db.String)
	definition = db.Column(db.String)
	sourceName = db.Column(db.String)
	sourceUrl = db.Column(db.String)
	# Store every rating it has received (array)
	ratings = db.Column(db.String)
	averageRating = db.Column(db.Float)
	# Store every user that has rated it (array)
	users = db.Column(db.String)
	tags = db.Column(db.String)

class File(db.Model):
	__tablename__ = 'files'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	contents = db.Column(db.LargeBinary)


# Configure session to use database
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"
app.config["PERMANENT_SESSION_LIFETIME"] = 3600 # 1 hour

# Configure session to use already declared database
app.config["SESSION_SQLALCHEMY"] = db

# Create tables
with app.app_context():
	db.create_all()
	# Use session settings declared above
	Session(app)
print("Tables created")

# Create directories
# print("Creating directories...")
# if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], "images")):
#     os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], "images"))
# print("Directories created")

print("More config...")
# Create image for loaders
# img = Image.new("RGB", (1, 1), "#99AABC")
# img.save(os.path.join("static","loader.png"))

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
print("App ready")



app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/aleatori')
def aleatori():
	return render_template('aleatori.html')

@app.route('/insults')
def insults():
	# make json in this structure:
	#  "insults": [
	#     {
	#         "definicio": "Persona que fa anar malament un pla previst.",
	#         "font": {
	#             "nom": "Viccionari",
	#             "url": "https://ca.m.wiktionary.org/wiki/aixafaguitarres"
	#         },
	#         "paraula": "Aixafaguitarres",
	#         "tags": [
	#             "despectiu"
	#         ]
	#     },
	# .......
	

	# If there is already a file named insults.json in the db, get it and return it
	insults = File.query.filter_by(name="insults.json").first()
	if insults:
		return insults.contents

	# If not, create it
	insultsDB = Insult.query.all()
	insults = []
	for insult in insultsDB:
		insults.append({
			"definicio": insult.definition,
			"font": {
				"nom": insult.sourceName,
				"url": insult.sourceUrl
			},
			"paraula": insult.insult,
			"tags": insult.tags.split(",")
		})
	return jsonify(insults)
 

	

# All errors
@app.errorhandler(werkzeug.exceptions.HTTPException)
def error(e):
	return render_template('404.html', error = str(e.code)), e.code
