import numpy as np
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):

        # matrix = [[0, 0], [0, 0]]
        # for i in range(len(self.list_1)):
        #     for j in range(len(self.list_1[0])):
        #         matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        # return str('\n'.join('\t'.join(str(el) for el in row) for row in matrix))
        matrix_1 = np.array(self.list_1)
        matrix_2 = np.array(self.list_2)
        matrix = matrix_1 + matrix_2
        return str('\n'.join('\t'.join(str(el) for el in row) for row in matrix))



    def __str__(self):
        print('Первая матрица')
        print(str('\n'.join('\t'.join(str(el) for el in row) for row in self.list_1)))
        print('Вторая матрица')
        print(str('\n'.join('\t'.join(str(el) for el in row) for row in self.list_2)))


my_mtx = Matrix([[5, 10], [15, 20]], [[1, 2], [3, 4]])
my_mtx.__str__()
print(f'Сумма двух матриц \n {my_mtx.__add__()}')