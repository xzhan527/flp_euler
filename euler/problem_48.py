# Problem 48 : Self powers
# https://projecteuler.net/problem=48

"""
Find the last ten digits of the series
"""
from functools import reduce


def generator():
    number = 1
    while True:
        yield number ** number
        number += 1


def problem_48():
    obj = generator()
    list_numbers = []
    while True:
        list_numbers.append(next(obj))
        if len(list_numbers) == 1000:
            break
    sum = reduce(lambda x, y: x + y, list_numbers)
    list_sum = ''.join(list(str(sum))[-10:])
    print(list_sum)


if __name__ == '__main__':
    problem_48()