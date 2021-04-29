from method import Method
from gradient_lambda_splitting import SplittingGradient
from normal_gradient import NormalGradient
from fastest_descent import FastestDescent
import random
import matplotlib.pyplot as plt
import numpy as np


def random_matrix(n, k):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = random.randint(1, k)
    i = random.randint(0, n - 1)
    matrix[i][i] = k
    j = i
    while j == i:
        j = random.randint(0, n - 1)
    matrix[j][j] = 1
    # for m in matrix:
    # print(*m)
    return matrix


def func_generation(n, k):
    matrix = random_matrix(n, k)
    func = lambda x: sum(x[i] ** 2 * matrix[i][i] for i in range(n))
    return func


def iterations_by_k(n) -> list:
    # fig, ax = plt.subplots()
    k_i = [[i * 10, 0] for i in range(1, 100)]
    for i in range(1, 5):
        k_i2 = []
        if i == 1:
            for j in range(85, 100):
                k = 10 * j
                method = FastestDescent(func_generation(n, k), 0.001, 100, 0.2,
                                        [random.randint(-10, 10) for _ in range(n)])
                method.run()
                k_i[j - 1][1] += method.iterations
                k_i2.append([k, method.iterations])
                print([k, method.iterations], method.answer)
        else:
            for j in range(1, 100):
                k = 10 * j
                method = FastestDescent(func_generation(n, k), 0.001, 100, 0.2,
                                        [random.randint(-10, 10) for _ in range(n)])
                method.run()
                k_i[j - 1][1] += method.iterations
                k_i2.append([k, method.iterations])
                print([k, method.iterations], method.answer)
    return k_i
    # x0 = k_i[0]
    # for i in range(1, len(k_i)):
    #     x = [x0[0], k_i[i][0]]
    #     y = [x0[1] / 10, k_i[i][1] / 10]
    #     ax.plot(x, y, color='blue')
    #     x0 = k_i[i]
    # plt.show()


f = open('k_i100.txt', 'w')

fig, ax = plt.subplots()
colors = ['blue', 'red', 'gold', 'darkorchid', 'lime']
labels = ['n = 2', 'n = 10', 'n = 100', 'n = 1000', 'n = 10000']

k_i2 = iterations_by_k(100)
f.write(str(k_i2))
# k_i10 = iterations_by_k(10)
# k_i100 = iterations_by_k(100)
# k_i1000 = iterations_by_k(1000)
# k_i10000 = iterations_by_k(10000)
# a = [k_i2, k_i10, k_i100, k_i1000, k_i10000]
# # a = [k_i2, k_i10]
#
# j = 0
# for p in a:
#     x0 = p[0]
#     for i in range(1, len(p)):
#         x = [x0[0], p[i][0]]
#         y = [x0[1] / 10, p[i][1] / 10]
#         ax.plot(x, y, color=colors[j], label=labels[j], linewidth=1)
#         x0 = p[i]
#     j += 1
#
# plt.xlabel("k")
# plt.ylabel("iterations")
# ax.legend()
# fig.set_figheight(10)
# fig.set_figwidth(10)
# plt.show()

# fig, ax = plt.subplots()
# x = [1, 2]
# y = [1, 2]
# ax.plot(x, y, color='lime', label='y=x', linewidth=1)
# plt.xlabel("xlabel")
# plt.ylabel("ylabel")
# ax.legend()
# fig.set_figheight(10)
# fig.set_figwidth(10)
# plt.show()
