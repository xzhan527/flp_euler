# Problem 13 : Large sum
# https://projecteuler.net/problem=6

"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from functools import reduce


def problem_6():
    sum = reduce(lambda x, y: x + y, [x for x in range(1, 101)])
    sum = sum**2
    square_sum = reduce(lambda x, y: x + y, [x**2 for x in range(1, 101)])
    print(sum - square_sum)


if __name__ == '__main__':
    problem_6()