import math
import itertools
from sys import stdin
import io

def get_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)

def min_sum_product(n):
    if n == 1:
        return 2

    factors = get_factors(n)
    min_sum = float("inf")
    for size in range(2, min(5, len(factors) + 1)):  
        for subset in itertools.combinations(factors, size):
            if math.lcm(*subset) == n:
                min_sum = min(min_sum, sum(subset))

    return min_sum if min_sum != float('inf') else n + 1  


input_value = int(stdin.readline().strip())
case = 1
while input_value != 0:
    print(f"Case {case}: {min_sum_product(input_value)}")
    case += 1
    input_value = int(stdin.readline().strip())