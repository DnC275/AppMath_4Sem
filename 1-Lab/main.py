from math import sin
from algorithms.golden_section import GoldenSection


function = lambda x: x ** 3 * sin(x)
print(function(5))
a = GoldenSection(function, 1, 2, 5)
print(a.function)
