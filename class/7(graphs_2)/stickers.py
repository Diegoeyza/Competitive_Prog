from collections import deque, Counter

def bfs(initial_owned, initial_duplicates, friends):
    max_unique = len(initial_owned)
    visited = set()
    q = deque()
    q.append((frozenset(initial_owned), tuple(sorted(initial_duplicates.items()))))

    while q:
        owned, dup_items = q.popleft()
        duplicates = Counter(dict(dup_items))
        state_id = (owned, dup_items)
        if state_id in visited:
            continue
        visited.add(state_id)
        max_unique = max(max_unique, len(owned))

        for friend in friends:
            friend_counter = Counter(friend)
            friend_owned = set(friend)
            friend_duplicates = [s for s, c in friend_counter.items() if c > 1]
            for s_bob in duplicates:
                if duplicates[s_bob] == 0:
                    continue
                for s_friend in friend_duplicates:
                    if s_bob not in friend_owned and s_friend != s_bob:
                        new_owned = set(owned)
                        new_duplicates = Counter(duplicates)
                        new_duplicates[s_bob] -= 1
                        if new_duplicates[s_bob] == 0:
                            del new_duplicates[s_bob]

                        if s_friend not in new_owned:
                            new_owned.add(s_friend)
                        else:
                            new_duplicates[s_friend] += 1
                        q.append((frozenset(new_owned), tuple(sorted(new_duplicates.items()))))
    return max_unique
