#!/usr/bin/env python

"""
Determine whether three numbers a, b, c are sides of a triangle.
Each number must be smaller than the sum of the other two!
"""

def triangle(a, b, c):
    return a<b+c and b<a+c and c<a+b

def triangle2(a, b, c):
    sides = set([a, b, c])
    for num in sides:
        others = sides.copy()
        others.remove(num)
        if num >= sum(others):
            return False
    return True

def main():
    print(triangle(3, 4, 5) is True)
    print(triangle(3, 5, 4) is True)
    print(triangle(4, 3, 5) is True)
    print(triangle(4, 5, 3) is True)
    print(triangle(5, 3, 4) is True)
    print(triangle(5, 4, 3) is True)

    print(triangle(1, 2, 3) is False)


    print(triangle2(3, 4, 5) is True)
    print(triangle2(3, 5, 4) is True)
    print(triangle2(4, 3, 5) is True)
    print(triangle2(4, 5, 3) is True)
    print(triangle2(5, 3, 4) is True)
    print(triangle2(5, 4, 3) is True)

    print(triangle2(1, 2, 3) is False)


if __name__ == "__main__":
    main()
