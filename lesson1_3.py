num = str(input('Введите число: '))
print(num)
num1 = int(num + num)
num2 = int(num + num + num)
sum1 = int(num) + num1 + num2
print('Вычисление суммы: n + nn + nnn')
print('Сумма {0}+{1}+{2} = ' .format(num, num1, num2) + str(sum1))
