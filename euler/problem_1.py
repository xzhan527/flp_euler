
# Problem 1 : Multiples of 3 and 5
# https://projecteuler.net/problem=1

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000

"""
from functools import reduce


def problem_1():
    multiples = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
    multiples.remove(0)
    sum_multi = reduce(lambda x, y: x+y, multiples)

    print(multiples)
    print(sum_multi)


if __name__ == '__main__':
    problem_1()
