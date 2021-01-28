class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print('Сумма первого и второго числа равна')
        return f'SUM = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print('Произведение двух числе равно')
        return f'MUL = {self.a * other.a - (self.b * other.b)} +' \
               f' {self.a * other.b + self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z_1 = Complex(7, -8)
z1 = complex(7, -8)
z_2 = Complex(2, 5)
z2 = complex(2, 5)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(f'Проверка суммирования, сумма равна {z1 + z2}\n ')
print(z_1 * z_2)
print(f'Проверка умножения, произведение равно {z1 * z2}\n ')
