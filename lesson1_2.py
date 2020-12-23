time = int(input('Введите пожалуйста время в секундах: '))
h = time // 3600
m = (time // 60) % 60
s = time % 60
print('Время чч:мм:сс')
print('{0}:{1}:{2}' .format(h, m , s))


