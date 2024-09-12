number = int(input('Введите число: '))

if number == 0:
    print('Ноль')
elif number > 0:
    if number % 2==0:
        print('Положительное четное')
    else:
        print('Положительное нечетное')
elif number < 0:
    if number % 2==0:
        print('Отрицательное четное')
    else:
        print('Отрицательное нечетное')