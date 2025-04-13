from sys import stdin
import io
import math
stdin = io.StringIO("""11
1""")

def find_primes(limit, starter):
    prime = bytearray([True]) * (limit + 1)
    prime[0]=False
    prime[1]=False

    for num in range(2, int(math.sqrt(limit)) + 1):
        if prime[num]:
            prime[num*num:limit+1:num] = bytearray([False]) * len(range(num*num, limit+1, num))
    return [i for i in range(starter + 1, limit + 1) if prime[i]]

def find_candidates(primes,num_sum):
    candidates = set()
    for num in primes:
        if sum(map(int, str(num))) == num_sum:
            candidates.add(num)
    return candidates







total_sum = int(stdin.readline().strip())
d=int(stdin.readline().strip())
primes=find_primes(99999,10000)
candidates=find_candidates(primes,11)

