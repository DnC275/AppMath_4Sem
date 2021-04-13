from math import sin
from algorithms.golden_section import GoldenSection
from algorithms.brent import Brent
from algorithms.dichotomy import DichotomyMethod
from algorithms.fibonacci import Fibonacci
from algorithms.porabolas import Porabolass


function = lambda x: x ** 3 * sin(x)

print('Dichotomy------------------------')
dichotomy = DichotomyMethod(function, 0.0001, 0, 100)
dichotomy.run()
print(f'iterations: {dichotomy.iterations}')
print(f'functins calls: {dichotomy.function_calls}')
print(f'answer: {dichotomy.answer}')
print(f'answer point: {dichotomy.answer_point}')

print('Golden section----------------------------------')
golden_section = GoldenSection(function, 0.0001, 0, 100).run()
print(f'iterations: {golden_section.iterations}')
print(f'functins calls: {golden_section.function_calls}')
print(f'answer: {golden_section.answer}')
print(f'answer point: {golden_section.answer_point}')
# print(f'relations:')
# for i in golden_section.relations:
#     print(float("%.4f" % i))
# print(f'relations amount: {len(golden_section.relations)}')
# print(f'ranges:')
# for i in golden_section.range:
#     print(f'[{float("%.4f" % i[0])}, {float("%.4f" % i[1])}]')
# print(f'ranges amount: {len(golden_section.range)}')

print('Fibonacci----------------------------------')
fibonacci = Fibonacci(function, 0.0001, 0, 100)
fibonacci.run()
print(f'iterations: {fibonacci.iterations}')
print(f'functins calls: {fibonacci.function_calls}')
print(f'answer: {fibonacci.answer}')
print(f'answer point: {fibonacci.answer_point}')

print('Parabolas----------------------------------')
parabolas = Porabolass(function, 0.0001, 0, 100)
parabolas.run()
print(f'iterations: {parabolas.iterations}')
print(f'functins calls: {parabolas.function_calls}')
print(f'answer: {parabolas.answer}')
print(f'answer point: {parabolas.answer_point}')

print('Brent-----------------------------------------')
brent = Brent(function, 0.0001, 0, 100)
brent.run()
print(f'iterations: {brent.iterations}')
print(f'functins calls: {brent.function_calls}')
print(f'answer: {brent.answer}')
print(f'answer point: {brent.answer_point}')
# print(f'relations:')
# for i in brent.relations:
#     print(float("%.4f" % i))
# print(f'relations amount: {len(brent.relations)}')
# print(f'ranges:')
# for i in brent.range:
#     print(f'[{float("%.4f" % i[0])}, {float("%.4f" % i[1])}]')
# print(f'ranges amount: {len(brent.range)}')