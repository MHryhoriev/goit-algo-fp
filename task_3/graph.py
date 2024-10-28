from typing import List, Tuple, Dict

class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.graph: Dict[int, List[Tuple[int, float]]] = {}

    def add_edge(self, u: int, v: int, weight: float):
        """
        Add an edge to the graph.

        Parameters:
            u (int): The starting vertex.
            v (int): The ending vertex.
            weight (float): The weight of the edge.
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def get_neighbors(self, u: int) -> List[Tuple[int, float]]:
        """
        Get the neighbors of a vertex.

        Parameters:
            u (int): The vertex to get neighbors for.

        Returns:
            List[Tuple[int, float]]: A list of tuples containing neighboring vertices and their weights.
        """
        return self.graph.get(u, [])
