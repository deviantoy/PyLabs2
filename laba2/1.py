# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать).

file = open('task1_file.txt', 'r')
text = file.read()
file.close()
s = '!@#№$%^&*(),.:;?/|"[]+_-'
vocabulary = {letter: text.count(letter) for letter in text if letter not in s}
for key in sorted(vocabulary.keys(), key=vocabulary.get, reverse=True):
    print(key, ': ', vocabulary[key])

