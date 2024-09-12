a = int(input('Введите время: '))

if 4 < a < 12:
    print('Утро')
elif 11 < a < 18:
    print('День')
elif 17 < a < 23 :
    print('Вечер')
elif 22< a < 25 or 0 <= a <= 4:
    print('Ночь')
else:
    print('Ошибка')