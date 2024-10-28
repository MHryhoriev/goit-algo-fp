from node import Node

def array_to_heap_tree(arr, index=0):
    """
    Recursively builds a tree from an array representing a binary heap.

    Parameters:
        arr (list): Array representing a binary heap.
        index (int): Current index in the array.

    Returns:
        Node: The root of the subtree built from part of the array.
    """
    if index >= len(arr):
        return None

    node = Node(arr[index])
    node.left = array_to_heap_tree(arr, 2 * index + 1)
    node.right = array_to_heap_tree(arr, 2 * index + 2)

    return node
