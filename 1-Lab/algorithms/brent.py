from algorithms.method import Method
from math import sqrt

function_call_counter = 0

class Brent(Method):
    # implementation here
    def my_func(self, x):
        self.function_calls += 1
        return self.function(x)

    def run(self):
        k = (3 - sqrt(5)) / 2
        a, c = self.left, self.right
        x = (a + c) / 2
        w, v = x, x
        fx = self.my_func(x)
        fw, fv = fx, fx
        d = c - a
        e = d
        prev_len = c - a
        while c - a >= self.eps:
            check_parabola = False
            g = e
            e = d
            if x != w and x != v and w != v and fx != fw and fx != fv and fw != fv:
                arr = sorted([(x, fx), (w, fw), (v, fv)])
                l, m, r = arr[0][0], arr[1][0], arr[2][0]
                fl, fm, fr = arr[0][1], arr[1][1], arr[2][1]
                #fl, fm, fr = self.my_func(l), self.my_func(m), self.my_func(r)
                u = self.parabol_func(l, m, r, fl, fm, fr)
                if a <= u <= c and abs(u - x) < g / 2:
                    check_parabola = True
                    d = abs(u - x)
            if not check_parabola:
                if x < (a + c) / 2:
                    u = x + k * (c - x)
                    d = c - x
                else:
                    u = x - k * (x - a)
                    d = x - a

            fu = self.my_func(u)
            if fu <= fx:
                if u >= x:
                    a = x
                else:
                    c = x
                v = w
                w = x
                x = u
                fv = fw
                fw = fx
                fx = fu
            else:
                if u >= x:
                    c = u
                else:
                    a = u
                if fu <= fw or w == x:
                    v = w
                    w = u
                    fv = fw
                    fw = fu
                elif fu <= fv or v == x or v == w:
                    v = u
                    fv = fu
            self.iterations += 1
            real_len = c - a
            self.range.append((a, c))
            self.relations.append(real_len / prev_len)
            prev_len = real_len
        self.answer_point = (a + c) / 2
        self.answer = self.function(self.answer_point)

    def parabol_func(self, a, x, b, f1, f2, f3):
        u = x - ((x - a) ** 2 * (f2 - f3) - (x - b) ** 2 * (f2 - f1)) / (
                2 * ((x - a) * (f2 - f3) - (x - b) * (f2 - f1)))
        return u