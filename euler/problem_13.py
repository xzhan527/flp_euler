# Problem 13 : Large sum
# https://projecteuler.net/problem=13

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
problem_20.txt
"""

from functools import reduce
from itertools import islice


def problem_13(numbers):
    sum = reduce(lambda x, y: x + y, numbers)
    list_sum = ''.join(list(islice(list(str(sum)),10)))
    print(list_sum)


if __name__ == '__main__':
    numbers = []

    with open("problem_20.txt", "r") as f:
        for line in f:
            numbers.append(int(line.strip('\n')))
    problem_13(numbers)
