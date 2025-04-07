from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""2
8 11 2 3 5
299 300 9 1 2 3 4 5 60 130 260 270""")

def zombies(cmin,cmax,n,insects):
    for i in range (n):
        c=combinations(insects,i+1)
        for comb in c:
            # print(comb)
            # print(sum(comb))
            if (sum(comb)>=cmin and sum(comb)<=cmax):
                print("Sallow swallow swallows.")
                return
    print("Sallow swallow wallows in dust.")
    


cases = int(stdin.readline().strip())
for i in range (cases):
    vals= [int(i) for i in stdin.readline().split()]
    cmin=vals[0]
    cmax=vals[1]
    n=vals[2]
    insects=vals[3:]
    zombies(cmin,cmax,n,insects)
    