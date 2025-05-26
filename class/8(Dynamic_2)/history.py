from sys import stdin
import io
import math
import functools
import itertools

def bag_ordering(bags):
    if sum(bags)%2 != 0:
        return "NO"
    else:
        target=sum(bags)/2
        for length in range (len(bags)):
            valid=False
            for subset in itertools.combinations(bags, length):
                # print(subset)
                ans=sum(subset)
                if ans==target:
                    return "YES"
                if ans<target:
                    valid=True
            if not (valid):
                return "NO"
            
    return "NO"


stdin = io.StringIO("""4
4 2 3 1
1 3 2 4
3 2 1 4
2 3 4 1
10
3 1 2 4 9 5 10 6 8 7
1 2 3 4 5 6 7 8 9 10
4 7 2 3 10 6 9 1 5 8
3 1 2 4 9 5 10 6 8 7
2 10 1 3 8 4 9 5 7 6
""")

def maximum_subsequence(order):
    length = len(order)
    accumulated = [1]*length

    for i in range(length):
        for j in range(i):
            if order[i]>order[j]:
                accumulated[i]=max(accumulated[i], accumulated[j] + 1)

    return max(accumulated) if accumulated else 0




cases = int(stdin.readline().strip())
while cases!="":
    base=list(map(int, stdin.readline().split()))
    dict={}
    for i in range (cases):
        dict[base[i]]=i+1
    # print(dict)

    student=list(map(int, stdin.readline().split()))
    while len(student)>1:
        order=[]
        for i in range(cases):
            order.append(dict[student[i]])
        # print(order)

        # print(student)
        print(maximum_subsequence(order))
        student=list(map(int, stdin.readline().split()))
    if len(student)==0:
        cases=""
    else:
        cases=student[0]

