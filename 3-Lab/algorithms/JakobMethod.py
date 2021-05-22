import math
import copy
import time
from random import choice
from numpy import linalg as la
from numpy import array
from matplotlib import pyplot as plt
from random import randint
from scipy.sparse import csr_matrix

from gauss_method import GaussMethod
from matrix import Matrix

aij = [0, -1, -2, -3, -4]
n_arr = [10, 50, 100, 150, 175, 200]


def getF(a: csr_matrix, x: array) -> array:
    return a.dot(x)


def getDiagonalMatrix(n: int) -> csr_matrix:
    matrix = array([array([-1.] * n) for _ in range(n)])
    s = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            matrix[i][j] = choice(aij)
            s += matrix[i][j]
    for i in range(n):
        matrix[i][i] = -s + 10**(-n) + randint(1, 10000)
    return csr_matrix(matrix)


def getGilbertMatrix(n: int) -> csr_matrix:
    matrix = array([array([-1.] * n) for _ in range(n)])
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1 / ((i + 1) + (j + 1) - 1)
    return csr_matrix(matrix)


# Проверка матрицы коэффициентов на корректность
def isCorrectArray(a: csr_matrix, b: array):
    for row in range(0, len(a.toarray())):
        if len(a.toarray()) != len(b):
            print('Не соответствует размерность')
            return False

    for row in range(0, len(a.toarray())):
        if a[row, row] == 0:
            print('Нулевые элементы на главной диагонали')
            return False
    return True


# Условие завершения программы на основе вычисления
# расстояния между соответствующими элементами соседних
# итераций в методе решения
def isNeedToComplete(x_old, x_new):
    eps = 0.0001
    # sum_up = 0
    # sum_low = 0
    # for k in range(0, len(x_old)):
    #     sum_up += (x_new[k] - x_old[k]) ** 2
    #     sum_low += (x_new[k]) ** 2
    # print(math.sqrt(sum_up / sum_low))
    # return math.sqrt(sum_up / sum_low) < eps
    return getDiff(x_old, x_new) < eps

# Процедура решения
def solution(a: csr_matrix, b: array) -> list:
    if (not isCorrectArray(a, b)):
        print('Ошибка в исходных данных')
    else:
        count = len(b)  # количество корней
        x = array([1.] * count)

        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = 100  # максимально допустимое число итераций
        while (numberOfIter < MAX_ITER):
            x_prev = array(x)
            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if j != k:
                        S = S + a[k, j] * x_prev[j]
                x[k] = b[k] / a[k, k] - S / a[k, k]
            if isNeedToComplete(x_prev, x):  # проверка на выход
                break

            numberOfIter += 1

#        print('Количество итераций на решение: ', numberOfIter)

        return [x, numberOfIter]


def getDiff(x1: array, x2: array) -> float:
    x = array([-1.] * len(x1))
    for i in range(len(x)):
        x[i] = x2[i] - x1[i]
    return la.norm(x)


if __name__ == '__main__':
    # # a = array([[10, -3, -2], [-1, 10, -1], [-1, -2, 10]])
    # # f = array([-2, 16, 25])
    # # solution = solution(a, f)
    # # answer = solution[0]
    # # it = solution[1]
    # # print('------')
    # # print("Ax: ", a.dot(answer))
    # # print("distance to the real answer:", getDiff(answer, [1, 2, 3]))
    # # print("answer:", answer)
    # # print("iterations:", it)
    # fir, ax = plt.subplots()
    # for n in n_arr:
    #     # for i in range(3):
    #         # matrix = getDiagonalMatrix(n)
    #     matrix = getDiagonalMatrix(n)
    #     _x = array([i for i in range(1, n + 1)])
    #     F = getF(matrix, _x)
    #     start_time = time.time()
    #     sol = solution(matrix, F)
    #     answer = sol[0]
    #     iterations = sol[1]
    #     # k = la.cond(matrix.toarray())
    #     # diff = getDiff(answer, _x)
    #     result_time = time.time() - start_time
    #     print("n:", n, "time:", result_time)
    #     # print("disctance:", diff, "answer:", answer)
    #     # print("n:", n, "iteration:", iterations)
    #     ax.scatter(n, result_time, color='blue')
    # plt.show()

    fir, ax = plt.subplots()
    for n in n_arr:
        matrix = getDiagonalMatrix(n)
        _x = array([i for i in range(1, n + 1)])
        F = getF(matrix, _x)
        start_time = time.time()
        sol = solution(matrix, F)
        result_time2 = time.time() - start_time
        # NewMatrix = Matrix(matrix.toarray())
        # start_time = time.time()
        # NewMatrix.LU_Decompose()
        # gauss = GaussMethod(NewMatrix, csr_matrix(F))
        # gauss.run()
        # result_time1 = time.time() - start_time
        # print("n:", n, "time:", result_time1, result_time2)
        print(getDiff(sol[0], _x))
        # ax.scatter(n, result_time1, color='blue')
        ax.scatter(n, result_time2, color='red')
    plt.show()


