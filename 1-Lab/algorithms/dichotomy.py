from algorithms.method import *


class DichotomyMethod(Method):
    # implementation here

    def __init__(self, function, eps, left, right):
        super().__init__(function, eps, left, right)

    def run(self):
        left = self.left
        right = self.right
        while right - left >= self.eps:
            first_diff = right - left
            self.iterations += 1
            x1 = ((right + left) / 2) - self.eps / 2 * 0.8
            x2 = ((right + left) / 2) + self.eps / 2 * 0.8
            f_x1 = self.function(x1)
            f_x2 = self.function(x2)
            self.function_calls += 2
            if f_x1 == f_x2:
                left = x1
                right = x2
            elif f_x1 > f_x2:
                left = x1
            elif f_x1 < f_x2:
                right = x2
            else:
                assert IOError("idk how you did this but your I/O quite bad")
            self.range.append([float('%.4f' % left), float('%.4f' % right)])
            self.relations.append((right - left) / first_diff)
        self.answer_point = (right + left) / 2
        self.answer = self.function(self.answer_point)
