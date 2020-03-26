# Напишите декоратор non_empty, который дополнительно проверяет
# списковый результат любой функции: если в нем содержатся пустые
# строки или значение None, то они удаляются. Пример кода:
# @non_empty
# def get_pages():
#  return ['chapter1', '', 'contents', '', 'line1']

# сам декоратор. Обёртка вокруг функции, которую вызываем
def non_empty(func):
    def dec():
        res = func()
        return list(filter(None, res))

    return dec


@non_empty  # вызов нашего декоратора
def get_pages():
    return [None, 'chapter1', '', 'contents', '', 'line1', None]


print(get_pages())
# декоратор есть обёртка вокруг какой-то функции