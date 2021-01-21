class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):

    def __init__(self, title,):
        Stationery.__init__(self, title)

    def draw(self):
        Stationery.draw(self)
        print(f'Вы рисуете {self.title}')

class Pencil(Stationery):

    def __init__(self, title,):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Вы рисуете {self.title}')

class Handle(Stationery):

    def __init__(self, title,):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Вы рисуете {self.title}')

pn = Pen('Ручка')
pn.draw()
print('------------------------------')
pns = Pencil('Карандаш')
pns.draw()
print('------------------------------')
main = Stationery('')
main.draw()
hnd = Handle('Маркер')
hnd.draw()