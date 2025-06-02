from sys import stdin
import io
import math
import functools

@functools.lru_cache(None)   #improves recursive call speed
def something():
    return 0

stdin = io.StringIO("""1 2 3 -999999
-5 -2 2 -30 -999999
-8 -999999
-1 0 -2 -999999""")




vals = list(map(int, stdin.readline().split()))
while len(vals)>1:
    vals.pop()
    # print(vals)
    maximum=float("-inf")
    for i in range (len(vals)):
        mult=vals[i]
        current=mult
        # print(mult)
        for j in range (i,len(vals)):
            if i!=j:
                mult=mult*vals[j]
                current = mult if mult > current else current
                # print(mult)
        maximum = mult if mult >maximum else maximum
    print(maximum)

        



    vals = list(map(int, stdin.readline().split()))