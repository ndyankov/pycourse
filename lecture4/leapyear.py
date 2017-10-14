#!/usr/bin/env python

"""
Determine whether a given year is a leap year.
"""

def leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    print(leap(2000) is True)
    print(leap(2001) is False)
    print(leap(2004) is True)
    print(leap(2100) is False)
    print(leap(2400) is True)


if __name__ == "__main__":
    main()
