import heapq, io
from collections import deque, defaultdict
import math
from sys import stdin

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.capacity = defaultdict(dict)  # For flow problems
        self.cost = defaultdict(dict)      # For min-cost flow
        self.directed = directed

    def add_edge(self, u, v, weight=1, cap=None, cost=None):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

        if cap is not None:
            self.capacity[u][v] = cap
            if not self.directed:
                self.capacity[v][u] = cap

        if cost is not None:
            self.cost[u][v] = cost
            if not self.directed:
                self.cost[v][u] = cost

    def update_edge(self, u, v, weight=None, cap=None, cost=None):
        # Update edge weight
        for i, (node, w) in enumerate(self.graph[u]):
            if node == v:
                if weight is not None:
                    self.graph[u][i] = (v, weight)
                break
        else:
            # Edge doesn't exist, add it
            self.graph[u].append((v, weight if weight is not None else 1))

        # Update capacity
        if cap is not None:
            self.capacity[u][v] = cap

        # Update cost
        if cost is not None:
            self.cost[u][v] = cost

        # For undirected graphs
        if not self.directed:
            self.update_edge(v, u, weight, cap, cost)

    def remove_edge(self, u, v):
        self.graph[u] = [(node, w) for node, w in self.graph[u] if node != v]
        self.capacity[u].pop(v, None)
        self.cost[u].pop(v, None)
        if not self.directed:
            self.remove_edge(v, u)

    def remove_node(self, u):
        self.graph.pop(u, None)
        self.capacity.pop(u, None)
        self.cost.pop(u, None)

        # Remove edges to u
        for v in list(self.graph):
            self.graph[v] = [(node, w) for node, w in self.graph[v] if node != u]
            self.capacity[v].pop(u, None)
            self.cost[v].pop(u, None)

    def has_node(self, u):
        return u in self.graph

    def has_edge(self, u, v):
        return any(node == v for node, _ in self.graph[u])


    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            u = queue.popleft()
            yield u
            for v, _ in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

                
    def traveling_merchant(self,start=0,end=None):
        if end is None:
            end=start

        nodes=list(self.graph.keys())
        if start not in nodes or end not in nodes:
            return [], float('inf')

        idx = {node: i for i, node in enumerate(nodes)}
        n   = len(nodes)

        #used as a base a function from stackoverflow because the travelling salesman problem does not support starting and ending at the same point, so it uses this when it fails and using bit shift it adds the return to the start
        def hamilton_path(s_idx, f_idx):
            dp= [[float('inf')]*n for aux in range(1<<n)]
            parent = [[-1]*n for aux in range(1<<n)]
            dp[1 << s_idx][s_idx] = 0

            for mask in range(1 << n):
                for u in range(n):
                    if not (mask & (1 << u)):
                        continue
                    for v_node, w in self.graph[nodes[u]]:
                        v = idx[v_node]
                        if mask & (1 << v):                
                            continue
                        nxt = mask | (1 << v)
                        new_cost = dp[mask][u] + w
                        if new_cost < dp[nxt][v]:
                            dp[nxt][v]= new_cost
                            parent[nxt][v]=u

            full = (1 << n) - 1
            cost = dp[full][f_idx]
            if cost == float('inf'):
                return [], cost

            mask = full
            cur  = f_idx
            path = []
            while cur != -1:
                path.append(nodes[cur])
                prv = parent[mask][cur]
                if prv == -1:
                    break
                mask ^= 1 << cur
                cur = prv
            path.reverse()
            return path, cost

        if start != end:
            return hamilton_path(idx[start], idx[end])
        
        best_cost = float('inf')
        best_path = []

        s_idx=idx[start]
        for last_node in nodes:
            if last_node==start:
                continue
            last_idx=idx[last_node]
            path, path_cost  = hamilton_path(s_idx, last_idx)
            if path_cost == float('inf'):
                continue
            back_cost = next((w for v,w in self.graph[last_node] if v==start), None)
            if back_cost is None:
                continue
            total = path_cost + back_cost
            if total<best_cost:
                best_cost=total
                best_path=path+[start]

        return best_path,best_cost


    def clear(self):
        self.graph.clear()
        self.capacity.clear()
        self.cost.clear()

stdin = io.StringIO("""1
10 10
1 1
4
2 3
5 5
9 4
6 5
""")

scenarios=int(stdin.readline().strip())

for scenario in range(scenarios):
    board =list(map(int, stdin.readline().split()))
    start =list(map(int, stdin.readline().split()))
    points= int(stdin.readline().strip())

    point_list=[start]
    for point in range(points):
        coords=list(map(int, stdin.readline().split()))
        point_list.append(coords)
    g=Graph(directed=True)
    for i in range(points + 1):
        for j in range(points + 1):
            if i != j:
                dist = abs(point_list[i][0]-point_list[j][0])+abs(point_list[i][1]-point_list[j][1])
                g.add_edge(i, j, dist)

    path,cost=g.traveling_merchant(start=0,end=0)
    print(f"The shortest path has length {cost}")
