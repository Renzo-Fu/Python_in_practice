import numpy as np


class MatrixBase:
    def __init__(self, matrix):
        self._matrix = np.array(matrix)


class ArithmeticMixin:
    def __add__(self, other):
        return AdvancedMatrix(self._matrix + other._matrix)

    def __sub__(self, other):
        return AdvancedMatrix(self._matrix - other._matrix)

    def __mul__(self, other):
        return AdvancedMatrix(self._matrix * other._matrix)

    def __truediv__(self, other):
        # Защита от деления на ноль
        with np.errstate(divide='ignore', invalid='ignore'):
            result = np.true_divide(self._matrix, other._matrix)
            result[np.isinf(result)] = 0
            result = np.nan_to_num(result)
        return AdvancedMatrix(result)


class FileMixin:
    def to_file(self, filename):
        np.savetxt(filename, self._matrix, fmt='%d')


class DisplayAccessMixin:
    def __str__(self):
        return np.array_str(self._matrix)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = np.array(value)


class AdvancedMatrix(MatrixBase, ArithmeticMixin, FileMixin, DisplayAccessMixin):
    pass


np.random.seed(0)
adv_matrix1 = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))
adv_matrix2 = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))


add_result = adv_matrix1 + adv_matrix2
sub_result = adv_matrix1 - adv_matrix2
mul_result = adv_matrix1 * adv_matrix2
div_result = adv_matrix1 / adv_matrix2

add_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.2\\advanced_matrix_add.txt")
sub_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.2\\advanced_matrix_sub.txt")
mul_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.2\\advanced_matrix_mul.txt")
div_result.to_file(
    "C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.2\\advanced_matrix_div.txt")
