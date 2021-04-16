from fastest_descent import FastestDescent
from normal_gradient import NormalGradient
import plot


def func(x: list) -> float:
    return 2 * x[0]**2 + 4 * x[1]**2 - 5 * x[0] * x[1] / 2 - 3 * x[1]
    #return x[0] ** 2 + x[1] ** 2


# Fastest descent test
method = FastestDescent(func, 0.001, [12, -2])
method.run()
print(method.answer)
print(method.answer_point)
print(method.segments)
plot.plot_and_show(method)
#
# # Gradient with static lambda test
# method = NormalGradient(func, 0.001, [4, 3])
# method.run()
# print(method.answer)
# print(method.answer_point)
# print(method.segments)
# plot_and_show(method)