from math import sin

from algorithms.method import *

function = lambda x: x ** 3 * sin(x)
print(function(5))
a = Method(function, 10, 10, 10)
print(a.function)
