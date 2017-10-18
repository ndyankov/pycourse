#!/usr/bin/env python

"""
EGN validator
"""

def validate(text):
    if not isinstance(text, str):
        return False
    if len(text) != 10:
        return False
    if not text.isdigit():
        return False
    try:
        egn(text)
    except ValueError:
        return False
    return True

def egn(text):
    year = text[0:2]
    month = text[2:4]
    day = text[4:6]
    area = text[6:9]
    checksum = text[9]

    digits = [int(x) for x in text[0:9]]
    sex = "M" if int(text[8]) % 2 == 0 else "F"

    if not validate_date(year, month, day):
        raise ValueError('invalid date')

    if calc_checksum(digits) != int(checksum):
        raise ValueError('invalid EGN')

    return (int(year), int(month), int(day), area, sex, int(checksum))

def validate_date(year, month, date):
    return True

def calc_checksum(digits):
    weights = (2,4,8,5,10,9,7,3,6)
    check = sum([weights[i]*digits[i] for i in range(9)]) % 11
    if check == 10:
        check = 0
    return check

def generate(year, month, day):
    for area in range(1000):
        tokens = []
        tokens.append(str(year))
        tokens.append(str(month).zfill(2))
        tokens.append(str(day).zfill(2))

        tokens.append(str(area).zfill(3))

        digits = ''.join(tokens)
        digits = [int(x) for x in digits]

        check = calc_checksum(digits)

        tokens.append(str(check))

        egn = ''.join(tokens)

        yield egn


def main():
    for egnto in generate(88, 8, 8):
        egn(egnto)
        assert validate(egnto)
        print(egnto)


if __name__ == "__main__":
    main()
