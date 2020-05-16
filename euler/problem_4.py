# Problem 4 : Largest palindrome product
# https://projecteuler.net/problem=4

"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def generator():
    num_1 = 999
    num_2 = 999
    while True:
        multiply = num_1*num_2
        yield multiply
        num_2 = num_2 - 1
        if num_2 == num_1-100:
            num_1 = num_1 - 1
            num_2 = num_1


def problem_4():
    obj = generator()
    while True:
        number = next(obj)
        list_num = list(str(number))
        if len(list_num)%2 == 0:
            half = int(len(list_num)/2)
            list_half = list_num[:half]
            list_half.reverse()
            if "".join(list_num[half:]) == "".join(list_half):
                break

    print(number)






if __name__ == '__main__':
    problem_4()