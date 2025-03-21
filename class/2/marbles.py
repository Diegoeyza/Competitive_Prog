from sys import stdin
import io
import math
stdin = io.StringIO("""43
1 3
2 4
40
5 9
5 12
0""")

def find_combinations(a, b, target):
    combinations = []

    for X in range(target // a + 1):
        remainder = target - a * X
        if remainder % b == 0:
            Y = remainder // b
            combinations.append((X, Y))
    
    return combinations



marbles = int(stdin.readline().strip())


while marbles != 0:
    cost=float("inf")
    idx=-1
    cost1, c1 = [int(item) for item in stdin.readline().split()]
    cost2, c2 = [int(item) for item in stdin.readline().split()]
    comb=find_combinations(c1,c2, marbles)
    for i,item in enumerate(comb):
        if (comb[i][0]*cost1+comb[i][1]*cost2<=cost):
            idx=i
            cost=comb[i][0]*cost1+comb[i][1]*cost2
    if (len(comb)==0):
        print("failed")
    else:
        print(f"{comb[idx][0]} {comb[idx][1]}")





    marbles = int(stdin.readline().strip())


