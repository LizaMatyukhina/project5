"""
Написать программу, которая считывает данные из файла input.txt.
Задача программы, каждую строку текста проверить на палиндром и вывести,
кол-во палиндромных строк в тексте и сами строки.
"""

import string

bad_chars = string.whitespace + string.punctuation
count = 0

file_start = input('Введите имя файла: ')

try:
    input_file = open(file_start, 'r')
except FileNotFoundError:
    print('Файл {} не найден'.format(file_start))
    exit()
