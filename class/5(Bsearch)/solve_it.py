from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""0 0 0 0 -2 1
1 0 0 0 -1 2
1 -1 1 -1 -1 1
""")

EPS = 1E-8
    
def has_sol(p,q,r,s,t,u):
    max=p*math.exp(-1)+q*math.sin(1)+r*math.cos(1)+s*math.tan(1)+t*1**2+u
    min=p*math.exp(0)+q*math.sin(0)+r*math.cos(0)+s*math.tan(0)+t*(0)**2+u
    if (max*min<=0):
        return True
    return False


def ecuation(p,q,r,s,t,u):
    x=0.5
    top=1
    floor=0
    if (has_sol(p,q,r,s,t,u)==False):
        return print("No solution")
    while x!=0:
        eq=p*math.exp(-x)+q*math.sin(x)+r*math.cos(x)+s*math.tan(x)+t*x**2+u
        # print(eq)
        if (eq<EPS and eq>-EPS):
            return print(f"{x:.4f}")
        elif (eq>0):
            floor=x
            x=x+(top-x)/2
            # print(x)
        elif (eq<0):
            top=x
            x=floor+(x-floor)/2
            # print(x)



p,q,r,s,t,u = [int(item) for item in stdin.readline().split()]
while p!="":
    # print(p)
    ecuation(p,q,r,s,t,u)


    try:
        p,q,r,s,t,u = [int(item) for item in stdin.readline().split()]
    except:
        p=""
    

    