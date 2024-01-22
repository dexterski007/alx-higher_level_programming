#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	enum = 0
	try:
		while enum is not x:
			print(my_list[enum], end="")
			enum += 1
	except IndexError:
		None
	print()
	return enum
