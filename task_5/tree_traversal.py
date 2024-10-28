from collections import deque
from typing import List, Optional, Set
from node import Node

def dfs_iterative_tree(root: Optional[Node]) -> List[Node]:
    """
    Perform an iterative depth-first search (DFS) traversal on a binary tree.

    Parameters:
        root (Node): The root node of the binary tree.

    Returns:
        List[Node]: A list of nodes visited during the DFS traversal in the order they were visited.
    """
    if root is None:
        return []
    
    visited = set()
    stack = [root]
    path = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            path.append(node)

            # Push right child first so that left child is processed next
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return path


def bfs_iterative_tree(root: Optional[Node]) -> List[Node]:
    """
    Perform an iterative breadth-first search (BFS) traversal on a binary tree.

    Parameters:
        root (Node): The root node of the binary tree.

    Returns:
        List[Node]: A list of nodes visited during the BFS traversal in the order they were visited.
    """
    if root is None:
        return []

    visited = set()
    queue = deque([root])
    path = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            path.append(node)

            # Add left and right children to the queue if not already visited
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)

    return path