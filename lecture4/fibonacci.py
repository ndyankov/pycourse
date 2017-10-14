#!/usr/bin/env python

"""
Given a number N, print the first N items in the Fibonacci sequence.
"""


def fibonacci(n):
    res = []
    if n>0:
        res.append(1)
    if n>1:
        res.append(1)
    for i in range(2, n):
        res.append(res[i-1] + res[i-2])
    return res


def main():
    print(fibonacci(0) == [])
    print(fibonacci(1) == [1])
    print(fibonacci(2) == [1, 1])
    print(fibonacci(3) == [1, 1, 2])
    print(fibonacci(7) == [1, 1, 2, 3, 5, 8, 13])


if __name__ == "__main__":
    main()
