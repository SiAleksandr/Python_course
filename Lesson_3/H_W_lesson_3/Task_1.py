# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A[i]. Последняя строка содержит число X
check = True
while check:
    list_length = int(input('Введите количество цифр -> '))
    if list_length > 0:
        check = False
    else:
        print('Число должно быть не меньше единицы.')
import random
min_mum = 0
max_num = 9
list = []
for i in range(list_length):
    list.append(random.randint(min_mum, max_num))
print('Получился такой массив')
print(*list)
number = int(input('На какое число проверить -> '))
count = 0
for i in list:
    if i == number:
        count += 1
print(f"Вот сколько раз встречается это число -> {count}")
