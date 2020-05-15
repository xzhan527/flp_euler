# Problem 16 : Digit factorials
# https://projecteuler.net/problem=16

"""
What is the sum of the digits of the number 21000?
"""

from functools import reduce


def generator():
    exponent = 0
    while True:
        yield 2 ** exponent
        exponent += 1


def problem_34(number):
    obj = generator()
    exponent = 0
    while True:
        number = next(obj)
        exponent += 1
        if exponent > 1000:
            break

    digit_sum = reduce(lambda x, y: x+y, list(map(int, str(number))))
    print(digit_sum)


if __name__ == '__main__':
    problem_34(145)


