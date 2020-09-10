#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    counter = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        token = arr[i][1]
        if i < len(arr) // 2:
            token = '-'
        counter[int(arr[i][0])].append(token)
    
    ans = []
    for tokens in counter:
        ans += tokens
    
    print(' '.join(ans))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
