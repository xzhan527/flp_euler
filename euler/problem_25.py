# Problem 25 : 1000-digit Fibonacci number
# https://projecteuler.net/problem=25

"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def generator():
    num_1 = 1
    num_2 = 1
    while True:
        sum = num_1+num_2
        yield sum
        num_1 = num_2
        num_2 = sum


def problem_25():
    obj = generator()
    list_fact = []
    while True:
        number = next(obj)
        list_fact.append(number)
        if len(list(str(number))) == 1000:
            break

    print(len(list_fact)+2)


if __name__ == '__main__':
    problem_25()