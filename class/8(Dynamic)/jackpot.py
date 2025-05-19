from sys import stdin
import io
import math
import functools
from itertools import combinations


def kadane(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0

    for i, num in enumerate(nums):
        if current_sum + num > num:
            current_sum += num
        else:
            current_sum = num
            temp_start = i

        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i

    return max_sum, nums[start:end+1]





stdin = io.StringIO("""5
12 -4
-10 4
9
3
-2 -1 -2
0""")


bets=int(stdin.readline().strip())
while bets!=0:
    arr=[]
    while len(arr)<bets:
        line=map(int, stdin.readline().split()) 
        for bet in line:
            arr.append(bet)
    # print(arr)
    sol=kadane(arr)
    if sol[0]<1:
        print("Losing streak.")
    else:
        print(f"The maximum winning streak is {sol[0]}.")
    # print(sol[0])

    bets=int(stdin.readline().strip())
