from sys import stdin
import io
import math
import functools

def kadane(nums):
    max_sum=float('-inf')
    current_sum=0
    start=end=temp_start= 0
    max_length=0

    for i,num in enumerate(nums):
        if current_sum+num>num:
            current_sum+=num
        else:
            current_sum=num
            temp_start=i
        current_length=i-temp_start+1
        if current_sum>max_sum or (current_sum==max_sum and current_length>max_length):
            max_sum=current_sum
            start, end=temp_start, i
            max_length=current_length

    return max_sum,[start+1,end+2]


stdin = io.StringIO("""3
3
-1
6
10
4
-5
4
-3
4
4
-4
4
-5
4
-2
-3
-4""")



routes = int(stdin.readline().strip())

for route in range(routes):
    stops=int(stdin.readline().strip())
    stop_list=[]
    for i in range (stops-1):
        stop_list.append(int(stdin.readline().strip()))
    # print(stop_list)
    sol=kadane(stop_list)
    if sol[0]>0:
        print(f"The nicest part of route {route+1} is between stops {sol[1][0]} and {sol[1][1]}")
    else:
        print(f"Route {route+1} has no nice parts")
