#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    item_map = {}
    for item in arr:
        if item_map.get(item) == None:
            item_map[item] = 1
        else:
            item_map[item] += 1

    return get_deletes(item_map)

def get_deletes(the_map):
    max_occur = 0
    sum = 0
    for occurs in the_map.values():
        sum += occurs
        if occurs > max_occur:
            max_occur = occurs

    return sum - max_occur


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

