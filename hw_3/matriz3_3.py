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


class HashableMixin:
    def __hash__(self):
        # Хэш-функция: суммируем все элементы матрицы, добавляем произведение размеров и берём остаток от деления на большое простое число
        return int(np.sum(self.matrix) + self.matrix.shape[0] * self.matrix.shape[1]) % 104729


class HashableMatrix(HashableMixin, Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)
    # Кэширование результатов матричного умножения
    _cache = {}

    def __matmul__(self, other):
        hash_pair = hash(self), hash(other)
        if hash_pair in self._cache:
            return self._cache[hash_pair]
        result = super().__matmul__(other)
        self._cache[hash_pair] = result
        return result


def find_collision():
    np.random.seed(0)
    hashes = {}
    while True:
        new_matrix = HashableMatrix(np.random.randint(0, 10, (10, 10)))
        new_hash = hash(new_matrix)
        if new_hash in hashes:
            if not np.array_equal(new_matrix.matrix, hashes[new_hash].matrix):
                return new_matrix, hashes[new_hash]
        else:
            hashes[new_hash] = new_matrix


A, C = find_collision()
B = HashableMatrix(np.random.randint(0, 10, (10, 10)))
D = B

AB = A @ B
CD = C @ D

# Сохранение результатов
A.to_file("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\A.txt")
B.to_file("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\B.txt")
C.to_file("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\C.txt")
D.to_file("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\D.txt")
AB.to_file("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\AB.txt")
CD.to_file("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\CD.txt")

with open("C:\\Users\\renz_\\Python_course\\hw_3\\artifacts\\3.3\\hash.txt", "w") as f:
    f.write(f"Hash of AB: {hash(AB)}\n")
    f.write(f"Hash of CD: {hash(CD)}\n")
