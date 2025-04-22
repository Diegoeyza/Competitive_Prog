from sys import stdin
import io


# stdin = io.StringIO("""7
# 1 2 0
# 2 3 4 0
# 3 1 0
# 4 5 0
# 5 4 0
# 6 7 0
# 7 6 0
# 0
# 7 1 2 3 4 5 6 7
# 5
# 0
# 5 1 2 3 4 5
# 4
# 1 2 3 4 0
# 2 3 4 0
# 3 4 0
# 0
# 4 1 2 3 4
# 3
# 1 2 0
# 2 2 0
# 3 1 2 0
# 0
# 2 1 2
# 4
# 1 2 0
# 2 3 0
# 3 4 0
# 0
# 2 2 1
# 5
# 1 2 0
# 2 3 0
# 3 4 0
# 4 5 0
# 1 1 0
# 0
# 1 1
# 0
# """)


def dfs(graph, i, visited):
    neighs=graph[i]
    for neigh in neighs:
        if not visited[neigh]:
            visited[neigh] = True
            dfs(graph, neigh, visited)
            


N = int(stdin.readline().strip())
respuestas = []
while N > 0:
    graph = [[] for i in range(N)]
    row = [int(item) for item in stdin.readline().split()]
    while row[0] != 0:
        for i in range(1,len(row) - 1):
            graph[row[0] - 1].append(row[i] - 1)
        
        row = [int(item) for item in stdin.readline().split()]
    find = [int(item) for item in stdin.readline().split()]
    for j in range(1,len(find)):
        visited = [False] * N
        dfs(graph, find[j]-1, visited)
        not_v = sum([1 for i in visited if not i])
        row_not_v=[]
        for i in range (len(visited)):
            if visited[i]==False:
                row_not_v.append(i+1)
        print(f"{not_v} {' '.join(map(str, row_not_v))}")
    N = int(stdin.readline().strip())