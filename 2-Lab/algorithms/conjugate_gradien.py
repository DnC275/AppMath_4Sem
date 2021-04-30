from method import Method
import numdifftools as ndt


class ConjugateGradient(Method):
    def run(self):
        k = 0
        pk = ndt.Gradient(self.function)(self.x0)
        cur_x = self.x0[:]

        while True:
            tmp = cur_x[:]
            cur_x = [cur_x[i] - self.lambda_by_golden_section(self.x0)*pk[i] for i in range(len(cur_x))]
            gr = ndt.Gradient(self.function)(cur_x)

            if self.len_vector(gr) < self.eps:
                break

            if k + 1 == self.n:
                self.x0 = cur_x[:]
                k = 0
                pk = ndt.Gradient(self.function)(self.x0)
                continue

            b = (self.len_vector(ndt.Gradient(self.function)(cur_x)) ** 2) / (self.len_vector(ndt.Gradient(self.function)(tmp)) ** 2)
            pk = [-gr[i] - b*pk[i] for i in range(len(pk))]
        self.answer = cur_x
        self.answer_point = self.function(cur_x)
        return self.answer

