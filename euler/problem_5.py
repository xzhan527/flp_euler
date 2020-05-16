# Problem 5 : Smallest multiple
# https://projecteuler.net/problem=5

"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from itertools import islice


def problem_5():
    div = [x for x in range(2,20)]
    num = 2520
    counter = 1
    while True:
        curr_num = num * counter
        list_num = list(islice(filter(lambda x: curr_num%x != 0,div),1))
        if len(list_num) == 0:
            break
        counter+=1

    print(curr_num)

if __name__ == '__main__':
    problem_5()