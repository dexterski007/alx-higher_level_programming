#!/usr/bin/python3
""" this is a module for reaading files """

def read_file(filename=""):
	""" read files """
	with open(filename, 'r') as file:
		file_contents = file.read()
		print(file_contents, end='')
