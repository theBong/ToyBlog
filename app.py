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

@app.route('/post/<title>')
def view(title):
	if helper.check_unique(title):
		return "No such post exists"
	else:
		entry=helper.view_entry(title)
		print (entry.content)
		return render_template("post.html",entry=entry)

@app.route('/delete/<title>')
def delete(title):
	helper.del_entry(title)
	return render_template("save.html", content=str(title + " kar diya delete"))

@app.route('/save', methods = ['POST'])
def save():
	title = request.form.get('title')
	post = request.form.get('post')
	if (title and post) and helper.check_unique(title):
		helper.add_entry(title,post)
		return render_template("save.html", content=str("Saved : " + title + " : " + post))
	else:
		return render_template("save.html", content="Title already taken")	

if __name__ == '__main__':
	models.initialize()
	app.run(debug = True, host='0.0.0.0', port = 8080)