from itertools import count, cycle

cnt = int(input('Введите стартовое число: '))
print('Генерация чисел закончится через 10 циклов')
for el in count(cnt):
    if el == cnt + 10:
        break
    else:
        print(el)

my_list = ['ABC', '12', 15]
cnt_1 = int(input('Введите количество повторений элементов списка: '))
for ell in cycle(my_list):
    if cnt_1 == 0:
        break
    else:
        print(ell)
        cnt_1 -= 1