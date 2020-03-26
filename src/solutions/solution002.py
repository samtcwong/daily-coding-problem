import functools
import operator

from typing import Dict, List

# Problem #2 [Hard]
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

tests = (
    # Example 1
    (([1, 2, 3, 4, 5],), [120, 60, 40, 30, 24]),
    # Example 2
    (([3, 2, 1],), [2, 3, 6]),
)


def solution_with_division(numbers: List[int]) -> List[int]:
    # Time complexity scaling linearly with respect to input
    if not numbers:
        return []

    product = functools.reduce(operator.mul, numbers)
    new_numbers = map(lambda number: product // number, numbers)

    return list(new_numbers)


def follow_up_solution_without_division(numbers: List[int]):
    # Solution with memoization, time complexity scaling linearly with respect to input
    assert numbers

    product_backward_cache: Dict[int, int] = dict()

    def product_backward(index):
        if index in product_backward_cache:
            return product_backward_cache[index]

        if index == 0:
            product_backward_cache[index] = numbers[0]
        else:
            product_backward_cache[index] = numbers[index] * product_backward(index - 1)

        return product_backward_cache[index]

    product_forward_cache: Dict[int, int] = dict()

    def product_forward(index):
        if index in product_forward_cache:
            return product_forward_cache[index]

        if index == len(numbers) - 1:
            product_forward_cache[index] = numbers[-1]
        else:
            product_forward_cache[index] = numbers[index] * product_forward(index + 1)

        return product_forward_cache[index]

    new_numbers = []
    for i, number in enumerate(numbers):
        if i == 0:
            new_numbers.append(product_forward(i + 1))
        elif i == len(numbers) - 1:
            new_numbers.append(product_backward(i - 1))
        else:
            new_numbers.append(product_backward(i - 1) * product_forward(i + 1))

    return new_numbers


solver = follow_up_solution_without_division
