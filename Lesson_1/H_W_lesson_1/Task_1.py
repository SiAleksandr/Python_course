# Найдите сумму цифр трехзначного числа.
min = 100
max = 999
check = True
while check:
    num = int(input('Введите трёхзначное число -> '))
    if num < min or num > max:
        print('Неподходящее число, введите другое')
    else:
        check = False
sum = 0
temp = num
while temp > 0:
    sum = sum + temp % 10
    temp = temp // 10
print(f"Сумма цифр числа = {sum}")
