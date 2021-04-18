from fastest_descent import FastestDescent
from normal_gradient import NormalGradient
from gradient_lambda_splitting import SplittingGradient
from algorithms import plot


def func(x: list) -> float:
    return 2 * x[0]**2 + 4 * x[1]**2 - 5 * x[0] * x[1] / 2 - 3 * x[1]
    #return x[0] ** 2 + x[1] ** 2


# # Fastest descent test
# method = FastestDescent(func, 0.001, 100, 0.2, [12, -2])
# method.run()
# print(method.answer)
# print(method.answer_point)
# print(method.segments)
# print('steps:', method.iterations)
# plot.plot_and_show(method)
#
# # Gradient with static lambda test
# method = NormalGradient(func, 0.001, 100, 0.2, [18, -17])
# method.run()
# print(method.answer)
# print(method.answer_point)
# print(method.segments)
# print('steps:', method.iterations)
# plot.plot_and_show(method)

method = SplittingGradient(func, 0.001, 100, 0.5, [18, -17])
method.run()
print(method.answer)
print(method.answer_point)
print(method.segments)
print('steps:', method.iterations)
#plot.plot_and_show(method)


#a = [ func(x[])/ for x in method.segments]


