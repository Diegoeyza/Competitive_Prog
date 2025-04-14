from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""10 11
1 1 1 1 1 1 1 1 1 1
10 10
1 1 1 1 1 1 1 1 1 1
5 3
1 2 3 4 5
3 2
4 78 9
1 2
1
1 1
1
5 1
1 2 3 4 5
5 2
1 2 3 4 5
10 3
9 5 1 4 2 8 7 3 6 5
21 6
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
""")

# def assign(ves,cont):
#     if len(ves)>cont:
#         cont_size=(len(ves)//cont)+1
#     if len(ves)<=cont:
#         return min(ves)
#     idx=-1
#     min_sum=float("inf")
#     for i in range (len(ves)):
#         if (len(ves)-i>=cont_size):
#             current_sum=0
#             for j in range(cont_size):
#                 current_sum+=ves[i+j]
#             if current_sum<min_sum:
#                 min_sum=current_sum
#                 idx=i
#     return min_sum

def is_valid(vessels, m, max_cap):
    containers = 1
    current = 0
    for v in vessels:
        if v > max_cap:
            return False
        if current + v <= max_cap:
            current += v
        else:
            containers += 1
            current = v
    return containers <= m

def assign(vessels, m):
    lowest = max(vessels)
    highest = sum(vessels)
    answer = highest
    while lowest <= highest:
        mid = (lowest + highest) // 2
        if is_valid(vessels, m, mid):
            answer = mid
            highest = mid - 1
        else:
            lowest = mid + 1
    return answer
    


vess, cont = [int(item) for item in stdin.readline().split()]
while vess!="":
    vessels=[int(item) for item in stdin.readline().split()]
    # print(vessels)
    print(assign(vessels,cont))
    try:
        vess, cont = [int(item) for item in stdin.readline().split()]
    except:
        vess=""
    

    