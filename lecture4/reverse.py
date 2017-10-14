#!/usr/bin/env python

"""
Given a string return the reversed string.
"""


def reverse(text):
	result = []
	n = len(text)
	while n>0:
		n = n -1
		result.append(text[n])
	return "".join(result)

def reverse2(text):
	# slice from start to end with a step -1
	return text[::-1]

def main():
	print(reverse("hello") == "olleh")
	print(reverse(reverse("hello")) == "hello")

	print(reverse2("hello") == "olleh")
	print(reverse2(reverse2("hello")) == "hello")


if __name__ == "__main__":
	main()
