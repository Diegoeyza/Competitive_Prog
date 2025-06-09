from sys import stdin
import io
import math
from collections import deque

stdin = io.StringIO("""3

2 5
0 2
2 0

3 20
0 2
2 0
2 1

3 5
3 0
0 4
5 5""")

def count_coins(coins, target):
    max_coord=target + 1
    coin_arr=[[math.inf for auxaux in range(max_coord)] for aux in range(max_coord)]
    coin_arr[0][0]=0
    queue=deque()
    queue.append((0, 0))
    while queue:
        x,y=queue.popleft()
        for dx,dy in coins:
            nx=x+dx
            ny=y+dy
            if nx<max_coord and ny<max_coord:
                if coin_arr[nx][ny]>coin_arr[x][y]+ 1:
                    coin_arr[nx][ny]=coin_arr[x][y] +1
                    queue.append((nx, ny))
    min_coins=math.inf
    for i in range(max_coord):
        for j in range(max_coord):
            if i*i+j*j==target*target:
                min_coins=min(min_coins, coin_arr[i][j])
    return min_coins if min_coins!=math.inf else "not possible"

n = int(stdin.readline().strip())
for case in range(n):
    stdin.readline()  #para que chuchaa meten lineas vacias
    m, S = map(int, stdin.readline().split())
    coins = []
    for aux in range(m):
        x,y=map(int,stdin.readline().split())
        coins.append((x, y))
    result = count_coins(coins, S)
    print(result)
