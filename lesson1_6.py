a = int(input('Введите дистанцию пробежки в первый день, км:  '))
b = int(input('Введите финальную дистанцию пробежки, км:  '))
count = 1
print('{0}-й день {1} км'.format(count, a))
while a <= b:
    count = count + 1
    a = a + a*0.1
    print('{0}-й день {1:.2f} км'.format(count, a))
print('Результат будет достигнут на ',count, 'день')
