import numpy as np


def task_10x10(line, column):
    matrix = np.zeros((line, column))
    matrix_1 = np.ones((1, column))
    matrix[0] = matrix_1
    return matrix


print(task_10x10(10, 10))


def task_border(line, column):
    matrix = np.zeros((line, column))
    matrix_1 = np.ones((1, column))
    matrix[0], matrix[-1] = matrix_1, matrix_1
    for i in range(1, line - 1):
        matrix[i][0], matrix[i][-1] = 1., 1.
    return matrix


print(task_border(10, 10))


def task_2_5x5_1(line, column):
    matrix = np.ones((line, column))
    another_matrix = np.ones((line, column))
    return matrix + another_matrix


print(task_2_5x5_1(5, 5))


def task_2_5x5_2(line, column):
    matrix = np.ones((line, column)) * 2
    return matrix


print(task_2_5x5_2(5, 5))


def task_0123():
    matrix_0 = np.zeros((5, 5))
    matrix_1 = np.ones((5, 5))
    matrix_2 = np.ones((5, 5)) * 2
    matrix_3 = np.ones((5, 5)) * 3
    matrix_01 = np.hstack((matrix_0, matrix_1))
    matrix_23 = np.hstack((matrix_2, matrix_3))
    matrix_0123 = np.vstack((matrix_01, matrix_23))

    return matrix_0123


print(task_0123())


def task_chess(line, column):
    matrix = np.zeros((line, column))
    for i in range(line):
        for j in range(column):
            if (i + j) % 2 != 0:
                matrix[i][j] = 1.
    return matrix


print(task_chess(10, 10))


def task_1_to_9_lines(line, column):
    matrix = np.ones((line, column))
    for i in range(1, line):
        matrix[i] = i + 1
    return matrix


print(task_1_to_9_lines(9, 9))


def task_1_to_100(line, column):
    matrix = np.ones((line, column))
    for i in range(line):
        for j in range(column):
            matrix[i][j] = i * 10 + j + 1
    return matrix


print(task_1_to_100(10, 10))


def task_multiplication_table(line, column):
    matrix = np.ones((line, column))
    for i in range(line):
        for j in range(column):
            matrix[i][j] = (i + 1) * (j + 1)
    return matrix


print(task_multiplication_table(9, 9))


def task_3_diags(n, a, b):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = a
            if i == j + 1 or j == i + 1:
                matrix[i][j] = b
    return matrix


print(task_3_diags(9, 7, 2))


def task_double_chess(line, column):
    matrix = np.ones((line, column))
    for i in range(0, line, 4):
        for j in range(0, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(0, line, 4):
        for j in range(1, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(1, line, 4):
        for j in range(0, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(1, line, 4):
        for j in range(1, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(2, line, 4):
        for j in range(2, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(2, line, 4):
        for j in range(3, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(3, line, 4):
        for j in range(2, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    for i in range(3, line, 4):
        for j in range(3, column, 4):
            matrix[i][j] = 0.
            matrix[i][j] = 0.
    return matrix


print(task_double_chess(20, 20))


def task_chukh(n):
    matrix = np.ones((n, n))
    for i in range(n):
        if i % 2 != 0:
            matrix[i:, i:] = 2
        else:
            matrix[i:, i:] = 1
    return matrix


print(task_chukh(5))
