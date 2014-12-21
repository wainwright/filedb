#!/usr/bin/python3

import sys
import argparse
from Entry import Entry
from Database import Database, loadDb

filedb = None;

def add(args):
	entry = Entry(path=args.file, tags=args.tags)
	filedb.addEntry(entry)
	print(filedb)
	print(filedb.lookup('gift'))

def search(args):
	print(filedb.lookup(args.term))

def listAll(args):
	print(filedb.index.tagIndex.index)
	print(filedb.data)

def parseArgs(argv):
	parser = argparse.ArgumentParser(prog='filedb')

	subparsers = parser.add_subparsers()

	parser_add = subparsers.add_parser('add', help='add entry')
	parser_add.add_argument('file', type=str, help='file to add')
	parser_add.add_argument('--tags', '-t', type=str, nargs='*', help='tags')
	parser_add.set_defaults(func=add)

	parser_search = subparsers.add_parser('search', help='find entry')
	parser_search.add_argument('term', type=str, help='search term')
	parser_search.set_defaults(func=search)

	parser_list = subparsers.add_parser('list', help='list all entries')
	parser_list.set_defaults(func=listAll)

	args = parser.parse_args(argv)
	args.func(args)

if __name__ == '__main__':
	filedb = loadDb()
	parseArgs(sys.argv[1:])
	filedb.save()
