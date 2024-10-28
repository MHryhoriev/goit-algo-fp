import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import random
from time import sleep
from matplotlib.animation import FuncAnimation
from typing import List, Tuple, Optional, Dict, Callable
from node import Node
from color_generator import generate_color_gradient

def build_graph_edges(node: Optional[Node], edges: Optional[List[Tuple[int, int]]] = None) -> List[Tuple[int, int]]:
    """
    Builds a list of edges for a graph from a binary tree.

    Parameters:
        node (Node): The root node of the binary tree.
        edges (Optional[List[Tuple[int, int]]]): A list of edges to be filled. Defaults to None.

    Returns:
        List[Tuple[int, int]]: A list of edges where each edge is represented as a tuple (parent_node, child_node).
    """
    if edges is None:
        edges = []

    if node:
        if node.left:
            edges.append((node.value, node.left.value))
            build_graph_edges(node.left, edges)
        if node.right:
            edges.append((node.value, node.right.value))
            build_graph_edges(node.right, edges)

    return edges


def hierarchy_pos(G: nx.Graph, root: Optional[int] = None, width: float = 1.0, 
                  vert_gap: float = 0.2, vert_loc: float = 0, xcenter: float = 0.5) -> Dict[int, Tuple[float, float]]:
    """
    Calculates the position of nodes in a tree for hierarchical layout.

    Parameters:
        G (nx.Graph): The input graph, which must be a tree.
        root (Optional[int]): The root node of the tree. If None, the root will be determined automatically.
        width (float): The total width of the plot area.
        vert_gap (float): The vertical gap between levels in the hierarchy.
        vert_loc (float): The vertical location for the root node.
        xcenter (float): The horizontal center of the root node.

    Returns:
        Dict[int, Tuple[float, float]]: A dictionary where keys are node values and values are tuples representing the (x, y) positions of the nodes.
    
    Raises:
        TypeError: If the input graph is not a tree.
    """
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def animate_traversal(tree_root: Node, traversal_func: Callable[[Node], List[Node]], 
                      traversal_type: str) -> None:
    """
    Animate the traversal of a binary tree using the specified traversal function.

    Parameters:
        tree_root (Node): The root node of the binary tree.
        traversal_func (Callable[[Node], List[Node]]): The function to use for traversal,
            which should return a list of nodes in the order they are visited.
        traversal_type (str): A string describing the type of traversal (e.g., "DFS" or "BFS").

    Returns:
        None
    """
    path = traversal_func(tree_root)
    print(traversal_type, [x.value for x in path])

    # Build the graph
    G = nx.DiGraph()
    G.add_edges_from(build_graph_edges(tree_root))
    pos = hierarchy_pos(G, root=tree_root.value)

    fig, ax = plt.subplots()

    # Generate a color gradient from dark to light blue
    start_color = (18, 150, 240)
    end_color = (173, 216, 230)
    colors = generate_color_gradient(start_color, end_color, len(path))

    def update(frame):
        """
        Update the animation for the current frame.

        Parameters:
            frame (int): The current frame number.

        Returns:
            None
        """
        sleep(0.5)
        ax.clear()
        nodes = [node.value for node in path[:frame + 1]]

        # Draw the graph with labels and colors
        nx.draw(G, pos=pos, with_labels=True, node_size=2000, node_color='grey', ax=ax, font_weight='bold')
        nx.draw_networkx_nodes(G, pos=pos, nodelist=nodes, node_color=colors[:frame + 1], node_size=2000, ax=ax)
        ax.set_title(f'{traversal_type} Traversal - Step {frame + 1}/{len(path)}')

    ani = FuncAnimation(fig, update, frames=len(path), repeat=True)
    plt.show()