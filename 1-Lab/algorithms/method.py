class Method:
    def __init__(self, function, eps, left, right):
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
