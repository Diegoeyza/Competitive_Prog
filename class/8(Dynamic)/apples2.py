from sys import stdin
import io
import math

def calc_apples(n, k):
    dp = [[0]*(n+2) for aux in range(n+2)]
    for length in range(2,n+ 1):
        for L in range(1,n-length+ 2):
            R=L+length-1
            s =R-L+ 1
            best=float('inf')
            for i in range(L, R + 1):
                cost=(k + i) * s + dp[L][i - 1] + dp[i + 1][R]
                best=min(best, cost)
            dp[L][R]=best
    return dp[1][n]

stdin = io.StringIO("""10
200 200
300 50
14 20
95 140
110 220
50 65
10 0
500 0
60 50
18 13
""")


test_cases = int(stdin.readline().strip())
for i in range (test_cases):
    n, k = map(int, stdin.readline().split())
    print(f"Case {i+1}: {calc_apples(n,k)}")