# Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False».

arr = [1, 2, 3, 4, 5]  # массив

flag = False

for elem in range(1, len(arr)):
    if arr[elem-1] < arr[elem]:
        flag = True
    else:
        flag = False
        break
print(flag)