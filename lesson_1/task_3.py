"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""
words = [
    'attribute',
    'класс',
    'функция',
    'type',
]

for word in words:
    try:
        b_word = bytes([ord(char) for char in word])
    except ValueError as e:
        print(f'{word} -- невозможно записать в байтовом типе')
