from sys import stdin
import io

def shopping_bag(shopping_list, l_weight):
    n=len(shopping_list)
    current=[0]*(l_weight+1)
    for i in range(n):
        value, weight=shopping_list[i]
        for w in range(l_weight, weight-1,-1):
            current[w]=max(current[w],current[w-weight]+value)
    return current[l_weight]


# stdin = io.StringIO("""2
# 3
# 72 17
# 44 23
# 31 24
# 1
# 26
# 6
# 64 26
# 85 22
# 52 4
# 99 18
# 39 13
# 54 9
# 4
# 23
# 20
# 20
# 26""")

t= int(stdin.readline().strip())
# print(t)
for case in range(t):
    n_obj=int(stdin.readline().strip())
    shopping_list=[]
    for object in range(n_obj):
        shopping_list.append(tuple(map(int,stdin.readline().strip().split())))
    P=int(stdin.readline().strip())
    family=[]
    for p in range(P):
        person=int(stdin.readline().strip())
        family.append(shopping_bag(shopping_list, person))
    print(f"{sum(family)}")
