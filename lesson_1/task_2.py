"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

b_words = [
    b'class',
    b'function',
    b'method',
]

for b_word in b_words:
    print(type(b_word))
    print(b_word)
    print(len(b_word))
