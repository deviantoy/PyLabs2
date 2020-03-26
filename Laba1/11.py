# Напишите генератор frange как аналог range() с дробным шагом.
# Пример вызова:
#
# for x in frange(1, 5, 0.1):
# print(x)
# # выводит 1 1.1 1.2 1.3 1.4 … 4.9 5.0

def frange(first, last, step):
    while first <= last:
        yield round(first, 1)  # округление до десятых
        first += step

for x in frange(1, 5, 0.1):
    print(x)

# yield - возвращает значение без выхода из функции, или что-то в этом роде