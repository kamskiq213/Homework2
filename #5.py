a = int(input('День недели: '))

if 1 <= a <=5:
    print('Будни')
elif 6 <= a <= 7:
    print('Выходные')
else:
    print('Ошибка')