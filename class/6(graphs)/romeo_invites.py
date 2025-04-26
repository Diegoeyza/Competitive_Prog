from sys import stdin
import io

stdin = io.StringIO("""3

5
1 3
1 1
0
1 5
0

8
2 4 5
2 1 3
0
0
0
1 3
0
1 5

3
2 2 3
1 3
1 1
""")

def kinda_red_black(graph, node, color, colors):
    queue = [node]
    colors[node] = color
    count = [0, 0]
    count[color] += 1
    component_nodes = [node]
    is_valid = True

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if colors[v] == -1:
                colors[v] = 1 - colors[u]
                count[colors[v]] += 1
                queue.append(v)
                component_nodes.append(v)
            elif colors[v] == colors[u]:
                is_valid = False

    for node in component_nodes:
        colors[node] = 2  
    
    if is_valid:
        return max(count)
    return 0









def calc_inv():
    cases = int(stdin.readline())
    stdin.readline()
    for i in range(cases):
        if i > 0:
            stdin.readline()
        n = int(stdin.readline())
        graph = [[] for aux in range(n)]
        for j in range(n):
            data = [int(item) for item in stdin.readline().split()]
            # print(data)
            for enemy in data[1:]:
                if 1 <= enemy <= n:
                    graph[j].append(enemy - 1)
                    graph[enemy - 1].append(j)

        colors = [-1] * n
        total = 0
        for i in range(n):
            if colors[i] == -1:
                res = kinda_red_black(graph, i, 0, colors)
                if res > 0:
                    total += res
        # print("total")
        print(total)

calc_inv()
