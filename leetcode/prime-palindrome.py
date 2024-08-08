#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'handleQueries' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY queries as parameter.
#
def isPrime(n, notPrimeSet, primeSet):
    if n in notPrimeSet:
        return False
    if n in primeSet:
        return True
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                notPrimeSet.add(n)
                return False
        primeSet.add(n)
        return True

def handleQueries(queries):
    # Write your code here

    # Queries will be of size Q and only has 2 numbers on every index - [0] and [1] is always going to be safe

    # Feel Free to add helper functions if needed
    notPrimeSet = set()
    primeSet = set()
    totalList = []
    for i in range(len(queries)):
        total = 0
        r0, r1 = queries[i]
        for n in range(r0, r1+1):
            pali = str(n)
            pali = pali[::-1]
            pali = int(pali)
            if isPrime(n, notPrimeSet, primeSet) and isPrime(pali, notPrimeSet, primeSet):
                total += 1
        totalList.append(total)
    return totalList

if __name__ == '__main__':
    Q = int(input().strip())

    queries = []

    for _ in range(Q):
        queries.append(list(map(int, input().rstrip().split())))

    result = handleQueries(queries)

    print('\n'.join(map(str, result)))
    print('\n')
