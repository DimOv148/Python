class Organisation:
    """""Основной класс организации"""
    def __init__(self, dep_name):
        self.dep_name = dep_name

    def __str__(self):
        return f'{self.dep_name}'


class Departments(Organisation):
    """"Класс подразделений организации и находящейся в них техники"""
    def __init__(self, dep_name):
        Organisation.__init__(self, dep_name)
        self.equipment = []

    def take(self, subj):
        self.equipment.append(subj)


class Warehouse(Organisation):
    """"Класс описывающий работу склада"""
    def __init__(self, dep_name):
        Organisation.__init__(self, dep_name)

    def to_give(self, subj, *departmets):
        for department in departmets:
            department.take(subj)

    @staticmethod
    def receipt():
        my_list = []
        while True:
            try:
                a = input('Введите назавание устройства: ')
                b = int(input('Введите цену стройства: '))
                c = int(input('Введите количество устройств: '))
                el = {'Тип устройства': a, 'Цена': b, 'Количество': c}
                my_list.append(el)
            except ValueError:
                print('Введены неверные данные')
            print('Для выхода - Q, продолжение - Enter')
            q = input('=> ')
            if q == 'Q' or q == 'q':
                print(f'Список оргтехники на складе:\n {my_list}\n')
                return 'Выход'


class Equipment:
    """"Класс хранящий в себе список оборудования
        передаваемого в подразделения"""
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def get_subjects(self):
        return self.subjects


class OfficeEquipment:
    """"Родительский класс для офисной техники"""
    def __init__(self, name, size, weight, cost):
        self.name = name
        self.size = size
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f'Наименование устройства: {self.name}, ' \
               f' Размер: {self.size}, ' \
               f'Вес: {self.weight}, Цена: {self.cost}'


class Printer(OfficeEquipment):
    """"Класс описывающий параметры принтеров"""
    def __init__(self, name, size, weight, cost, *properties):
        OfficeEquipment.__init__(self, name, size, weight, cost)
        self.properties = list(properties)

    def get_properties(self):
        return f'Дополнительные параметры устройства: {self.properties}'

    def get_run(self):
        return f'У "{self.name}" дополнительно' \
               f' {len(self.properties)} параметра(ов)\n'


class Scan(OfficeEquipment):
    """"Класс описывающий параметры сканеров"""
    def __init__(self, name, size, weight, cost, *properties):
        OfficeEquipment.__init__(self, name, size, weight, cost)
        self.properties = list(properties)

    def get_properties(self):
        return f'Дополнительные параметры устройства: {self.properties}'

    def get_run(self):
        return f'У "{self.name}" дополнительно ' \
               f'{len(self.properties)} параметра(ов)\n'


class Xerox(OfficeEquipment):
    """"Класс описывающий параметры копировальных станций"""
    def __init__(self, name, size, weight, cost, copy, *properties):
        OfficeEquipment.__init__(self, name, size, weight, cost)
        self.properties = list(properties)
        self.copy = copy

    def get_properties(self):
        return f'Дополнительные параметры устройства: {self.properties}'

    def get_run(self):
        return f'"{self.name}" выполнил {self.copy} копий \n'


prn = Printer('Принтер', 'Big', 15, 456, 'laser',
              'double_side', 'color', '1500 copy/hour')
print(prn)
print(prn.get_properties())
print(prn.get_run())

sc = Scan('Сканер', 'Portable', 1, 324, 'a4', 'negative + positive',
          'double_side', 'color', '150 scan/hour')
print(sc)
print(sc.get_properties())
print(sc.get_run())

xr = Xerox('Копировальный автомат', 'Prom', 150, 1324, 6254,
           'a3', 'double_side', 'color', '1500 copy/hour')
print(xr)
print(xr.get_properties())
print(xr.get_run())

Warehouse.receipt()

ware = Warehouse('Warehouse')
acc = Departments('Accounts')
sel = Departments('Sales')
aho = Departments('Administration')

sb = Equipment('printer', 'scaner', 'xerox')
ware.to_give(sb.get_subjects(), acc, sel)

sb = Equipment('PC')
ware.to_give(sb.get_subjects(), aho, acc)

print('Список оргтехники хранящейся в подразделениях: ')
print(acc, acc.equipment)
print(sel, sel.equipment)
print(aho, aho.equipment)
