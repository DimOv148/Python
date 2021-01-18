with open("les5_3.txt", "r", encoding='utf-8') as f:
    s = []
    p = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000.00:
            p.append(i[0])
        s.append(i[1])
print(f'Сотрудники, имеющие заработную плату менее 20 000 руб. : {p}')
print(f'Средняя заработная плата составляет: {(sum(map(float, s)) / len(s)):.2f} рубля')
