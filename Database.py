class UniqueId:
	count = 0
	def get(self):
		self.count += 1
		return self.count

class Database:
	data = {}
	idGenerator = UniqueId()

	def addEntry(self, entry):
		self.data[self.idGenerator.get()] = entry;

	def __str__(self):
		return self.data.__str__()

	def __repr__(self):
		return self.__str__()
