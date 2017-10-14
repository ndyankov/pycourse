#!/usr/bin/env python
# -*- coding: utf8

"""
По зададено входящо съобщение да се кодира текста в него 
по следната схема:

Използват се само буквите:
abcdefghijklmnopqrstuvwxyz

Всяка буква се замества със следващата поредна 
в азбуката (z се замества с a)!

Пример:
hello -> ifmmp
zebra -> afcsb


Алтернативно могат да се използват и функциите chr, ord.
"""


def build_rule():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    secret = letters[1:] + letters[0]
    rule = {}
    for i in range(len(letters)):
        rule[letters[i]] = secret[i]
    return rule


RULE = build_rule()

def encode(text):
    result = []
    for letter in text:
        secret = RULE.get(letter)
        result.append(secret)
    return "".join(result)


def decode(text):
    # TODO: implement
    pass


def main():
    print(encode("hello") == "ifmmp")
    print(encode("zebra") == "afcsb")


if __name__ == "__main__":
    main()
