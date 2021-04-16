from method import Method
from .. import utils

class FastestDescent(Method):
    def run(self):
        x0 = self.x0
        gradx0 = self.calculate_gradient(x0)
        _lambda = self.lambda_by_fibonacci(x0)
        s = _lambda * gradx0
        x = utils.get_list_subtraction(x0, s)
        while utils.get_vector_module(s) >= self.eps:
            self.segments.append([x0, x])
            x0 = x
            gradx0 = self.calculate_gradient(x0)
            _lambda = self.lambda_by_golden_section(x0)
            s = _lambda * gradx0
            x = utils.get_list_subtraction(x0, s)
        pre_result = utils.get_list_sum(x, x0)
        self.answer = self.function(utils.divide_list_by_number(pre_result, 2))
        self.answer_point = utils.divide_list_by_number(pre_result, 2)
        return self

# func = lambda x: x[0]**2 + x[1]**2
# print(ndt.Gradient(func)([4, 1]))
