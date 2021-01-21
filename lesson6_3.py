class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    # def __init__(self, name, surname, position, wage, bonus):
        # Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


a = Position('Ivan', 'Aleksevich', 'layer', 12500, 100500)

a.get_full_name()
a.get_total_income()

print(a.position)
print(a._income)
