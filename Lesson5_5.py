with open("les5_5.txt", "w", encoding='utf-8') as f:
    from random import randint
    my_list = " ".join([str(randint(0, 30)) for i in range(15)])
    print(f' Произвольные числа записанные в файл {my_list}')
    f.write(my_list)

with open("les5_5.txt", "r", encoding='utf-8') as f:
    sum_list = []
    my_list = f.read().split(' ')
    for i in my_list:
        i = int(i)
        sum_list.append(i)
    print(f'Числа загруженные из файла {sum_list}')
print(f'Сумма введенных чисел равна {sum(sum_list)}')
