lst = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))
lst.append(a)
print(sorted(lst, reverse=True))

# ну или если действительно вводимую цифру необходимо подставить на определенное место
lst_1 = [7, 5, 3, 3, 2]
b = int(input('Введите число: '))
for i in range(len(lst_1)):
    if lst_1[0] < b:
        lst_1.insert(0, b)
    elif lst_1[-1] > b:
        lst_1.append(b)
    elif lst_1[i] > b and lst_1[i + 1] < b:
        lst_1.insert(i+1, b)
print(lst_1)








