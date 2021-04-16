from method import Method
import numdifftools as ndt


class FastestDescent(Method):
    def run(self):
        pass


func = lambda x: x ** 2
print(ndt.Gradient(func)([1]))
# class FastestDescent(Method):
#     def run(self):
#         while
