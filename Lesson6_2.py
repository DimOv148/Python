class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self):
        thick_coat = int(input('Введите желаемую толщину дорожного покрытия в см: '))
        # mas_per_sq_met - постоянная равная удельному весу 1 кв. метра асфальта толщиной 1 см в кг.
        mas_per_sq_met = 25
        return mas_per_sq_met * thick_coat * self._lenght * self._width


m4 = Road(20, 5000)
print(f' Масса асфальта автодороги равна {m4.mass()} кг.\n')

m11 = Road(30, 15000)
print(f' Масса асфальта автодороги равна {m11.mass()} кг.')

print('------------------------------------------------------')
class Road_new:

    def __init__(self, lenght, width, std_road):
        self._lenght = lenght
        self._width = width
        self.std_road = std_road

    def mass(self):
        return self._lenght * self._width * self.std_road


m4 = Road_new(20, 5000, 125)
print(f' Масса асфальта автодороги равна {m4.mass()} кг.\n')

m11 = Road_new(30, 15000, 125)
print(f' Масса асфальта автодороги равна {m11.mass()} кг.\n')
m11.std_road = 100
print(f' Масса асфальта автодороги при новой удельной массе\n 1 кв. метра асфальта (100) равна {m11.mass()} кг.')