a = int(input('Сторона 1: '))
b = int(input('Сторона 2: '))
c = int(input('Сторона 3: '))

if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')

