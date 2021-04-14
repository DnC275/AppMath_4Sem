from algorithms.method import Method


def dec(func):
    def wrapper(a: Method, x):
        a.inc_calls()
        return func(x)
    return wrapper


@dec
def function(func):
    return func


def test(func):
    return function(func)