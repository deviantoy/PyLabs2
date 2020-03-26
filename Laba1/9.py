# Напишите программу, имитирующую работу банкомата. Выберите
# структуру данных для хранения купюр разного достоинства в заданном
# количестве. При вводе пользователем запрашиваемой суммы денег,
# скрипт должен вывести на консоль количество купюр подходящего
# достоинства. Если имеющихся денег не хватает, то необходимо
# напечатать сообщение «Операция не может быть выполнена!».
# Например, при сумме 5370 рублей на консоль должно быть выведено
# «5*1000 + 3*100 + 1*50 + 2*10».

def cashDispenser():
    money_in_stock = {1000: 2, 500: 2, 200: 10, 100: 5, 50: 5, 10: 20}
    result = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 10: 0}
    money = 5370
    for key in money_in_stock.keys():
        current = money // key  # деление без остатка
        if current > money_in_stock[key]:
            money = money - (money_in_stock[key] * key)
            result[key] = money_in_stock[key]
        else:
            money = money % key
            result[key] = current
    print("Your money : " + str(sum([k * v for k, v in zip(result.keys(), result.values())])))
    print(result)


cashDispenser()