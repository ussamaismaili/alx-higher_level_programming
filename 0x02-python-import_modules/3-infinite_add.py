#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv

	if len(argv) == 1:
	print('{:d}'.format(len(argv)-1))

	elif len(argv) > 1:
	sum = 0
	for i in range(1, len(argv)):
		sum += int(argv[i])
	print('{:d}'.format(sum))
