from collections import deque, Counter
import heapq
from sys import stdin
import io
import math

def bfs(initial_owned, initial_duplicates, friends):
    max_unique = len(set(initial_owned))
    visited = set()
    q = deque()
    friend_counters = [Counter(friend) for friend in friends]
    q.append((frozenset(initial_owned),tuple(sorted(initial_duplicates.items())),tuple(tuple(sorted(fc.items())) for fc in friend_counters)))#testing frozenset, it should let me append to a list

    while q:
        owned, dup_items, friends_state = q.popleft()
        duplicates = Counter(dict(dup_items))
        state_id = (owned, dup_items, friends_state)
        if state_id in visited:
            continue
        visited.add(state_id)
        max_unique = max(max_unique, len(owned))
        current_friends = [Counter(dict(friend)) for friend in friends_state]
        for idx,friend_counter in enumerate(current_friends):
            # print(f"idx: {idx}, friend_counter: {friend_counter}, owned={owned}")
            friend_owned=set(friend_counter.elements())
            friend_duplicates=[s for s, c in friend_counter.items() if c > 1]

            for s_bob in duplicates:
                if duplicates[s_bob]== 0 or s_bob in friend_owned:
                    continue
                for s_friend in friend_duplicates:
                    if s_friend==s_bob:
                        continue
                    new_owned =set(owned)
                    new_duplicates= Counter(duplicates)
                    new_friends =[Counter(dict(fc)) for fc in current_friends]
                    new_duplicates[s_bob] -=1
                    if new_duplicates[s_bob]==0:
                        del new_duplicates[s_bob]
                    if s_friend not in new_owned:
                        new_owned.add(s_friend)
                    else:
                        new_duplicates[s_friend]+=1
                    new_friends[idx][s_bob]+=1
                    new_friends[idx][s_friend] -=1
                    if new_friends[idx][s_friend]==0:
                        del new_friends[idx][s_friend]
                    q.append((
                        frozenset(new_owned),
                        tuple(sorted(new_duplicates.items())),
                        tuple(tuple(sorted(fc.items())) for fc in new_friends)
                    ))
    return max_unique




stdin = io.StringIO("""2
2 5
6 1 1 1 1 1 1
3 1 2 2
3 5
4 1 2 1 1
3 2 2 2
5 1 3 4 4 3
""")


cases = int(stdin.readline())
for i in range(cases):
    n, m = map(int, stdin.readline().split()) 
    my_line = list(map(int, stdin.readline().split()))
    my_stickers = my_line[1:]
    my_counter = Counter(my_stickers)
    my_owned = set(my_counter.keys())
    my_duplicates = Counter({k: v - 1 for k, v in my_counter.items() if v > 1})
    friends = []
    for _ in range(n - 1):
        line = list(map(int, stdin.readline().split()))
        friends.append(line[1:])
    # print(my_stickers)
    # print(friends)


    result = bfs(my_owned, my_duplicates, friends)
    print(f"Case #{i+1}: {result}")
