import datetime as dt
from peewee import *
from collections import OrderedDict
import os
import sys

db = SqliteDatabase('blog.db')


def menu_loop():
	choice = None
	clear()
	while choice != 'q':
		print("Enter q to quit:")
		for key, value in menu.items():
			print (key, value.__doc__)
		choice = input('Actions: ').lower().strip()
		if choice in menu:
			menu[choice]()

class Entry(Model):
	'''Content, timestamp, url-unique'''
	url = TextField(unique = True)
	content = TextField()
	timestamp = DateField(default=dt.datetime.now)

	class Meta:
		database = db

def add_entry():
	"""Add an Entry"""
	print("Write blog here. Press Ctrl+D when finished")
	data = sys.stdin.read().strip()
	url = input("\nEnter unique url")

	if data:
		Entry.create(content=data, url=url)
		print("\nSaved yo!")

def view_entries(search=None):
	"""View Entries"""
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search:
		entries = entries.where(Entry.content.contains(search))
	for entry in entries:
		timestamp = entry.timestamp.strftime('%A %B %d, %y %I:%M%p')
		print(timestamp)
		print('='*len(timestamp))
		print(entry.url)
		print('='*len(timestamp))
		print(entry.content)
		print('\nn)next entry\nd)Delete entries\nq)return to main menu\n')
		next_action = input('Action: [Nq]').lower().strip()

		if next_action == 'q':
			break
		elif next_action == 'd':
			delete_entry(entry)

def search_entries():
	'''Search through the entries'''
	view_entries(input("Enter search query: "))

def delete_entry(entry):
	"""Delete  entry"""
	entry.delete_instance()


def clear():
	os.system('clear')
	
def initialize():
	db.connect()
	db.create_tables([Entry], safe = True)
	db.close()

menu = OrderedDict([
		('a', add_entry),
		('v', view_entries),
		('s', search_entries)
	])
if __name__ == '__main__':
	initialize()

	menu_loop()