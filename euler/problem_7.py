# Problem 7 : 10001st prime
# https://projecteuler.net/problem=7

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from itertools import islice
from math import sqrt


def generator_p_num():
    i = 2
    while True:
        factors = list(islice(filter(lambda x: i % x == 0, [x for x in range(2, int(sqrt(i)+1))]), 1))
        if len(factors) == 0:
            yield i
        i += 1


def problem_7():
    generator = generator_p_num()
    counter = 0
    while True:
        counter += 1
        p_number = next(generator)

        if counter == 10001:
            print(p_number)
            break


if __name__ == '__main__':
    problem_7()