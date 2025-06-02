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


stdin = io.StringIO("""3
1 2 1 2 1
2 3 4 1 2 5 10 50 3 50
3 5 2 7 1 7 5 2 8 9 1 25 15 8 3 1 38 45 8 1
""")


cases = int(stdin.readline().strip())

weights = sorted(list(map(int, stdin.readline().split())))
while len(weights)>0:
    # print(weights)
    print(bag_ordering(weights))
    try:
        weights = sorted(list(map(int, stdin.readline().split())))
    except:
        break