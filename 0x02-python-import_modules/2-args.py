#!/usr/bin/python3
def print_arg_ke(argv):
	n = len(argv) - 1
	if n == 0:
		print("{:d} argument{}.".format(n, '' if n == 1 else 's'))
		return
	else:
		print("{:d} argument{}:".format(n, '' if n == 1 else 's'))
		i = 1
		while i <= n:
			print("{:d}: {}".format(i, argv[i]))
			i += 1

if __name__ == "__main__":
	import sys
	print_arg_ke(sys.argv)
