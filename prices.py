#!/bin/python3

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    prices.sort()
    i = count = 0
    while k > prices[i]:
        k -=prices[i]
        i+=1
        count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
