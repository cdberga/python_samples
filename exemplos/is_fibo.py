#!/bin/python3

import os
import sys
import math   # This will import math module

def is_quantity_ok(t):
    return 1<= t <= math.pow(10, 5)

def is_number_ok(n):
    return 1<= n <= math.pow(10, 10)

# Complete the solve function below.
def solve(n):
    fibo_num = [0,1]
    test_num = fibo_num[0] + fibo_num[1]
    if is_number_ok(n):
        while test_num <= n:
            if test_num == n:
                return "IsFibo"
            test_num = fibo_num[0] + fibo_num[1]
            fibo_num[0] = fibo_num[1]
            fibo_num[1] = test_num

        return "IsNotFibo"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    if not is_quantity_ok(t):
        exit()

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

