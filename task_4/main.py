from tree_builder import array_to_heap_tree
from tree_visualizer import draw_tree

def main():
    """
    Creates and visualizes a tree from an array representing a binary heap.
    """
    # Array representing a binary heap (e.g., a min-heap)
    heap_array = [3, 9, 5, 10, 12, 15, 17]

    # Build the tree from the heap array
    heap_tree_root = array_to_heap_tree(heap_array)

    # Visualize the tree
    draw_tree(heap_tree_root)

if __name__ == "__main__":
    main()
