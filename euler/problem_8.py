# Problem 8 : Largest product in a series
# https://projecteuler.net/problem=8

"""
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

from functools import reduce


def get_digits(index,numbers):
    return reduce(lambda x,y: x*y, numbers[index:index+13])


def problem_8(numbers):
    start = 0
    end = 1
    list_sum = [get_digits(x,numbers)for x in range(len(numbers)-13)]
    print(max(list_sum))


if __name__ == '__main__':
    numbers = []
    with open("problem_8.txt", "r") as f:
        for line in f:
            numbers.append(line.strip('\n'))
    numbers = "".join(numbers)
    numbers = list(map(int,numbers))
    problem_8(numbers)
