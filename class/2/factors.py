from math import prod
from sys import stdin
import io
def combinations(arr, r):
    def bcktrack(start, path):
        if len(path) == r:
            result.append(tuple(path))
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            bcktrack(i + 1, path)
            path.pop()
    
    result = []
    bcktrack(0, [])
    return result

def get_factors(n):
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def find_min_sum_factors(n):
    factors = get_factors(n)
    min_sum = float('inf')
    if n==1:
        return 2

    for r in range(2, len(factors) + 1):
        for combo in combinations(factors, r):
            if prod(combo) == n:
                print(combo)
                min_sum = min(min_sum, sum(combo))

    return min_sum if min_sum != float('inf') else n+1

stdin = io.StringIO("""12
10
5
9
2147483647
0""")

input_value = int(stdin.readline().strip())
case=1
while input_value != 0:
    print(f"Case {case}: {find_min_sum_factors(input_value)}")
    case+=1

    input_value = int(stdin.readline().strip())
