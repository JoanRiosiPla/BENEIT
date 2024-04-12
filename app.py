# Joan Rios i Pla contact.joanrios@gmail.com 2024

from flask import Flask, request, jsonify, render_template
import werkzeug.exceptions

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/aleatori')
def aleatori():
	return render_template('aleatori.html')

# All errors
@app.errorhandler(werkzeug.exceptions.HTTPException)
def error(e):
	return render_template('404.html', error = str(e.code)), e.code
