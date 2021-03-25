from math import sqrt

from algorithms.method import *


def get_fibonacci_number(n):
    return (1 / sqrt(5)) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n)


class Fibonacci(Method):

    def run(self):
        n = 0
        while ((self.right - self.left) / self.eps) > get_fibonacci_number(n + 2):
            n += 1
        left = self.left
        right = self.right
        first_diff = right - left
        x1 = left + get_fibonacci_number(n) / get_fibonacci_number(n + 2) * (right - left)
        x2 = left + get_fibonacci_number(n + 1) / get_fibonacci_number(n + 2) * (right - left)
        self.iterations += 1
        f_x1 = self.function(x1)
        f_x2 = self.function(x2)
        self.function_calls += 2
        if f_x1 > f_x2:
            left = x1
            point_tmp = x2
            f_point_tmp = f_x2
        else:
            right = x2
            point_tmp = x1
            f_point_tmp = f_x1
        self.range.append([float('%.4f' % left), float('%.4f' % right)])
        self.relations.append((right - left) / first_diff)
        while right - left >= self.eps:
            first_diff = right - left
            self.iterations += 1
            if point_tmp - left < right - point_tmp:
                x1 = point_tmp
                f_x1 = f_point_tmp
                x2 = right - (x1 - left)
                f_x2 = self.function(x2)
                self.function_calls += 1
            else:
                x2 = point_tmp
                f_x2 = f_point_tmp
                x1 = left + (right - point_tmp)
                f_x1 = self.function(x1)
                self.function_calls += 1
            if f_x1 > f_x2:
                left = x1
                point_tmp = x2
                f_point_tmp = f_x2
            else:
                right = x2
                point_tmp = x1
                f_point_tmp = f_x1
            self.range.append([float('%.4f' % left), float('%.4f' % right)])
            self.relations.append((right - left) / first_diff)
        self.answer_point = (right + left) / 2
        self.answer = self.function(self.answer_point)
