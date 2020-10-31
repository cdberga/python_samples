#!/bin/python3

from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
n,k = map(int,input().split())
teams = [list(map(int,list(input()))) for i in range(n)]
sums = [sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(teams,2)]
print(max(sums),sums.count(max(sums)),sep='\n')

