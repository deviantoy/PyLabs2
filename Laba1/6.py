# Напишите программу, позволяющую ввести с клавиатуры текст
# предложения и вывести на консоль все символы, которые входят в этот
# текст ровно по одному разу.

text = input('Enter the text: ')
symbol = (text.lower())  # понижение всего текста
for i in range(len(text)):
    if symbol.count(symbol[i]) == 1:  # счётчик символов в тексте. Если встречается 1 раз - на вывод
        print(symbol[i], end=' ')