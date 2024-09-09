number1 = int(input("Введите делимое число: "))
number2 = int(input("Введите делитель: "))
if number2 == 0:
    print('На 0 делить нельзя')
elif number1 % number2 == 0:
    print(f'Число {number1} кратно числу {number2}')
else:
    print(f'Число {number1} не кратно числу {number2}')