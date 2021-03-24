from math import *

counter = 0


def f_counter(num):
    global counter
    counter += 1
    return sin(num) * pow(num, 3)


def golden_section_method(a, b, epsilon):
    invphi = (sqrt(5) - 1) / 2
    invphi2 = (3 - sqrt(5)) / 2

    h = b - a
    lengths = []
    lengths.append(h)
    if h <= epsilon:
        print(f'a: {a}; b: {b}; fun calls: {counter}; iterations: 0; lengths: {lengths}')
        return (a, b, counter, 0, lengths)

    # required steps to achieve tolerance
    n = int(ceil(log(epsilon / h) / log(invphi)))

    x1 = a + invphi2 * h
    x2 = a + invphi * h
    yx1 = f_counter(x1)
    yx2 = f_counter(x2)

    iterations = 0
    while h > epsilon:
        if yx1 < yx2:
            b = x2
            x2 = x1
            yx2 = yx1
            h = invphi * h
            lengths.append(h)
            x1 = a + invphi2 * h
            yx1 = f_counter(x1)
            iterations+=1
        else:
            a = x1
            x1 = x2
            yx1 = yx2
            h = invphi * h
            lengths.append(h)
            x2 = a + invphi * h
            yx2 = f_counter(x2)
            iterations+=1

    if yx1 < yx2:
        print(f'a: {a}; b: {b}; fun calls: {counter}; iterations: {iterations}; lengths: {lengths}')
        return (a, x2, counter, n, lengths) # self.a = var
    else:
        print(f'a: {a}; b: {b}; fun calls: {counter}; iterations: {iterations}; lengths: {lengths}')
        return (x1, b, counter, n, lengths)
