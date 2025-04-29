import heapq
from sys import stdin
import io

# did this one using kushala and union disjoint class from the class jupyter
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def minimum_cost(N, edges):
    edges.sort()
    uf = UnionFind(N + 1)

    total_cost = 0
    for cost, node1, node2 in edges:
        if uf.union(node1, node2):
            total_cost += cost

    return total_cost

stdin = io.StringIO("""7
4 5 6
7 3 8
7 4 9
5 6 12
2 6 15
1 4 18
2
1 7 30
1 3 3
10
4 5 6
7 3 8
7 4 9
5 6 12
6 7 14
2 6 15
7 4 17
1 4 18
2 3 20
4 1 20

11
5 10 2
11 9 3
6 5 5
8 2 10
7 4 12
4 9 12
11 2 13
5 9 14
3 2 14
2 1 15
10
5 3 14
4 9 8
6 7 29
3 6 11
9 7 15
10 8 28
2 11 25
2 5 14
9 11 1
3 7 4
14
5 10 2
11 9 3
6 5 5
8 2 10
7 4 12
4 9 12
11 2 13
5 9 14
3 2 14
2 1 15
5 7 17
3 9 22
10 3 24
9 3 28
""")

N = (stdin.readline().strip())
while N:
    N = int(N)
    graph1 = []
    og_cost=0
    for i in range(N - 1):
        comp1, comp2, cost = [int(item) for item in stdin.readline().split()]
        graph1.append([cost, comp1, comp2])
        og_cost+=cost

    # print("Original Graph:", graph1)
    print(og_cost)

    graph2 = []
    K = int(stdin.readline().strip())
    for i in range(K):
        comp1, comp2, cost = [int(item) for item in stdin.readline().split()]
        graph2.append([cost, comp1, comp2])

    M = int(stdin.readline().strip())
    for i in range(M):
        comp1, comp2, cost = [int(item) for item in stdin.readline().split()]
        graph2.append([cost, comp1, comp2])
    combined_edges = graph1 + graph2
    result = minimum_cost(N, combined_edges)
    print(result)
    stdin.readline()

    N = (stdin.readline().strip())


