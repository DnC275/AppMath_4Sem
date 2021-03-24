from algorithms.fibonacci import *
from algorithms.brent import *
from algorithms.golden_section import *

lens = golden_section_method(3, 6, 0.01)[4]
for i in range(1, len(lens)):
    print(lens[i-1]/lens[i])