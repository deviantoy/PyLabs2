import argparse
import ffmpeg
import subprocess
import os
import glob
import random

"""
Написать скрипт trackmix.py, который формирует обзорный трек-микс
альбома (попурри из коротких фрагментов mp3-файлов в
пользовательской директории). Для манипуляций со звуковыми
файлами можно использовать сторонние утилиты, например, FFmpeg.
Пример вызова и работы скрипта:
trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e
--- processing file 1: 01 - Intro.mp3
--- processing file 2: 02 - Outro.mp3
--- done!
Параметры скрипта:
--source (-s) – имя рабочей директории с треками, обязателен;
--destination (-d) – имя выходного файла, необязателен (если не указан,
то имя выходного файла – mix.mp3 в директории source);
--count (-c) – количество файлов в "нарезке", необязателен (если он не
указан, то перебираются все mp3-файлы в директории source);
--frame (-f) – количество секунд на каждый файл, необязателен (если не
указан, скрипт вырезает по 10 секунд из произвольного участка каждого
файла);
--log (-l) – необязательный ключ (если этот ключ указывается, то скрипт
должен выводить на консоль лог процесса обработки файлов, как в
примере);
--extended (-e) – необязательный ключ (если этот ключ указывается, то
каждый фрагмент попурри начинается и завершается небольшим
fade in/fade out). (Как я понял - затуханием и оттуханием (XD))
"""

"""
trackmix --source "E:/Python/Laba2/Music_For_ex7" --count 5 --frame 15 -l True -e False
"""

parser = argparse.ArgumentParser(description='Parser for Exercise 6')
parser.add_argument('-s', '--source', type=str, default=None, required=True)
parser.add_argument('-d', '--dest', type=str, default=None)
parser.add_argument('-c', '--count', type=int, default=None)
parser.add_argument('-f', '--frame', type=int, default=10)
parser.add_argument('-l', '--log', type=bool, default=False)
parser.add_argument('-e', '--extended', type=bool, default=False)
my_parser = parser.parse_args()


def isNone(smth):
    return True if smth is None else False


path = ''
destination_name = ''
countInt = None
frameInt = None
logBool = False
extendedBool = False


def check_all_variables(src, dst, cnt, frame, logs, extended):
    global path, destination_name, countInt, frameInt, logBool, extendedBool
    if isNone(src):
        print('No path')
    else:
        if isNone(dst):
            destination_name = src + 'mix.mp3'
        else:
            destination_name = dst

        if not isNone(cnt):
            countInt = cnt
        else:
            countInt = len(os.listdir(src))

        if not isNone(frame):
            frameInt = frame
        else:
            pass

        if isNone(logs):
            pass
        else:
            logBool = True

        if isNone(extended):
            pass
        else:
            extendedBool = True


def track_mix():
    check_all_variables(my_parser.source, my_parser.dest, my_parser.count, my_parser.frame, my_parser.log,
                        my_parser.extended)

    tracklist = list(glob.glob((os.path.join(my_parser.source, '*.mp3')).replace('\\\\', '/')))
    print(tracklist)


track_mix()