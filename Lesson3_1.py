def my_div():
    """ Функция запрашивает ввод двух чисел и выполняет деление одного числа на другое"""
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    while num_2 == 0:
        num_2 = float(input('Делить на ноль нельзя! Введите еще раз второе число: '))
    quot = round((num_1 / num_2), 2)
    return quot
print(my_div())




def my_div_1(n_1, n_2):
    """ Функция принимаент два числа и выполняет деление одного числа на другое"""
    quot = round((n_1 / n_2), 2)
    return quot

n_1 = float(input('Введите первое число: '))
n_2 = float(input('Введите второе число: '))
while n_2 == 0:
    n_2 = float(input('Делить на ноль нельзя! Введите еще раз второе число: '))

print(my_div_1(n_1, n_2))
