# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
minNum = 100000
maxNum = 999999
check = True
while check:
    num = int(input('Введите шестизначный номер билета -> '))
    if num < minNum or num > maxNum:
        print('Это не шестизначное число.')
    else:
        check = False
leftPart = 0
rightPart = 0
temp = num
half = 3
lastValue = -half
while half > lastValue:
    if half > 0:
        rightPart += temp % 10
    else:
        leftPart += temp % 10
    temp = temp // 10
    half -= 1
if rightPart == leftPart:
    print (f"{num} - Это счастливый билет!")
else:
    print (f"Нет, {num} это не счастливый билет.")
