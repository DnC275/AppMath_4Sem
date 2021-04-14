from math import sin
from algorithms.golden_section import GoldenSection
from algorithms.porabolas import Porabolass
from algorithms.brent import Brent


function = lambda x: x ** 3 * sin(x)
#print(function(5))
a = Brent(function, 0.0001, 0, 100)
d = a.function(1)
a.run()
print('Answer -', a.answer)
print("Iterations -", a.iterations)
print("Function calls -", a.function_calls)
print(*a.relations, sep='\n')
print('-----------')
print(*a.range, sep='\n')