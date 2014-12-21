from Index import *

import os
import pickle

_defaultPath = os.path.expanduser('~/.filedb')
_dbFilename = 'db.pickle'

class UniqueId:
	def __init__(self):
		self.count = 0

	def get(self):
		self.count += 1
		return self.count

def loadDb(path=_defaultPath, createIfNotFound=True):
	# create the directory if not present
	if not os.path.exists(_defaultPath):
		os.makedirs(_defaultPath)
	# open the file
	try:
		with open(path + '/' + _dbFilename, 'rb') as f:
			return pickle.load(f)
	except IOError:
		if createIfNotFound:
			return Database()
		else:
			raise

class Database:

	def __init__(self):
		self.data = {}
		self.idGenerator = UniqueId()
		self.index = DatabaseIndex()

	def save(self, path=_defaultPath):
		with open(path + '/' + _dbFilename, 'wb') as f:
			pickle.dump(self, f);

	# todo should be atomic
	def addEntry(self, entry):
		newId = self.idGenerator.get()
		self.data[newId] = entry
		self.index.add(newId, entry)

	def lookup(self, term):
		return [self.data[j] for j in self.index.lookup(term)]

	def __str__(self):
		return self.data.__str__()

	def __repr__(self):
		return self.__str__()
