# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
check = True
while check:
    oneSide = int(input('Введите, сколько долек в одной стороне -> '))
    otherSide = int(input('Введите, сколько долек в другой стороне -> '))
    desired = int(input('Введите, сколько долек отломить -> '))
    if oneSide > 0 and otherSide > 0 and desired > 0:
        check = False
    else:
        print('Где-то введено недопустимое число. Попробуйте снова.')
if (desired // oneSide > 0) and (desired % oneSide == 0):
    if desired < oneSide * otherSide:
        check = True
    else:
        check = False
elif (desired // otherSide > 0) and (desired % otherSide == 0):
    if desired < otherSide * oneSide:
        check = True
    else:
        check = False
else:
    check = False
if check == True:
    print('Да, от такой шоколадки можно отломить столько долек, сделав один ровный разлом.')
else:
    print('Нет, от такой шоколадки нельзя отломить столько долек, сделав один ровный разлом.')



