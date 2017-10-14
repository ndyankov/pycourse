#!/usr/bin/env python
# -*- encoding: utf8

"""
Дадени са две строго положителни числа. 
Да се напише функция, която разменя местата им без използването на
допълнителни променливи.
"""

def swap(a, b):
    return b, a

def swap1(a, b):
    """Only allowed are signs + or - """
    a = a + b
    b = a - b
    a = a - b
    return a, b

def swap2(a, b):
    """Only allowed are signs * or / """
    # TODO: implement
    return a, b

def swap3(a, b):
    """Only allowed are bitwise operations on numbers ^ |"""
    # TODO: implement
    return a, b


def main():
    print(swap(6, 10) == (10, 6))
    print(swap1(6, 10) == (10, 6))
    print(swap2(6, 10) == (10, 6))
    print(swap3(6, 10) == (10, 6))


if __name__ == "__main__":
    main()
