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
    ind_s = 1

    if check_attendees(topic) == False:
        return [0, 0]

    len_topic = len(topic)

    while ind_f < len_topic:
        while ind_s < len_topic:
            mem_topics = sum_topics(topic[ind_f], topic[ind_s])
            if mem_topics > max_topics:
                max_topics = mem_topics
                teams_max = 1
            elif mem_topics == max_topics:
                teams_max += 1
            ind_s += 1
        ind_f += 1
        ind_s = ind_f+1

    return [max_topics, teams_max]

def check_attendees(topic):
    qt_lines = len(topic)
    return qt_lines >= 2 and qt_lines <= 500

def check_topics(topics):
    return topics >= 1 and topics <= 500

def sum_topics(f, s):
    sum_ = 0
    i = 0
    attends = check_topics(f,s)

    len_f = range(0, len(f))
    for i in len_f:
        if attends(i):
            sum_ += 1

    return sum_

def check_topics(f, s):
    return lambda n : f[n] == '1' or s[n] == '1'

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

