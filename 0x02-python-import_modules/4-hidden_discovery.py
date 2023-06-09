#!/usr/bin/python3
if __name__ == "__main__":
	import hidden_4

	objects = dir(hidden_4)

	for i in range(len(objects)):
		obj = objects[i]

		if obj[:2] == '__':
			continue

	else:
		print('{}'.format(objects[i]))
