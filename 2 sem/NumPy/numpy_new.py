import numpy as np

matrix = np.array([1, 34, 6, 345, 788, 132, 39627])


def task_1(matrix_1, k):
    return matrix_1[matrix_1 % k != 0]


print(task_1(matrix, 3))


def task_2(matrix_2):
    return np.where(matrix_2 % 2 == 0, matrix_2 // 2, matrix_2)


print(task_2(matrix))


matrix_3 = np.arange(2, 101)


def task_3(matrix_3):

