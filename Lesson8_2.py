class Except:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def exc(self):
        try:
            res = self.num1 / self.num2
        except ZeroDivisionError:
            print('Деление на ноль')
        else:
            print(res)
        finally:
            print('Конец программы')


b = int(input('Введите первое число: '))
c = int(input('Введите второе число: '))
a = Except(b, c)
a.exc()
