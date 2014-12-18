#!/usr/bin/python3

from datetime import datetime

from Entry import Entry
from Database import Database

import sys

d = Database()

d.addEntry(
		Entry(
			'receipt1.pdf',
			tags=set(('receipt', 'donation', 'tax', 'oxfam')),
			properties={'value':10.55, 'date':datetime(2014, 12, 11)},
			text='donation receipt to oxfam for $10.55'))

d.addEntry(
		Entry(
			'receipt2.pdf',
			tags=set(('receipt', 'groceries', 'woolworths')),
			properties={'value':40.0, 'date':datetime(2014, 12, 9)},
			text='hummus $10, avocados $4'))

d.addEntry(
		Entry(
			'receipt3.pdf',
			tags=set(('receipt', 'clothing', 'myer', 'tax')),
			properties={'value':140.0, 'date':datetime(2014, 12, 9)},
			text='jeans $140'))

print('LOOKUP:')
print('------------------------------')
print('receipt:\n', d.lookup('receipt'))
print('------------------------------')
print('tax:\n',     d.lookup('tax'))
print('------------------------------')
print('myer:\n',    d.lookup('myer'))
sys.exit(0)

# TEST the properties
for e in d.data:
	v = d.data[e]
	try:
		if v.properties['value'] < 60:
			print(v)
	except KeyError:
		pass
