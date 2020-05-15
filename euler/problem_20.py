# Problem 20 : Factorial digit sum
# https://projecteuler.net/problem=20

"""
Find the sum of the digits in the number 100!
"""

from functools import reduce


def problem_20():
    factorial = reduce(lambda x, y: x*y, [x for x in range(1, 100)])
    digit_sum = reduce(lambda x, y: x+y, list(map(int, str(factorial))))
    print(digit_sum)


if __name__ == '__main__':
    problem_20()