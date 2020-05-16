# Problem 36 : Large sum
# https://projecteuler.net/problem=36

"""
Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2
"""
from copy import deepcopy
from functools import reduce

# poznamka: najde, ale trva velmi dlho


def is_palindrome(x):
    list_x = list(str(x))
    reverse_x = deepcopy(list_x)
    reverse_x.reverse()
    bin_x = list("{0:b}".format(x))
    reverse_bin = deepcopy(bin_x)
    reverse_bin.reverse()
    return list_x == reverse_x and bin_x == reverse_bin


def problem_36():
    list_num = [x for x in range(10)]
    list_pali = list(filter(is_palindrome,range(1,1000000)))
    sum = reduce(lambda x,y: x+y, list_pali)
    print(sum)


if __name__ == '__main__':
    problem_36()
