class Index:
	'''A generic index '''
	index = {}

	def add(self, key, entries):
		for e in entries:
			if e not in self.index:
				self.index[e] = set()
			self.index[e].add(key)

	def lookup(self, term):
		try: return self.index[term]
		except KeyError: return set()

class DatabaseIndex:
	'''An index specifically for the file database'''
	tagIndex = Index()
	textIndex = Index()
	propertyIndex = Index()

	def add(self, identity, entry):
		self.tagIndex.add(identity, entry.tags)
		self.textIndex.add(identity, entry.text.split())
		self.propertyIndex.add(identity, entry.properties.keys())

	def lookup(self, term):
		return \
			self.tagIndex.lookup(term) | \
			self.textIndex.lookup(term) | \
			self.propertyIndex.lookup(term)
