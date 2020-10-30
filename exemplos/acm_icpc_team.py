#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    max_topics = 0
    mem_topics = 0
    teams_max = 0

    ind_f = 0
    ind_s = 0

    for f_member in topic:
        for s_member in topic:
            if ind_f < ind_s:
                mem_topics = sum_topics(f_member, s_member)
                if mem_topics > max_topics:
                    max_topics = mem_topics
                    teams_max = 1
                elif mem_topics == max_topics:
                    teams_max += 1
            ind_s += 1
        ind_s = 0
        ind_f += 1

    return [max_topics, teams_max]

def sum_topics(f, s):
    sum_ = 0
    i = 0
    while i < len(f):
        if f[i] == 1 or s[i] == 1:
            sum_ += 1
        i += 1
    return sum_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print(result)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

