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
with open(file_start) as f_in:
    for line in f_in:
        modified_line = line.lower()
        for i in bad_chars:
            modified_line = modified_line.replace(i,'')
            modified_str = modified_line[::-1]
        if modified_str == modified_line:
            count += 1
            print(line, end = '')
print('\n')
if count == 0:
    print('В данном тексте нет палиндромов!:(')
else:
    print('В этом тексте найдено {} палиндромов, все они написаны чуть выше!!'.format(count))
    print('Все остальные строки палиндромами не являются.')

