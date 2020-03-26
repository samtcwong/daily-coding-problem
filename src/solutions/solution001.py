from typing import Any, List, Tuple, Union

# Problem #1 [Easy]
#
# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

tests: Any = (
    # Given example test
    (([10, 15, 3, 7], 17), True),
    # should return false on the empty list
    (([], 0), False),
    # should return false on lists with a single element
    (([0], 0), False),
    (([1], 1), False),
    (([-1], -1), False),
    # should handle sums to zero
    (([0, 0], 0), True),
    (([1, -1], 0), True),
    # should handle summing with zero
    (([0, 1], 1), True),
    (([1, 0], 1), True),
    # should handle positive sums
    (([1, 2], 3), True),
    (([2, 1], 3), True),
    # should handle negative sums
    (([-1, -1], -2), True),
    (([1, -2], -1), True),
    # should handle list of 4 elements that match at the start
    (([1, 3, 2, 4], 4), True),
    # should handle list of 4 elements that match at the end
    (([1, 3, 2, 4], 6), True),
    # should handle list of 4 elements that match in the middle
    (([1, 3, 2, 4], 5), True),
    # should handle list of 5 elements that match at both ends
    (([1, 3, 2, 0, 5], 6), True),
    # should not match when sum to k doesn't exist in list
    (([6, 4, 2, 0], 3), False),
)


def any_two_numbers_add_up_to_k(numbers: List, k: int):
    if len(numbers) <= 1:
        return False

    targets = set()
    for number in numbers:
        if number in targets:
            return True
        new_target = k - number
        targets.add(new_target)

    return False


solver = any_two_numbers_add_up_to_k
