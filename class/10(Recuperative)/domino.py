from sys import stdin
import io
import math
from functools import lru_cache



stdin = io.StringIO("""3
4
0 1
3 4
2 1
5 6
2 2
3 2
2
4
0 1
3 4
1 4
4 4
3 2
5 6
0""")


def check(n, pieces):
    left=tuple(pieces[0])
    right=tuple(pieces[-1])
    pool=[tuple(p) for p in pieces[1:-1]]
    m=len(pool)
    want_start=left[1]
    want_end=right[0]
    @lru_cache(None)
    def dfs(pos,need, used_mask):
        if pos==n:
            return need==want_end

        for i in range(m):
            if (used_mask>>i)&1:
                continue
            a,b=pool[i]
            if a==need and dfs(pos+1,b,used_mask|(1 << i)): #using bitmask, same as the problem from last week, review this for the test
                return True
            if b==need and dfs(pos+1, a, used_mask| (1 << i)):
                return True
        return False

    result = dfs(0, want_start, 0)
    print("YES" if result else "NO")
    return result

spaces = int(stdin.readline().strip())
while spaces!=0:
    m=int(stdin.readline().strip())
    pieces=[[] for _ in range(m+2)]
    pieces[0]=list(map(int, stdin.readline().split()))
    pieces[-1]=list(map(int, stdin.readline().split()))
    for p in range (m):
        pieces[p+1]=list(map(int, stdin.readline().split()))
    # print(pieces)
    check(spaces,pieces)
    try:  
        spaces = int(stdin.readline().strip())
    except:
        spaces=0

