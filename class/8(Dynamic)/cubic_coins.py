from sys import stdin
import io
import math
import functools
from itertools import combinations



MAX_VAL = 10000
coins=[i**3 for i in range(1, 22)]     
ways= [0]*(MAX_VAL+1)
ways[0]=1
for c in coins:                     
    for v in range(c,MAX_VAL+1):
        ways[v]+=ways[v - c]
del c,v #revisar, creo que así se borraban cosas en py                    

stdin = io.StringIO("""10
21
77
9999""")


cost=int(stdin.readline().strip())
while cost!="":
    # print(cost)
    print(ways[cost])


    try:
        cost=int(stdin.readline().strip())
    except:
        cost=""

