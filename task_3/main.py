from graph import Graph
from dijkstra import dijkstra

def main():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 5)
    
    for vertex in range(4):
        g.add_edge(vertex, vertex, 0)

    start_vertex = 0
    shortest_paths = dijkstra(g, start_vertex)
    
    print(f"Shortest paths from vertex {start_vertex}:\n")
    
    for vertex in range(len(shortest_paths)):
        distance = shortest_paths[vertex]
        if distance < float('inf'):
            print(f"Vertex {vertex}: Distance {distance}")
        else:
            print(f"Vertex {vertex}: Not reachable from vertex {start_vertex}")

if __name__ == "__main__":
    main()
