"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

import chardet
import locale
# Получим кодировку ОС по умолчани.
def_encoding = locale.getpreferredencoding()
# print(def_encoding)

new_lines = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]
# Запишем в файл строки и проверим кодировку файла по умолчанию (просто так)
with open('test_file.txt', 'w') as test_file:
    test_file.write('\n'.join(new_lines))
    if def_encoding == test_file.encoding:
        print(f'Используется кодировка по умолчанию: {def_encoding}')
    else:
        print(f'file encoding = {test_file.encoding}')

# По сути, код ниже работает не только для utf8, работает для (по идее) почти любой указанной кодировки
with open('test_file.txt', encoding='utf8') as test_file:
    with open(test_file.name, 'rb') as t_file:
        raw_data = t_file.read()
        raw_encoding = (chardet.detect(raw_data))['encoding']
        encoding_data = raw_data.decode(raw_encoding).encode(test_file.encoding)
    print(encoding_data.decode(test_file.encoding))
