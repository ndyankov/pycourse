#!/usr/bin/python


import sys
from optparse import OptionParser


def main(argv):
	print(argv)
	print(__file__)

	parser = OptionParser()
	parser.add_option('-f', '--file', dest='filename', 
		help='output filename', metavar='FILE')

	options, args = parser.parse_args()

	print(options)
	print(args)
	print(options.filename)

# TODO: enhance with:
# pid
# current dir
# environment varialbles
# arguments
# memory


if __name__ == "__main__":
	sys.exit(main(sys.argv))
