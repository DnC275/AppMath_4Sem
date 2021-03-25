# def inc_decorator(func):
#     def wrapper(self, function):
#         self.inc_calls()
#         print('sosi')
#         return func(self, function)
#     return wrapper


class Method:
    def __init__(self, function, eps, left, right):
        # #self.function = self.inc_decorator(self.impl_calls(), function)
        # self.function = self.smart_func(function)
        self.function = function
        self.eps = eps
        self.left = left
        self.right = right
        self.answer = None
        self.answer_point = None
        self.iterations = 0
        self.function_calls = 0

    def run(self):
        pass

    # def inc_calls(self):
    #     self.function_calls += 1
    #
    # @inc_decorator
    # def smart_func(self, func):
    #     return func

