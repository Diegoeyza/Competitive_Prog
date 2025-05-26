from sys import stdin
import io
import math
import functools


def create_combinations(blocks):
    possibilities=[]
    for block in blocks:
        for i in range (2,0,-1):
            pos=[block[i],block[i-1],block[i-2]]
            if pos not in possibilities:
                possibilities.append(pos)
    return possibilities

def validate_blocks(last,current):
    if last[0]>current[0] and last[1]>current[1]:
        return True

def check_max_height(possibilities):
    possibilities.sort(key=lambda x:(-x[0],-x[1]))
    n=len(possibilities)
    heights=[0]*n
    for i in range(n):
        heights[i]=possibilities[i][2]
        for j in range(i):
            if possibilities[j][0] > possibilities[i][0] and possibilities[j][1] > possibilities[i][1]:
                heights[i]=max(heights[i],heights[j]+ possibilities[i][2])
    return max(heights)


stdin = io.StringIO("""1
10 20 30
2
6 8 10
5 5 5
7
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
5
31 41 59
26 53 58
97 93 23
84 62 64
33 83 27
0""")


block_num = int(stdin.readline().strip())
p_case=1
while block_num!=0:
    blocks=[[] for i in range (block_num)]
    for i in range (block_num):
        blocks[i]=[int(item) for item in stdin.readline().split()]
        blocks[i].sort()
        # print(blocks[i])
    # print(blocks)
    possibilities=create_combinations(blocks)
    height=check_max_height(possibilities)
    print(f"Case {p_case}: maximum height = {height}")

    p_case+=1
    
    block_num = int(stdin.readline().strip())
