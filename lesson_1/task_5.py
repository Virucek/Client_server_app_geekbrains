"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""

import subprocess
import chardet

resources = [
    'yandex.ru',
    'youtube.com',
]

for resource in resources:

    args = ['ping', resource]

    proc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in proc_ping.stdout:
        _meta = chardet.detect(line)
        line = line.decode(encoding=_meta['encoding']).encode('utf8')
        print(line.decode('utf8'))
