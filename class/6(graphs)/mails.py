from sys import stdin
import io

stdin = io.StringIO("""3
3
1 2
2 3
3 1
4
1 2
2 1
4 3
3 2
5
1 2
2 1
5 3
3 4
4 5
""")

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        # print(node)
        visited.add(node)
        dfs(graph, graph[node], visited)
    return visited





cases=int(stdin.readline())
for i in range (cases):
    martians=int(stdin.readline())
    graph={}
    for j in range (martians):
        row= [int(item) for item in stdin.readline().split()]
        graph[row[0]]=row[1]
    # print(graph)
    max_c=0
    max=0
    for j in range (martians):
        count=len(dfs(graph,j+1))
        if count>max_c:
            max=j+1
            max_c=count
    print(f"Case {i+1}: {max}")

# while V!=0:
#     graph={}
#     vert=set()
#     row= [int(item) for item in stdin.readline().split()]
#     while row[0]!=0:
#         graph[row[0]]=row[1:-1]
#         vert.add(row[0])
#         print(row)
#         # print(graph)
#         row= [int(item) for item in stdin.readline().split()]
#     find=[int(item) for item in stdin.readline().split()]
#     # print(f"find= {find}")
#     for item in find[1:]:
#         if len(graph.keys()):
#             visited=[]
#         else:
#             visited=(dfs(graph,item))
#             if item not in graph[item]:
#                 visited.remove(item)
#         # print(visited)
#         not_visited=[]
#         for n in vert:
#             if not (n in visited):
#                 not_visited.append(n) 
#         # print(not_visited)
#         out=f"{len(not_visited)}"
#         for val in not_visited:
#             out+=f" {val}"
#         print(out)
#     V=int(stdin.readline())


    