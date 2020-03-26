
# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен

import os
from glob import glob
import os.path

path = 'C:\\Users\\artem\\PycharmProjects\\laba2\\Task3'
os.chdir(path)
trackFiles = glob('*.mp3')

namesFiles = list(filter(None, [text.replace('\n', '') if text is not 'fileLists.txt' else None for text in
                                open('fileLists.txt', 'r', encoding='UTF-8')]))

cnt = 0
Done = False

for i in range(len(trackFiles)):
    try:
        os.rename(trackFiles[i], namesFiles[i])
        if cnt == len(trackFiles) - 1:
            Done = True
        cnt += 1
    except Exception as e:
        print('Some error with file #' + str(cnt) + ': ', e.args)

if Done:
    print('All files renamed!')
else:
    print('oh shit, here we got some errors!')