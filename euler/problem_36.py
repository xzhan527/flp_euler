# Problem 63 : Large sum
# https://projecteuler.net/problem=13

"""
How many n-digit positive integers exist which are also an nth power?
"""

def generator():
    num = 2
    exponent = 0
    counter = 0
    while True:
        product = num**exponent
        print(product)
        if len(list(str(product))) == exponent:
            yield product

        if len(list(str(product))) > exponent:
            num +=1
            exponent=0
        exponent += 1


def problem_63():
    obj = generator()
    list_num = []
    while True:
        number = next(obj)
        list_num.append(number)
        if len(list_num) == 4:
            break
    print(list_num)




if __name__ == '__main__':
   problem_63()