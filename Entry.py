class Entry:

	def __init__(self, path, tags=set(), properties=dict(), text=None):
		self.path = path
		self.tags = set(tags)
		self.properties = properties
		if text is None:
			with open(path, 'rb') as f:
				self.text = f.read()
		else:
			self.text = text

	def addTag(self, *tags):
		print(tags)
		for tag in tags:
			self.tags.add(tag);

	def setProperty(self, key, value):
		properties[key] = value

	def setText(self, text):
		self.text = text

	def __str__(self):
		return str(self.path) + '\n' \
				+ 'tags: ' + ', '.join(self.tags) + '\n' \
				+ 'prop: ' + str(self.properties) + '\n' \
				+ 'text: ' + str(self.text) + '\n'

	def __repr__(self):
		return self.__str__()
