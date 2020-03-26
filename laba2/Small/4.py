# Напишите скрипт, который позволяет ввести с клавиатуры имя
# текстового файла, найти в нем с помощью регулярных выражений все
# подстроки определенного вида, в соответствии с вариантом.
# Вариант 8:найдите все логические выражения – подстроки вида
# «x&&y», «x&y», где х и у – любые слова. Количество пробелов может
# быть также любым

import re  # либа для регулярок



pattern = re.compile(r"[a-zA-Z]+&{1,3}[a-zA-Z]+")
content = ''
matches = []
path = input('Введите название вашего файла: ')
try:
    file = open('C:\\Users\\artem\\PycharmProjects\\laba2\\' + path, 'r', encoding='UTF-8')
    content = file.read().replace('\n', ' ')
    file.close()
except FileNotFoundError as e:
    print('File does not exist. ', e.args)

print(content)

result = re.findall(pattern, content)
print(result)