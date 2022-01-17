#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	try:
		new_list = my_list[:x]
		count = 0
		print(new_list)
		for i in new_list:
			count = count + 1
		return count
	except:
		return count
