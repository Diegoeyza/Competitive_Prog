from sys import stdin
import io
import math
import functools
from itertools import combinations

@functools.lru_cache(None)
def find_primes(limit, starter):
    prime = bytearray([True]) * (limit + 1)
    prime[0]=False
    prime[1]=False

    for num in range(2, int(math.sqrt(limit)) + 1):
        if prime[num]:
            prime[num*num:limit+1:num] = bytearray([False]) * len(range(num*num, limit+1, num))
    return [i for i in range(starter + 1, limit + 1) if prime[i]]





stdin = io.StringIO("""24 3
24 2
2 1
1 1
4 2
18 3
17 1
17 3
17 4
100 5
1000 10
1120 14
0 0""")


max_num=1120
primes=find_primes(max_num,0)
comb=[[0]*(max_num+1) for length in range (14+1)]
comb[0][0]=1
for prime in primes:
    for length in range (14, 0, -1):
        for num in range (prime, max_num+1):
            comb[length][num]+=comb[length-1][num-prime]
n, k = map(int, stdin.readline().split()) 
while n!=0:
    # print(comb)
    print(f"{comb[k][n]}")

        
    try:
        n, k = map(int, stdin.readline().split()) 
    except:
        n=""