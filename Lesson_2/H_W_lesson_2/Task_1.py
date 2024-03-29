# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
check = True
while check:
    sum_coins = int(input('Введите общее число монет -> '))
    if sum_coins > 0:
        check = False
    else:
        print('Должна быть хотя бы одна монета.')
print('Введите по очереди, какой частью вверх лежит монета. 1 - орёл; 0 - решка')
front = back = 0
for i in range(sum_coins):
    position = int(input())
    if position > 0:
        back += 1
    else:
        front += 1
msg = 'Минимальное число монет, которые нужно перевернуть это '
if back >= front:
    print(msg + f"{front}")
else:
    print(msg + f"{back}")