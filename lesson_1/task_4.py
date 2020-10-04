"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

words = [
    'разработка',
    'администрирование',
    'protocol',
    'standard',
]

for word in words:
    if isinstance(word, str):
        word = word.encode('utf8')
        print(word)
        word = word.decode('utf8')
        print(word)
    else:
        print(f'{word} не строка')