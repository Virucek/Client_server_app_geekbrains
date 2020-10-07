"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re


# РЕШЕНИЕ 1 - через регулярки
# Передаем файлы, из которых нужно получить информацию
def get_data(*files):
    # Делаем универсальную функцию, чтобы можно было достать любой параметр из файлов
    main_data = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]

    res_data = [
        main_data,
    ]
    # Номер файла (первый элемент в строке в csv)
    i = 0

    for file in files:
        with open(file) as file_open:
            text = file_open.read()
            i += 1
            data_list = [i, ]
            for data in main_data:
                line = re.search(data + '.*\n', text)
                if line is not None:
                    line = (re.split(": ", line.group(0))[-1]).strip()
                # Если не нашли нужные данные - запишем None и в csv на данном месте будет пропуск
                data_list.append(line)
            res_data.append(data_list)
    return res_data


def write_to_csv(csv_file, *files):

    with open(csv_file, 'w') as csv_file:
        csv_data = get_data(*files)
        csv_file_writer = csv.writer(csv_file)
        for line in csv_data:
            csv_file_writer.writerow(line)


# -----------------------------------------------------------------------------
# РЕШЕНИЕ 2 - через массивы
# Передаем файлы, из которых нужно получить информацию
def get_data_array(*files):
    # Делаем универсальную функцию, чтобы можно было достать любой параметр из файлов
    main_data = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]

    res_data = [
        main_data,
    ]
    # Номер файла (первый элемент в строке в csv)
    i = 0

    for file in files:
        with open(file) as file_open:
            i += 1
            data_list = [i, ]
            j = 0
            # ЧТобы обеспечить наличие None в случае ненахождения параметра - заполняем по дефолту массивы None
            while j < len(main_data):
                data_list.append(None)
                j += 1
            text = file_open.read().split('\n')
            for row in text:
                s_row = row.split(': ')
                key = s_row[0]
                value = s_row[-1].strip()
                k = 0
                # Обеспечиваем заполнение массива в нужном порядке (как идут параметры в main_data)
                while k < len(main_data):
                    if key == main_data[k]:
                        data_list[k+1] = value
                        break
                    k += 1
            res_data.append(data_list)
    return res_data


def write_to_csv_arr(csv_file, *files):

    with open(csv_file, 'w') as csv_file:
        csv_data = get_data_array(*files)
        csv_file_writer = csv.writer(csv_file)
        for line in csv_data:
            csv_file_writer.writerow(line)


# функция для чтения csv в виде списка
def read_csv(csv_file):
    with open(csv_file) as file:
        return list(csv.reader(file))


write_to_csv('test.csv', 'info_1.txt', 'info_2.txt', 'info_3.txt')
write_to_csv_arr('test_array.csv', 'info_1.txt', 'info_2.txt', 'info_3.txt')
assert read_csv('test.csv') == read_csv('test_array.csv'), 'файлы, записанные разными способами, не совпадают!'
