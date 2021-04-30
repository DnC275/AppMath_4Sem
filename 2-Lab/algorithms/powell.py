from method import Method
from scipy import optimize
import utils


class Powell(Method):
    def run(self):
        x = self.x0[:]
        n = 2
        d = [[1, 0], [0, 1]]
        while True:
            new_func = lambda _lambda: self.function(utils.get_list_sum(x, utils.multiply_list_by_number(d[n - 1], _lambda))) # 2
            _lambda = optimize.minimize(new_func, x0=0)["x"][0]
            x = utils.get_list_sum(x, utils.multiply_list_by_number(d[n - 1], _lambda)) # 3
            y = x[:]
            i = 1
            while i < n + 1: # 4, 5, 6
                new_func = lambda _lambda: self.function(utils.get_list_sum(x, utils.multiply_list_by_number(d[i - 1], _lambda)))
                _lambda = optimize.minimize(new_func, x0=0)["x"][0]
                x = utils.get_list_sum(x, utils.multiply_list_by_number(d[i - 1], _lambda))
                i += 1
            i = 1
            while i < n:
                d[i - 1] = d[i]
                i += 1
            d[n - 1] = utils.get_list_subtraction(x, y)
            if utils.get_vector_module(d[n - 1]) < self.eps:
                break
        self.answer_point = x
        self.answer = self.function(x)
        return self

