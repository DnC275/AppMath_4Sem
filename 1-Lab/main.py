from math import sin
from algorithms.golden_section import GoldenSection
from algorithms.porabolas import Porabolass


function = lambda x: x ** 3 * sin(x)
#print(function(5))
a = Porabolass(function, 0.00001, 4, 6)
a.run()
print(a.iterations)
