import math
import os
import random
import re
import sys

def optimalPoint(magic, dist):
    if sum(magic) < sum(dist):
        return -1
    n, total_val, start = len(magic), 0, 0
    for i in range(n):
        if total_val < 0:
            start = i
            total_val = 0
        total_val += (magic[i] - dist[i])
    return start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    magic_count = int(input().strip())
    magic = []
    for _ in range(magic_count):
        magic_item = int(input().strip())
        magic.append(magic_item)

    dist_count = int(input().strip())
    dist = []
    for _ in range(dist_count):
        dist_item = int(input().strip())
        dist.append(dist_item)

    result = optimalPoint(magic, dist)
    fptr.write(str(result) + '\n')
    fptr.close()
