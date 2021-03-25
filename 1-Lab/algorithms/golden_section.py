from math import *
from algorithms.method import Method

counter = 0


class GoldenSection(Method):
    def f_counter(self, num):
        global counter
        counter += 1
        return self.function(num)

    def run(self):
        invphi = (sqrt(5) - 1) / 2
        invphi2 = (3 - sqrt(5)) / 2

        h = self.right - self.left
        lengths = [h]
        if h <= self.eps:
            print(f'a: {self.left}; b: {self.right}; fun calls: {counter}; iterations: 0; lengths: {lengths}')
            return (self.left, self.right, counter, 0, lengths)

        # required steps to achieve tolerance
        n = int(ceil(log(self.eps / h) / log(invphi)))

        x1 = self.left + invphi2 * h
        x2 = self.left + invphi * h
        yx1 = self.f_counter(x1)
        yx2 = self.f_counter(x2)

        iterations = 1
        while h > self.eps:
            if yx1 < yx2:
                self.right = x2
                x2 = x1
                yx2 = yx1
                h = invphi * h
                lengths.append(h)
                x1 = self.left + invphi2 * h
                yx1 = self.f_counter(x1)
                iterations += 1
            else:
                self.left = x1
                x1 = x2
                yx1 = yx2
                h = invphi * h
                lengths.append(h)
                x2 = self.left + invphi * h
                yx2 = self.f_counter(x2)
                iterations += 1

        if yx1 < yx2:
            print(
                f'a: {self.left}; b: {self.right}; fun calls: {counter}; iterations: {iterations}; lengths: {lengths}')
            return (self.left, x2, counter, n, lengths)
        else:
            print(f'a: {self.left}; b: {self.left}; fun calls: {counter}; iterations: {iterations}; lengths: {lengths}')
            return (x1, self.right, counter, n, lengths)
