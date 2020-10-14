#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):

    sticks_count_arr = []
    sticks_count_arr.append(len(arr))
    while len(arr)>1:
        arr = sticksRemaining(arr)
        sticks_count_arr.append(len(arr))

    return sticks_count_arr

def sticksRemaining(arr):
    minor = min(arr)
    sticks_size_arr = []
    for item in arr[:]:
        if (item - minor) > 0:
            sticks_size_arr.append(item - minor)
    return sticks_size_arr

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)
    #print(result)
    print('\n'.join(map(str, result)))
    print('\n')
    #fptr.close()