"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
также проверить тип и содержимое переменных.
"""


def check_type_pair(word_1, word_2):
    if type(word_1) == type(word_2):
        return f'Типы равнозначны - {word_1} - {type(word_1)}'
    else:
        return f'Типы разные! {word_1} - {type(word_1)}, {word_2} - {type(word_2)}'


def check_value_pair(word_1, word_2):
    if word_1 == word_2:
        return f'Значения одинаковы - {word_2}'
    else:
        return f'Значения разные! {word_1}, {word_2}'


words = [
    ('разработка', '\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430'),
    ('сокет', '\u0441\u043E\u043A\u0435\u0442'),
    ('декоратор', '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440'),
]

for word in words:
    print(check_type_pair(word[0], word[1]))
    print(check_value_pair(word[0], word[1]))
