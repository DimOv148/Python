num = int(input('Введите целое положительное число: '))
mx = num % 10
num = num // 10
while num > 0:
    if num % 10 > mx:
        mx = num % 10
    num = num // 10
print('Наибольшая цифра в числе', mx)
