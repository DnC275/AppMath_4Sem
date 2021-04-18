import utils
from method import Method


def lambda_splitting(_lambda, flag: bool):
    if flag:
        return _lambda / 2
    return _lambda


class SplittingGradient(Method):
    def run(self):
        counter = 0
        check = False
        x0 = self.x0
        gradx0 = self.calculate_gradient(x0)
        _lambda = self._lambda
        s = _lambda * gradx0
        x = utils.get_list_subtraction(x0, s)
        fx0 = self.function(x0)
        fx = self.function(x)
        while fx >= fx0:
            check = True
            _lambda = lambda_splitting(_lambda, True)
            s = _lambda * gradx0
            x = utils.get_list_subtraction(x0, s)
            fx0 = self.function(x0)
            fx = self.function(x)
        self.iterations += 1
        if check:
            counter += 1
        while utils.get_vector_module(s) >= self.eps:
            print(x0, gradx0)
            self.segments.append([x0, x])
            x0 = x
            gradx0 = self.calculate_gradient(x0)
            _lambda = lambda_splitting(_lambda, False)
            s = _lambda * gradx0
            x = utils.get_list_subtraction(x0, s)
            fx0 = self.function(x0)
            fx = self.function(x)
            while fx >= fx0:
                check = True
                _lambda = lambda_splitting(_lambda, True)
                s = _lambda * gradx0
                x = utils.get_list_subtraction(x0, s)
                fx0 = self.function(x0)
                fx = self.function(x)
            self.iterations += 1
            if check:
                counter += 1
            if counter >= 50:
                check = False
                counter = 0
                _lambda = self._lambda
        pre_result = utils.get_list_sum(x, x0)
        self.answer = self.function(utils.divide_list_by_number(pre_result, 2))
        self.answer_point = utils.divide_list_by_number(pre_result, 2)
        return self
