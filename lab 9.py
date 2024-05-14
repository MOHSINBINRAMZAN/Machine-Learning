<<<<<<< HEAD
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

def shortest_path(predecessors, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = predecessors[target]
    return path

# Example usage:
graph = {
    'Memphis': {'Nashville': 15, 'Atlanta': 10, 'Mobile': 7, 'New Orleans': 3},
    'New Orleans': {'Mobile': 2},
    'Mobile': {'Savannah': 6, 'Atlanta': 2},
    'Savannah': {'Atlanta': 1},
    'Atlanta': {'Nashville': 2},
    'Nashville': {},  # Add an empty entry for Nashville
}

start_node = 'Memphis'
end_node = 'Nashville'

distances, predecessors = dijkstra(graph, start_node)

# Check if the end_node is in the graph
if end_node in distances:
    shortest_path_result = shortest_path(predecessors, end_node)
    print("Shortest distances:", distances)
    print("Shortest path from {} to {}: {}".format(start_node, end_node, shortest_path_result))
else:
    print(f"No path found from {start_node} to {end_node}.")
=======
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

def shortest_path(predecessors, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = predecessors[target]
    return path

# Example usage:
graph = {
    'Memphis': {'Nashville': 15, 'Atlanta': 10, 'Mobile': 7, 'New Orleans': 3},
    'New Orleans': {'Mobile': 2},
    'Mobile': {'Savannah': 6, 'Atlanta': 2},
    'Savannah': {'Atlanta': 1},
    'Atlanta': {'Nashville': 2},
    'Nashville': {},  # Add an empty entry for Nashville
}

start_node = 'Memphis'
end_node = 'Nashville'

distances, predecessors = dijkstra(graph, start_node)

# Check if the end_node is in the graph
if end_node in distances:
    shortest_path_result = shortest_path(predecessors, end_node)
    print("Shortest distances:", distances)
    print("Shortest path from {} to {}: {}".format(start_node, end_node, shortest_path_result))
else:
    print(f"No path found from {start_node} to {end_node}.")
>>>>>>> e0d3d757fa858b53a002a1dad5388be5b4af4699
