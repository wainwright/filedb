from Index import *

class UniqueId:
	count = 0
	def get(self):
		self.count += 1
		return self.count

class Database:
	data = {}
	idGenerator = UniqueId()
	index = DatabaseIndex()

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
