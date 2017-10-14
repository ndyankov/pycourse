#!/usr/bin/env python
# -*- encoding: utf8

"""
Да се напише функция, която приема текст за вход и връща
списък със всички думи в текста по следните правила:
 - думите са изписани с малки букви
 - всяка дума се среща само по веднъж
 - думите са подредени по азбучен ред
[word1, word2, word3]

Вариант 2: да се промени програмата, 
така че да връща броя срещания на всяка дума:
{word: count}
"""

# https://www.youtube.com/watch?v=NBwVm-bWgCM
POETRY = """
Gin a body meet a body, comin thro' the rye,
Gin a body kiss a body, need a body cry;
Ilka body has a body, ne'er a ane hae I;
But a' the lads they loe me, and what the waur am I.

Gin a body meet a body, comin frae the well,
Gin a body kiss a body, need a body tell;
Ilka body has a body, ne'er a ane hae I,
But a the lads they loe me, and what the waur am I.

Gin a body meet a body, comin frae the town,
Gin a body kiss a body, need a body gloom;
Ilka Jenny has her Jockey, ne'er a ane hae I,
But a' the lads they loe me, and what the waur am I.
"""

def words(text):
	# TODO: implement
	return []

def main():
	print(words(POETRY))


if __name__ == "__main__":
	main()
