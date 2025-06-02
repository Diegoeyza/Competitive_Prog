from sys import stdin
import io
import math
import functools
from itertools import permutations



stdin = io.StringIO("""5
19 15
7 13
5 7
6 8
1 2
0""")



def tallest(boxes):
    n=len(boxes)
    dp=[0]+[float("inf")]*n
    max_h=0
    for weight,load in reversed(boxes):
        for h in range(max_h,-1,-1):
            if dp[h]<=load:
                w_total= dp[h]+weight
                if w_total<dp[h+1]:
                    dp[h +1]=w_total
                    max_h=max(max_h,h + 1)
        # print(dp)

    return max_h




n_boxes = int(stdin.readline().strip())
while n_boxes!=0:
    boxes=[]
    for i in range (n_boxes):
        boxes.append(list(map(int, stdin.readline().split())))
    # print(boxes)
    print(tallest(boxes))
    n_boxes = int(stdin.readline().strip())




