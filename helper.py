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

def del_entry(title):
	a = models.Entry.select().where(models.Entry.title==title)
	if a:
		b = models.Entry.delete().where(models.Entry.title==title)
		return b.execute()
	else:
		return "No such entry exists"
