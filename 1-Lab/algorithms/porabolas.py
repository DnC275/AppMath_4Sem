from algorithms.method import Method


class Porabolass(Method):
    # implementation here
    def run(self):
        a = self.left
        b = self.right
        x = (a + b) / 2
        f1 = self.function(a)
        f2 = self.function(x)
        f3 = self.function(b)
        self.function_calls += 3
        prev_len = b - a
        while b - a >= self.eps:
            #print(a, b)
            u = x - ((x - a) ** 2 * (f2 - f3) - (x - b) ** 2 * (f2 - f1)) / (
                        2 * ((x - a) * (f2 - f3) - (x - b) * (f2 - f1)))
            if u > b or u < a:
                print(u)
                raise Exception("Некорректный отрезок")
            f4 = self.function(u)
            self.function_calls += 1
            l = x
            r = u
            if u < x:
                l, r = r, l
                f2, f4 = f4, f2
            if f2 < f4:
                b = r
                x = l
                f3 = f4
            elif f2 > f4:
                a = l
                x = r
                f1 = f2
                f2 = f4
            else:
                a = l
                b = r
                x = (l + r) / 2
                f1 = f2
                f3 = f4
                f2 = self.function(x)
                self.function_calls += 1
            self.iterations += 1
            real_len = b - a
            #print("[", "{:.5f}".format(a), ", ", "{:.5f}".format(b), "]", sep = '')
            #print(a, b)
            #print(real_len/prev_len)
        self.answer = (a + b) / 2
