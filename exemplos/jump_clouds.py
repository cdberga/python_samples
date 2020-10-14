#!/bin/python3

import math
import os
import random
import re
import sys

def havePassedConstraints(c, n):
    return isNumberOfMembersAllowed(n) and areAllMembersAllowed(c) and areFirstAndLastMembersAllowed(c,n)

def isNumberOfMembersAllowed(n):
    return n >= 2 and n <= 100

def areAllMembersAllowed(c):
    for item in c:
        if item==0 or item==1:
            return True
    return False

def areFirstAndLastMembersAllowed(c, n):
    return c[0] == c[n-1] == 0

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, n):
    if not havePassedConstraints(c,n):
        return -1

    counter = 1
    jumps=0
    shift=1
    previous=0
    while counter < n:
        current = c[counter]

        if shift == 1 and current == 0:
            jumps += 1
            if previous == 1:
                shift=0
            shift += 1
        elif shift == 2 and current ==0:
            shift=0
        elif current == 1:
            shift = 1

        previous = current
        counter += 1

    return jumps

#7
#0 0 1 0 0 1 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    print(str(result) + '\n')
    fptr.write(str(result) + '\n')

    fptr.close()

