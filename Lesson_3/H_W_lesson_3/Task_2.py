# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A [i]. Последняя строка
# содержит число X
check = True
while check:
    list_length = int(input('Введите количество цифр -> '))
    if list_length > 0:
        check = False
    else:
        print('Число должно быть не меньше единицы.')
import random
min_num = 0
max_num = 9
list = []
for i in range(list_length):
    list.append(random.randint(min_num, max_num))
print('Получился такой массив')
print(*list)
number = int(input('Какое число проверить -> '))
nearest = list[0]
for i in list:
    if abs(number - i) < abs(number - nearest):
        nearest = i
    elif (i < number) and ((number - i) == (nearest - number)):
        nearest = i
print(f"Ближайшее число из массива это {nearest}")