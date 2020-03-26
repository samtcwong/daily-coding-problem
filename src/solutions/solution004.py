from typing import List

# Problem #4 [Hard]
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

tests = (
    # Example 1
    (([3, 4, -1, 1],), 2),
    # Example 2
    (([1, 2, 0],), 3),
    # Negative Singleton
    (([-1],), 1),
    # Zero Singleton
    (([0],), 1),
    # Positive Singletons
    (([1],), 2),
    (([2],), 1),
    # Duplicates
    (([0, 0, 1],), 2),
    (([0, 1, 1],), 2),
    (([0, 1, 1, 1],), 2),
    (([-1, -1],), 1),
    (([0, 2, 2, 0, 0],), 1),
    # Input of length 2
    (([0, 1],), 2),
    (([0, -1],), 1),
    (([-1, 1],), 2),
    (([-1, 2],), 1),
    (([2, 0],), 1),
    # Input of length 3 or more
    (([1, 2, 4],), 3),
    (([4, 2, 1],), 3),
    (([3, 1, 4, 2],), 5),
    (([3, 1, -2, 4],), 2),
    (([3, 1, -10, 4, 2],), 5),
)


def first_missing_positive_integer(numbers: List[int]) -> int:
    for index in range(len(numbers)):
        if numbers[index] == index + 1:
            continue

        hanging_number = numbers[index]
        while (
            hanging_number is not None
            and 1 <= hanging_number <= len(numbers)
            and numbers[hanging_number - 1] != hanging_number
        ):
            next_hanging_number = numbers[hanging_number - 1]
            numbers[hanging_number - 1] = hanging_number
            hanging_number = next_hanging_number

    for index in range(len(numbers)):
        if numbers[index] != index + 1:
            return index + 1

    return len(numbers) + 1


solver = first_missing_positive_integer
