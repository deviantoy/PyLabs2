import re
import string
"""
Введите с клавиатуры текст. Программно найдите в нем и выведите
отдельно все слова, которые начинаются с большого латинского
символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
«Petr93», «Johnny70», «Service2002». Используйте регулярные
выражения.
"""

"""
Пример текста:
Sometext1233 sadasd777 Dadya6111 Zachtitelabuplz000
"""

upper_letters = string.ascii_uppercase
pattern = re.compile(r"[A-Z][a-z]{1,}(?:\d{4}$|\d{2}$)")
text = input('Enter the text: ')

result = re.findall(pattern, text)
print(str(result))