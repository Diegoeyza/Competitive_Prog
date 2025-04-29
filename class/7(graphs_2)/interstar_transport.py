import heapq
from sys import stdin
import io


# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     queue = [(0, start)]
#     path=[]
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#         if current_distance > distances[current_node]:
#             continue
#         for neighbor, weight in graph[current_node]:
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 path.append(current_node)
#                 distances[neighbor] = distance
#                 heapq.heappush(queue, (distance, neighbor))
#     return distances,current_node


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node 
                heapq.heappush(queue, (distance, neighbor))
    path = []
    node = end
    if previous[node] is not None or node == start: 
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
    return path, distances[end]



stdin = io.StringIO("""5 7
A B 1
B C 2
C D 3
D E 2
E A 1
A D 3
A C 4
3
B D
A D
E C
""")

s,p = [int(item) for item in stdin.readline().split()]
graph={}
for i in range(p):
    start, dest, price = stdin.readline().split()
    price = int(price)
    if start not in graph:
        graph[start] = [(dest, price)]
    else:
        graph[start].append((dest, price))
    if dest not in graph:
        graph[dest] = [(start, price)]
    else:
        graph[dest].append((start, price))
# print(graph)
q_count=int(stdin.readline())
for i in range (q_count):
    start,end = [item for item in stdin.readline().split()]
    path,cost=dijkstra(graph,start,end)
    print(" ".join(path))


