import math


def get_vector_module(x: list):
    return math.sqrt(sum([i ** 2 for i in x]))


def get_list_subtraction(a: list, b: list):
    if len(a) != len(b):
        raise ValueError("The lists must be of the same length")
    return [a[i] - b[i] for i in range(len(a))]


def get_list_sum(a: list, b: list):
    if len(a) != len(b):
        raise ValueError("The lists must be of the same length")
    return [a[i] + b[i] for i in range(len(a))]


def divide_list_by_number(a: list, x):
    return [i / x for i in a]