
# Problem 7 : 10001st prime
# https://projecteuler.net/problem=7

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
from collections import defaultdict
from itertools import count, islice

def sieve():
    numbers = []
    n = 2
    while True:
        if numbers[n]:
            print("ahoj")
        else:
            numbers.append((n * n, n))
            yield n
        n =+ 1



def _sieve_of_eratosthenes():
    factors = defaultdict(set)
    print(factors)

    for n in count(2):
        print("tu")
        print(n)
        # ak take cislo existuje
        if factors[n]:
            for m in factors.pop(n):
                print("ahoj")
                print(m)
                print(factors)
                factors[n+m].add(m)
                print(factors)
        else:
            factors[n*n].add(n)
            print(n)
            print(factors)
            yield n

def problem_2():

    object = _sieve_of_eratosthenes()
    next(object)
    next(object)
    next(object)

    next(object)



if __name__ == '__main__':
    problem_2()