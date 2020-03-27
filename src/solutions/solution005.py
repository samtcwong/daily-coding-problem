from typing import Any, Callable, List, Tuple

# Problem #5 [Medium]
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
# last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# Implement car and cdr.


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def left(a, _):
        return a

    return pair(left)


def cdr(pair):
    def right(_, b):
        return b

    return pair(right)


def eval_(function):
    return function


tests = (
    ((car(cons(3, 4)),), 3),
    ((cdr(cons(3, 4)),), 4),
    ((car(cons(-1, 4)),), -1),
    ((cdr(cons(0, -1)),), -1),
)


solver = eval_
