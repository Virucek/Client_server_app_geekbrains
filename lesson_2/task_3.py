"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

products_list = [
    'chair',
    'sofa',
    'table',
]

products_dict = dict.fromkeys(products_list)

price = 100
for key in products_dict:
    products_dict[key] = str(price) + '\u20AC'
    price += 50

data_to_yaml = {
    'products': products_list,
    'products_quantity': 100,
    'products_price': products_dict,
}

file_name = 'test.yaml'


def write_to_yaml(data=data_to_yaml, f_name=file_name):
    with open(f_name, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True, default_flow_style=False)


def read_yaml(f_name=file_name):
    with open(f_name, encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


write_to_yaml()
assert read_yaml() == data_to_yaml, 'Данные в созданном файле не совпадают с изначальными!'
