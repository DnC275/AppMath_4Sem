import numdifftools as ndt
import utils
import math
import numpy as np
from scipy.misc import derivative
from method import Method


class NewtonMethod(Method):
    def run(self):
        x0 = self.x0[:]
        gradient = self.calculate_gradient(x0)
        hessian = ndt.Hessian(self.function)(x0)
        s = np.linalg.solve(hessian, [-i for i in gradient])
        x = utils.get_list_sum(x0, s)
        self.iterations+=1

        while utils.get_vector_module(s) >= self.eps:
            self.segments.append([x0, x])
            x0 = x
            gradient = self.calculate_gradient(x0)
            hessian = ndt.Hessian(self.function)(x0)
            s = np.linalg.solve(hessian, [-i for i in gradient])
            x = utils.get_list_sum(x0, s)
            self.iterations += 1

        self.answer_point = x
        self.answer = self.function(x)
