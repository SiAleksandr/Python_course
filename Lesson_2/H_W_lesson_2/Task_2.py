# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
check = True
limit = 2000
minimum = 1
while check:
    sum = int(input('Введите сумму чисел -> '))
    multiply = int(input('Введите произведение этих чисел -> '))
    if sum > limit:
        print('Слишком большие числа. Введите другие.')
    elif (sum < minimum) or (multiply < minimum):
        print('Числа должны быть натуральными. Введите другие.')
    else:
        check = False
if (sum ** 2 - 4 * multiply) < 0:
    print('Не существует чисел, подходящих под данные условия.')
else:
    first_num = (sum - (sum ** 2 - 4 * multiply) ** 0.5) / 2
    second_num = sum - first_num
    first_num = int(first_num)
    second_num = int(second_num)
    if first_num + second_num == sum:
        print(f"Эти числа {first_num} и {second_num}")
    else:
        print('Нет натуральных чисел, подходящи под данные условия.')
