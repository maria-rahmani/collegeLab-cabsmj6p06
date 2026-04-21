import heapq

def dijkstra(graph, start, end):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've found a better path already
        if current_distance > distances[current_node]:
            continue

        # Stop when reaching the destination
        if current_node == end:
            break

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes.get(current)
    
    return path, distances[end]

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8},
    'D': {}
}
start_node = 'A'
end_node = 'D'

path, distance = dijkstra(graph, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {path}")
print(f"Total distance: {distance}")   
