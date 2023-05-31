# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова.
letters = {}
letters[1] = 'AEIOULNSTRАВЕИНОРСТ'
letters[2] = 'DGДКЛМПУ'
letters[3] = 'BCMPБГЁЬЯ'
letters[4] = 'FHVWYЙЫ'
letters[5] = 'KЖЗХЦЧ'
letters[8] = 'JXШЭЮ'
letters[10] = 'QZФЩЪ'
word = input('Введите слово -> ')
word = word.upper()
sum = 0
for item in letters:
    for i in range(len(word)):
        if word[i] in letters[item]:
            sum += item
print(f"Стоимость этого слова -> {sum}")
