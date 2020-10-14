#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    st = str(n)
    sum_if_true = 0
    for itr in st:
        number = int(itr)
        sum_if_true += 0 if (number == 0) or ((n % number) != 0) else 1
    return sum_if_true

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('myfile.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
