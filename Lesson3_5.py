sum_list = []
while True:
    c = input('Программа вычисления суммы. Для продолжения нажмите Enter, для выхода нажмите Q: ').upper()
    if c == 'Q':
        break
    num_list = input('Введите числа через пробел или введите любой символ для выхода: ').split()
    for num in num_list:
        try:
            num = int(num)
            sum_list.append(num)
        except ValueError:
            print('Вычисления окончены, попробуйте еще раз! ')
            break
    print(f'Введенные числа {sum_list}')
    sum_all = sum(sum_list)
    print(f'Сумма введенных чисел = {sum_all}')
