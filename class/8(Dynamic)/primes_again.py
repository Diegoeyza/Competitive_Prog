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



n, k = map(int, stdin.readline().split()) 
while n!=0:
    primes=find_primes(n,0)
    comb=combinations(primes,k)
    counter=0
    for c in comb:
        if len(c)<k:
            continue
        if sum(c)==n:
            counter+=1
    print(f"N={n}, counter={counter}")

        
    try:
        n, k = map(int, stdin.readline().split()) 
    except:
        n=""