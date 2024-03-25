
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __add__(self, other):
        if self.matrix.shape != other.matrix.shape:
            raise ValueError(
                "Matrices must have the same dimensions for addition")
        return Matrix(self.matrix + other.matrix)

    def __mul__(self, other):
        if self.matrix.shape != other.matrix.shape:
            raise ValueError(
                "Matrices must have the same dimensions for component-wise multiplication")
        return Matrix(self.matrix * other.matrix)

    def __matmul__(self, other):
        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise ValueError(
                "The number of columns in the first matrix must be equal to the number of rows in the second matrix for matrix multiplication")
        return Matrix(self.matrix @ other.matrix)

    def to_file(self, filename):
        np.savetxt(filename, self.matrix, fmt='%d')


np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Выполнение операций
add_result = matrix1 + matrix2
mul_result = matrix1 * matrix2
matmul_result = matrix1 @ matrix2


add_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.1\\matrix+.txt")
# Изменили имя файла
mul_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.1\\matrixx.txt")
matmul_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.1\\matrix@.txt")
