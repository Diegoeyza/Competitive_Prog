from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""4
1 4 5 7
4
4 6 8 10
""")

def taller_than(c, h):
    low, high = 0, len(c) - 1
    tallest = None
    while low <= high:
        mid = (low + high) // 2
        if c[mid] > h:
            tallest = c[mid]
            high = mid - 1
        else:
            low = mid + 1
    if tallest==None:
        return "X"
    else:
        return tallest


def smaller_than(c, h):
    low, high = 0, len(c) - 1
    smallest = None
    while low <= high:
        mid = (low + high) // 2
        if c[mid] < h:
            smallest = c[mid]
            low = mid + 1 
        else:
            high = mid - 1
    if smallest==None:
        return "X"
    else:
        return smallest




N=int(stdin.readline())
Chimps= [int(item) for item in stdin.readline().split()]
Q_num=int(stdin.readline())
Q= [int(item) for item in stdin.readline().split()]

for i in range (Q_num):
    tall=taller_than(Chimps,Q[i])
    small=smaller_than(Chimps,Q[i])
    print(f"{small} {tall}")

    