from flask import (Flask, render_template, request,
					redirect, url_for, make_response)
import helper
import models

app = Flask(__name__)


def get_data():
	entries = models.Entry.select()
	return entries

@app.route('/')
def index():
	return render_template("index.html", entries=get_data())

@app.route('/add')
def add():
	return render_template("add.html")

@app.route('/save', methods = ['POST'])
def save():

	title = request.form.get('title')
	post = request.form.get('post')
	if (title and post) and helper.check_unique(title):
		helper.add_entry(title,post)
		return "Saved : " + title + " : " + post
	else:
		return "Title already taken"
	

if __name__ == '__main__':
	models.initialize()
	app.run(debug = True, host='0.0.0.0', port = 8080)