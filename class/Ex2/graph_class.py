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

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                yield u
                for v, _ in reversed(self.graph[u]):
                    stack.append(v)
    
    #returns the first path it finds with the lowest cost to every node from start, regardless of the length of the path
    def dijkstra(self, start):
        dist = {}
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in self.graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return dist
    
    #same as the above, but this one returns the distance to one node, not to all, so its the shortest distance from A to B. it returns [[path],cost]
    def dijkstra_single(self, start, end):
        dist = {}
        prev = {}
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            if u == end:
                break
            for v, w in self.graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
                    if v not in prev or d + w < dist.get(v, float('inf')):
                        prev[v] = u
        if end not in dist:
            return None, float('inf')
        path = []
        at = end
        while at != start:
            path.append(at)
            at = prev[at]
        path.append(start)
        path.reverse()
        return path, dist[end]

    #returns int: the total maximum flow from source node `s` to sink node `t`
    def max_flow(self, s, t):
        parent = {}

        def bfs():
            visited = set()
            queue = deque([s])
            visited.add(s)
            parent.clear()

            while queue:
                u = queue.popleft()
                for v in self.capacity[u]:
                    if v not in visited and self.capacity[u][v] > 0:
                        visited.add(v)
                        parent[v] = u
                        if v == t:
                            return True
                        queue.append(v)
            return False

        flow = 0
        while bfs():
            path_flow = float('inf')
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u
            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v].setdefault(u, 0)
                self.capacity[v][u] += path_flow
                v = u
            flow += path_flow
        return flow

    #returns a tuple with 2 vals: (flow_sent, total_cost)
    def min_cost_flow(self, s, t, max_flow):
        n = defaultdict(lambda: float('inf'))
        flow = 0
        cost_total = 0

        def spfa():
            dist = defaultdict(lambda: float('inf'))
            in_queue = defaultdict(bool)
            parent = {}
            dist[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                in_queue[u] = False
                for v in self.capacity[u]:
                    if self.capacity[u][v] > 0:
                        new_dist = dist[u] + self.cost[u][v]
                        if new_dist < dist[v]:
                            dist[v] = new_dist
                            parent[v] = u
                            if not in_queue[v]:
                                q.append(v)
                                in_queue[v] = True
            return dist, parent

        while flow < max_flow:
            dist, parent = spfa()
            if t not in parent:
                break
            # Find bottleneck
            path_flow = max_flow - flow
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u
            # Update capacities
            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v].setdefault(u, 0)
                self.capacity[v][u] += path_flow
                cost_total += path_flow * self.cost[u][v]
                v = u
            flow += path_flow
        return flow, cost_total
    
    #returns every path from a to b with their associated cost, in the format [[[path],cost],[[path],cost]]
    def all_paths_with_cost(self, start, end):
        def dfs(u, path, cost, visited):
            if u == end:
                result.append((list(path), cost))
                return
            for v, w in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    path.append(v)
                    dfs(v, path, cost + w, visited)
                    path.pop()
                    visited.remove(v)

        result = []
        visited = set([start])
        dfs(start, [start], 0, visited)
        return result
    

    def bipartite(self, start, color, colors):
        """
        Check if the connected component starting from `start` is bipartite.
        Uses BFS to attempt a 2-coloring of the graph.
        
        Args:
            start: The starting node for the component.
            color: The initial color to assign to the starting node (0 or 1).
            colors: A dictionary mapping nodes to their color (-1 if unvisited).

        Returns:
            The size of the larger color class if the component is bipartite,
            otherwise 0 if the component contains an odd cycle.
        """
        queue = deque([start])
        colors[start] = color
        count = [0, 0]
        count[color] += 1
        component_nodes = [start]
        is_valid = True

        while queue:
            u = queue.popleft()
            for v, _ in self.graph[u]:  # Use self.graph to access adjacency list
                if colors[v] == -1:
                    colors[v] = 1 - colors[u]
                    count[colors[v]] += 1
                    queue.append(v)
                    component_nodes.append(v)
                elif colors[v] == colors[u]:
                    is_valid = False

        for node in component_nodes:
            colors[node] = 2  # Mark as processed

        return max(count) if is_valid else 0


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
    


    def print_graph(self):
        print("Graph adjacency list:")
        for u in self.graph:
            for v, w in self.graph[u]:
                print(f"  {u} -> {v} (weight: {w})")
        
        if self.capacity:
            print("\nCapacities:")
            for u in self.capacity:
                for v in self.capacity[u]:
                    print(f"  {u} -> {v} (capacity: {self.capacity[u][v]})")

        if self.cost:
            print("\nCosts:")
            for u in self.cost:
                for v in self.cost[u]:
                    print(f"  {u} -> {v} (cost: {self.cost[u][v]})")




    def clear(self):
        self.graph.clear()
        self.capacity.clear()
        self.cost.clear()

#all paths
# g = Graph(directed=True)
# g.add_edge('A', 'B', 1)
# g.add_edge('A', 'C', 2)
# g.add_edge('B', 'C', 1)
# g.add_edge('C', 'D', 3)
# g.add_edge('B', 'D', 5)

# paths = g.all_paths_with_cost('A', 'D')
# for path, cost in paths:
#     print("Path:", path, "Cost:", cost)

# # max flow
# g = Graph(directed=True)

# # Add edges with capacities
# g.add_edge('S', 'A', cap=10)
# g.add_edge('S', 'B', cap=5)
# g.add_edge('A', 'B', cap=15)
# g.add_edge('A', 'T', cap=10)
# g.add_edge('B', 'T', cap=10)

# # Compute max flow
# maxflow = g.max_flow('S', 'T')
# print("Maximum Flow:", maxflow)


#bipartite

# Create a graph instance
g = Graph(directed=False)

# Add edges to create a bipartite graph (e.g., a square)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

# Prepare colors dictionary (-1 means unvisited)
colors = defaultdict(lambda: -1)

# Call the bipartite method on one of the nodes
largest_color_class = g.bipartite(start=1, color=0, colors=colors)

print("Is bipartite:", largest_color_class > 0)
print("Size of largest color class:", largest_color_class)

#sol
# 1 — 2
# |   |
# 4 — 3

# It's a cycle with 4 nodes — an even cycle, which is always bipartite.

# What Bipartite Means
# A bipartite graph is one where:
# You can split the nodes into two sets (say, Red and Blue),
# Such that no edge connects two nodes of the same set.

# This is equivalent to saying:
# The graph can be 2-colored with no two adjacent nodes sharing the same color.

# The bipartite Method:
# The method does the following:
# Starts coloring node 1 with color 0 (say, Red).
# Its neighbors (node 2 and 4) get color 1 (Blue).
# Then, node 2's neighbor 3 gets color 0 (Red again).
# Node 3's neighbor 4 already has color 1, which is fine (not equal to 3’s color 0).
# No conflicts are found → it's bipartite.

# Why "size of largest color class = 2"?
# The method counts how many nodes got color 0 and how many got 1:
# Color 0: nodes 1, 3 → 2 nodes
# Color 1: nodes 2, 4 → 2 nodes
# → max(count) is 2, which is the result.

# So:
# Yes, it's bipartite ✅
# Largest color class size = 2 🔢


