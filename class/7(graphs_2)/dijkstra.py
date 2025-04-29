import heapq

def dijkstra(graph, start):
    # graph: dict of node -> list of (neighbor, weight)
    # start: starting node
    
    # Initialize distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue: (distance_so_far, node)
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # If we already found a better path before, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3)],
    'E': [('C', 8), ('D', 3)]
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)