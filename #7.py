x1 = int(input('Координата x1: '))
y1 = int(input('Координата y1: '))
x2 = int(input('Координата x2: '))
y2 = int(input('Координата y2: '))

if 1 <= x1 <=8 and 1 <= x2 <=8 and 1 <= y1 <=8 and 1 <= y2 <=8:
    if y2 - y1==2 and x2 - x1 == 1: # вверх влево
        print('YES')
    elif y2 - y1==2 and x1 - x2 == 1: # вверх вправо
        print('YES')
    elif y1 - y2==2 and x2 - x1 == 1: # вниз влево
        print('YES')
    elif y1 - y2==2 and x1 - x2 == 1: # вниз вправо
        print('YES')
    elif x2 - x1==2 and y2 - y1 == 1: # влево вверх
        print('YES')
    elif x2 - x1==2 and y1 - y2 == 1: # влево вниз
        print('YES')
    elif x1 - x2==2 and y2 - y1 == 1: # вправо вверх
        print('YES')
    elif x1 - x2==2 and y1 - y2 == 1: # вправо вниз
        print('YES')
    else:
        print("NO")

else:
    print('Ошибка')