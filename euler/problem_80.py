# Problem 80 : Square root digital expansion
# https://projecteuler.net/problem=80

"""
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots
"""
from decimal import *
from functools import reduce


def get_sum(num):
    getcontext().prec = 102
    num = list(str(Decimal(num).sqrt()).replace('.', ''))
    num = list(map(int, list(num)))[:100]
    sum_num = reduce(lambda x, y: x + y, num)
    return sum_num


def problem_10():
    square = list(filter(lambda x: '.'  in str(Decimal(x).sqrt()) ,[x for x in range(1,100)]))
    square_sum = [get_sum(x) for x in square]
    sum_all = reduce(lambda x, y: x + y, square_sum)
    print(sum_all)


if __name__ == '__main__':
    problem_10()