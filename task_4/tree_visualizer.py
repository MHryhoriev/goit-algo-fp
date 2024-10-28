import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Recursively adds nodes and edges to a graph to construct a tree for visualization.

    Parameters:
        graph (nx.DiGraph): The graph representing the tree.
        node (Node): The current node in the tree.
        pos (dict): Dictionary containing node coordinates.
        x (float): X-coordinate of the current node.
        y (float): Y-coordinate of the current node.
        layer (int): The current layer level in the tree.

    Returns:
        nx.DiGraph: The graph representing the tree.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """
    Displays the tree as a graph.

    Parameters:
        tree_root (Node): The root node of the tree.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
