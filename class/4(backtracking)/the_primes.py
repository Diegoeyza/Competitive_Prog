from sys import stdin
import io
import math
stdin = io.StringIO("""11
1""")

def find_primes(limit,starter):
    prim=set()
    s_prim=set()
    prim.add(2)
    for i in range (2,limit):
        p=True
        for item in prim:
            if i%item==0:
                p=False
        if (p):
            prim.add(i)
            if i>starter:
                s_prim.add(i)
    return(sorted(s_prim))

def find_primes(limit, starter):
    prime = bytearray([True]) * (limit + 1)
    prime[0]=False
    prime[1]=False

    for num in range(2, int(math.sqrt(limit)) + 1):
        if prime[num]:
            prime[num*num:limit+1:num] = bytearray([False]) * len(range(num*num, limit+1, num))
    return [i for i in range(starter + 1, limit + 1) if prime[i]]

total_sum = int(stdin.readline().strip())
d=int(stdin.readline().strip())
print(find_primes(99999,10000))

