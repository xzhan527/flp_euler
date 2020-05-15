# Problem 2 : Even Fibonacci numbers
# https://projecteuler.net/problem=2

"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
from functools import reduce


def generator():
    num_1 = 1
    num_2 = 1
    while True:
        sum = num_1+num_2
        if sum %2 == 0:
            yield sum
        num_1 = num_2
        num_2 = sum


def problem_2():
    obj = generator()
    list_even = []
    while True:
        number = next(obj)
        if number > 4000000:
            break
        list_even.append(number)

    sum = reduce(lambda x, y: x + y, list_even)
    print(sum)


if __name__ == '__main__':
    problem_2()