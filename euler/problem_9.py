# Problem 9 : Special Pythagorean triplet
# https://projecteuler.net/problem=9

"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from functools import reduce


def get_trip(x):
    for y in range(1,1000):
        z = 1000-y-x
        if (x ** 2 + y**2) == z**2:
            return True


def problem_9():
    answer = list(filter(get_trip,[x for x in range(1,1000)]))
    answer.append(1000-(answer[0]+answer[1]))
    print(reduce(lambda x,y: x*y, answer))


if __name__ == '__main__':
    problem_9()