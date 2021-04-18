from method import Method
import numdifftools as ndt
from scipy import optimize


class Powell(Method):
    def run(self):
        p = [[1, 0], [0, 1]]
        cur_x = self.x0[:]
        while self.len_vector(p[1]) >= self.eps:
            new_function = lambda l: self.function([cur_x[k] + l * p[1][k] for k in range(len(cur_x))])
            h_min = optimize.minimize(new_function, x0=0)["x"][0]
            cur_x = [cur_x[k] + h_min * p[1][k] for k in range(len(cur_x))]
            y = cur_x[:]
            i = 0
            while i <= 1:
                new_function = lambda l: self.function([cur_x[k] + l * p[i][k] for k in range(len(cur_x))])
                h_min = optimize.minimize(new_function, x0=0)["x"][0]
                cur_x = [cur_x[k] + h_min * p[i][k] for k in range(len(cur_x))]
                i += 1
            i = 0
            p[i] = p[i+1][:]
            p[1] = [cur_x[k] - y[k] for k in range(len(p))]
            print(p, '!!!!')
        self.answer_point = cur_x
        return self.answer_point

    def run_(self):
        p1 = [1, 0]
        p2 = [0, 1]
        cur_x = self.x0[:]
        while True:
            gr = ndt.Gradient(self.function)(cur_x)
            gr_len = self.len_vector(gr)
            # print(gr_len)
            if gr_len < self.eps:
                break
            x1_h = [lambda h: cur_x[i] + h * p2[i] for i in range(len(cur_x))]
            pnt = lambda h: self.function(list(map(lambda x: x(h), x1_h)))
            h_min = optimize.minimize(pnt, x0=0)["x"][0]
            print(h_min)
            x1 = [f(h_min) for f in x1_h]
            print(x1)

            x2_h = [lambda h: x1[i] + h * p1[i] for i in range(len(cur_x))]
            pnt = lambda h: self.function(list(map(lambda x: x(h), x2_h)))
            h_min = optimize.minimize(pnt, x0=0)["x"][0]
            x1 = [f(h_min) for f in x2_h]

            x3_h = [lambda h: x1[i] + h * p2[i] for i in range(len(cur_x))]
            pnt = lambda h: self.function(list(map(lambda x: x(h), x3_h)))
            h_min = optimize.minimize(pnt, x0=0)["x"][0]
            x3 = [f(h_min) for f in x3_h]

            cur_x = x3
            p2 = [x3[i] - x1[i] for i in range(len(p1))]
        return cur_x
