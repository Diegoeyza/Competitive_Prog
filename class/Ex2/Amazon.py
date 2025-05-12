import heapq, io
from collections import deque, defaultdict
import math
from sys import stdin

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


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


    def bfs_reachable(self, start, total_nodes):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return len(visited) == total_nodes

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def find_2_closest(current_idx, coords):
    dists = []
    for i, point in enumerate(coords):
        if i!=current_idx:
            dist=distance(coords[current_idx], point)
            dists.append((dist, point[0], point[1], i))

    dists.sort()
    # print(dists)
    return [dists[0][3], dists[1][3]] 




stdin = io.StringIO("""4
1 0 0 1 -1 0 0 -1
8
1 0 1 1 0 1 -1 1 -1 0 -1 -1 0 -1 1 -1
6
0 3 0 4 1 3 -1 3 -1 -4 -2 -5
0
""")

while True:
    line = stdin.readline()
    if not line:
        break
    c = int(line.strip())
    if c == 0:
        break

    coords_raw= list(map(int, stdin.readline().split()))
    coords =[(coords_raw[i], coords_raw[i + 1]) for i in range(0, len(coords_raw), 2)]

    graph=Graph()
    for i in range(c):
        closest = find_2_closest(i,coords)
        for neighbor in closest:
            graph.add_edge(i,neighbor)

    if graph.bfs_reachable(0,c):
        print(f"All stations are reachable.")
    else:
        print(f"There are stations that are unreachable.")
