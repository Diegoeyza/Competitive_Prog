from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""324534536
48223023
847223
1231298
2147483647
1000000
99999999
0
""")




m = int(stdin.readline().strip())
while m!=0:
    # print(m)
    closest=0
    for i in range(32):
        for j in range(0,32):
            val=(2**i)*(3**j)
            # print(f"val={val}, closest={closest}") 
            if closest==0 and val>=m:
                closest=val
            elif (val>=m and val<closest):
                closest=val
    print(closest)
    m=int(stdin.readline().strip())
    

    