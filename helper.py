import models

def add_entry(title, post):
	"""Add an Entry"""
	models.Entry.create(content=post, title=title)
	print("On your way boy")
	
def check_unique(title):
	if models.Entry.select().where(models.Entry.title==title):
		return False
	else:
		return True

def view_entry(title):
	if models.Entry.select().where(models.Entry.title==title):
		return models.Entry.select().where(models.Entry.title==title).get()
	else:
		return "No such entry exists"