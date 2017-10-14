#!/usr/bin/env python

"""
Given an input string, write a function that determines
whether the brackets in it are balanced.
Only () need to be supported.
Each opening "(" bracket needs to have a matching 
closing ")" bracket that comes after it.


Examples:
good: "(1+2)*(3-2*(20))"
bad: ")(2)"

Hints: use a list to realize a stack.
Add an opening bracket to the end.
When adding a closing one check whether there's an opening
one at the top and remove it.

The brackets are balanced if at the end the stack/list of length 0.
"""

def brackets(text):
	# TODO: write here
	return True

def main():
	print(brackets("(1+2)*a-10") is True)
	print(brackets("sqrt(2/3)") is True)
	print(brackets(")(") is False)


if __name__ == "__main__":
	main()
