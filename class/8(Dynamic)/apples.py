from sys import stdin
import io
import math
import functools

def simulate_custom_start(n, k, start_idx):
    total_cost=0
    weights=[k+i for i in range(1,n+1)] 

    for target in range(1,n+1):
        cost= 0
        l,r= 1,n
        visited= set()

        idx=start_idx
        cost+=weights[idx-1]
        visited.add(idx)

        if idx == target:
            total_cost += cost
            continue

        if idx < target:
            l=idx +1
        else:
            r=idx-1

        while l <= r:
            length= r-l+1
            if length==1:
                break
            if length%2==0:
                mid = l+length//2-1
            else:
                mid=l+length//2
            cost+=weights[mid-1]
            visited.add(mid)
            if mid==target:
                break
            elif mid<target:
                l =mid+1
            else:
                r=mid-1
        total_cost+=cost

    return total_cost





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
18 13""")


test_cases = int(stdin.readline().strip())
for i in range (test_cases):
    n, k = map(int, stdin.readline().split())
    # print(n,k)
    # min_cost=min(min_total_cost(n,k),simulate_middle_start(n,k))
    # print(f"cost start= {min_total_cost(n,k)}")
    # print(f"cost mid= {simulate_middle_start(n,k)}")
    if n==18:
        for j in range(n):
            if simulate_custom_start(n,k,j+1)==1228:
                print("possible")
            if j==0:
                minimum=simulate_custom_start(n,k,j+1)
            else:
                minimum=min(minimum,simulate_custom_start(n,k,j+1))
        print(f"Case {i+1}: {minimum}")
        # print(f"cost= {min_cost}")

'''
Case 1: 374369
Case 2: 407876
Case 3: 1036
Case 4: 92924
Case 5: 163377
Case 6: 19588
Case 7: 123
Case 8: 936327
Case 9: 21891
Case 10: 1228
'''