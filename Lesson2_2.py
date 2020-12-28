lst = []
print('Введите не менее трех элементов списка')
for i in range(3):
    el = input('Введите элемент списка:')
    lst.append(el)
qst = input('Желаете продолжить ввод? yes/no: ')
if qst == 'yes':
    count = int(input('Сколько еще элементов хотите добавить? '))
    for i in range(count):
        el = input('Введите дополнительный {} элемент списка:'.format(count))
        lst.append(el)
print('Введенный список', lst)
d = 0
for i in range(int(len(lst)/2)):
    lst[d], lst[d+1] = lst[d+1], lst[d]
    d = d +2
print('Измененный список', lst)
