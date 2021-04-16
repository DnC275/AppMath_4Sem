from algorithms.method import Method
import utils


class NormalGradient(Method):
    def run(self):
        x0 = self.x0
        gradx0 = self.calculate_gradient(x0)
        _lambda = self.lambda_static()
        s = _lambda * gradx0
        print(gradx0)
        print(s)
        x = utils.get_list_subtraction(x0, s)
        while utils.get_vector_module(s) >= self.eps:
            print(x0, gradx0)
            self.segments.append([x0, x])
            x0 = x
            gradx0 = self.calculate_gradient(x0)
            _lambda = self.lambda_static()
            s = _lambda * gradx0
            x = utils.get_list_subtraction(x0, s)
        pre_result = utils.get_list_sum(x, x0)
        self.answer = self.function(utils.divide_list_by_number(pre_result, 2))
        self.answer_point = utils.divide_list_by_number(pre_result, 2)
        return self