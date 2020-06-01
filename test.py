#!/bin/python3

import sys

def minimumDeletions(a):
    # Complete this function
    deletions = 0
    lastX = None
    trend = 0
    for x in a:
        deleteX = False
        if lastX:
            if lastX < x:
                if trend > 0 and trend == 1:
                    deleteX = True
                else:
                    trend = 1
            elif lastX > x:
                if trend < 0 and trend == -1:
                    deleteX = True
                else:
                    trend = -1
            else:
                trend = 0
        if deleteX:
            deletions = deletions + 1
        else:
            lastX = x
    return deletions


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)