class Body_cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell
        # return 'nooo'
    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            return f'Количество ячеек общей клетки меньше 0'
    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, num_in_row):
        row = str("")
        for i in range(int(self.cell / num_in_row)):
            row += f'{"*" * num_in_row}\\n '
        row += f'{"*" * (self.cell % num_in_row)}'
        return row

a = Body_cell(15)
b = Body_cell(19)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))
print(b.make_order(10))
