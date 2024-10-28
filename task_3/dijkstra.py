from graph import Graph
from min_heap import MinHeap
from typing import Dict

def dijkstra(graph: Graph, start: int) -> Dict[int, float]:
    """
    Perform Dijkstra's algorithm to find the shortest paths from a starting vertex.

    Parameters:
        graph (Graph): The graph to search.
        start (int): The starting vertex.

    Returns:
        Dict[int, float]: A dictionary of shortest paths from the starting vertex to all other vertices.
    """
    min_heap = MinHeap()
    min_heap.add_task(start, 0)

    distances = {vertex: float('inf') for vertex in graph.graph}
    distances[start] = 0
    
    while not min_heap.is_empty():
        current_vertex, current_distance = min_heap.pop_task()
        
        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight
            
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                min_heap.add_task(neighbor, distance)
    
    return distances