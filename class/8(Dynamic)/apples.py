from sys import stdin
import io
import math
import functools
def min_total_cost(n, k):
    total_cost = 0
    weights = [k + i for i in range(1, n + 1)]  # 1-based indexing

    for target in range(1, n + 1):  # Assume apple at `target` is sweet
        cost = 0
        visited = set()

        # Always start with the smallest apple
        if target == 1:
            cost += weights[0]
            # print(cost)
        else:
            cost += weights[0]
            visited.add(1)

            l = 2
            r = n

            while l <= r:
                mid = (l + r) // 2
                if (r - l + 1) % 2 == 0 and mid+1!=n:
                    mid += 1  # middle+1 if even
                # print(f"mid={mid}")
                
                if len(visited)==1 and n==2:
                    break

                elif mid == target:
                    # found the sweet apple
                    cost += weights[mid - 1]
                    break
                elif mid < target:
                    # bitter → go right
                    cost += weights[mid - 1]
                    visited.add(mid)
                    if mid + 1 == target:
                        # no need to eat target, it's the only one left
                        break
                    l = mid + 1
                else:
                    # sour → go left
                    cost += weights[mid - 1]
                    visited.add(mid)
                    if mid - 1 == target:
                        break
                    r = mid - 1

        total_cost += cost

    return total_cost

def simulate_middle_start(n, k):
    total_cost = 0
    weights = [k + i for i in range(1, n + 1)]  # 1-based indexing

    for target in range(1, n + 1):  # assuming apple at 'target' is sweet
        cost = 0
        l, r = 1, n

        # find initial middle index (middle-1 if even length)
        length = r - l + 1
        if length % 2 == 0:
            mid = l + length // 2 - 1
        else:
            mid = l + length // 2

        while True:
            cost += weights[mid - 1]
            if mid == target:
                # found sweet apple
                break
            elif mid < target:
                # apple at mid is bitter, sweet is to the right
                l = mid + 1
                length = r - l + 1
                if length == 1:
                    # only one left to right, which must be sweet
                    # no need to eat it
                    break
                if length % 2 == 0:
                    mid = l + length // 2 - 1
                else:
                    mid = l + length // 2
            else:
                # apple at mid is sour, sweet is to the left
                r = mid - 1
                length = r - l + 1
                if length == 1:
                    # only one left to left, which must be sweet
                    # no need to eat it
                    break
                if length % 2 == 0:
                    mid = l + length // 2 - 1
                else:
                    mid = l + length // 2

        total_cost += cost

    return total_cost







def calculate_apples(n,k):
    weight=0

    return weight

stdin = io.StringIO("""4
2 0
3 0
4 0
5 0
10 20""")


test_cases = int(stdin.readline().strip())
for i in range (test_cases):
    n, k = map(int, stdin.readline().split())
    print(n,k)
    min_cost=min(min_total_cost(n,k),simulate_middle_start(n,k))
    print(f"cost start= {min_total_cost(n,k)}")
    print(f"cost mid= {simulate_middle_start(n,k)}")
    print(f"cost= {min_cost}")