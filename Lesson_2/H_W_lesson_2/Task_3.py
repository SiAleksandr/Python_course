# Требуется вывести все целые степени двойки (т.е. числа
# вида 2 ** k ), не превосходящие числа N.
check = True
while check:
    limit = int(input('Введите предельное число -> '))
    if limit > 0:
        check = False
    else:
        print('Не подходит. Число должно быть не меньше единицы.')
base = 2
power = 0
while (base ** power) <= limit:
    print(base ** power)
    power += 1