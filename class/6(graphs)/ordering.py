from sys import stdin
import io

stdin = io.StringIO("""2

A B C
A<B B<C C<A

A B
A<B B<A

""")

def all_sequences(graph, in_degree, sequence, visited, results, variables):
    added=False
    for node in sorted(variables): 
        if not visited[node] and in_degree[node] ==0:
            visited[node] = True
            sequence.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor]-= 1
            all_sequences(graph, in_degree, sequence, visited, results, variables)
            for neighbor in graph[node]:
                in_degree[neighbor]+=1
            visited[node]=False
            sequence.pop()
            added = True
    if not added and len(sequence) == len(variables):
        results.append(' '.join(sequence))


cases = int(stdin.readline())
for aux in range(cases):
    stdin.readline()
    graph = {}
    in_degree ={}
    variables =stdin.readline().split()
    data =stdin.readline().split()

    for var in variables:
        graph[var] = []
        in_degree[var] = 0

    for rule in data:
        a, b = rule[0], rule[2]
        graph[a].append(b)
        in_degree[b] += 1
    visited={var: False for var in variables}
    results =[]
    all_sequences(graph, in_degree.copy(), [], visited, results, variables)

    if results:
        for res in results:
            print(res)
    else:
        print("NO")  #caso bordeeeeeee maldito
    if aux < cases - 1:
        print()
