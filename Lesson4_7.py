from math import factorial

n = int(input('Введите неотрицательное целое число "n" для получения генератора с 1! до n!: '))

def fact(n):
    """"Функция принимает значение "n" и реализует генератор начиная с 1! и до n!"""
    for el in range(1, n+1):
        yield factorial(el)

for i in fact(n):
    print(i)
