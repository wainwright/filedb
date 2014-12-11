class Database:
	_index = {}

	def addEntry(self, entry):
		self._index[entry.path] = entry;

	def __str__(self):
		return self._index.__str__()

	def __repr__(self):
		return self.__str__()
