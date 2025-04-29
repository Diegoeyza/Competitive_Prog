import heapq
from sys import stdin
import io
import math

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

def distance(a,b):
    x1, y1=map(int, a.split(','))
    x2, y2=map(int, b.split(','))
    return math.hypot(x1 - x2, y1 - y2)

stdin = io.StringIO("""1

0 0 10000 1000
0 200 5000 200 7000 200 -1 -1
2000 600 5000 600 10000 600 -1 -1
""")

cases = int(stdin.readline())
stdin.readline()

for case_n in range(cases):
    coords= stdin.readline().split()
    home=",".join(coords[:2])
    school=",".join(coords[2:])
    
    points={home, school}
    subway_lines =[]
    
    line =stdin.readline().split()
    
    while line:
        subway = []
        for i in range(0, len(line) - 2, 2):
            if line[i] == "-1" and line[i+1] == "-1":
                break
            point = ",".join(line[i:i+2])
            subway.append(point)
            points.add(point)
        if subway:
            subway_lines.append(subway)
        line = stdin.readline().split()
        if not line:
            break
    

    graph = {p: [] for p in points}

    for line in subway_lines:
        for i in range(len(line) - 1):
            d =distance(line[i], line[i+1])
            time=d/(40000/60) 
            graph[line[i]].append((line[i+1], time))
            graph[line[i+1]].append((line[i], time))
    # print(graph)
    point_list =list(points)
    for i in range(len(point_list)):
        for j in range(i+1, len(point_list)):
            a,b= point_list[i], point_list[j]
            d=distance(a, b)
            time= d/(10000/60)
            graph[a].append((b, time))
            graph[b].append((a, time))
    print(graph["0,200"])
    
    path, total_time=dijkstra(graph,home, school)
    
    print(f"{round(total_time)}\n")










