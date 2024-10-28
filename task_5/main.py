from tree_builder import array_to_heap_tree
from tree_traversal import dfs_iterative_tree, bfs_iterative_tree
from tree_visualizer import animate_traversal

import warnings
warnings.filterwarnings('ignore')

def main():
    heap_array = [3, 9, 5, 10, 12, 15, 17]
    heap_tree_root = array_to_heap_tree(heap_array)

    # Animate DFS traversal
    #animate_traversal(heap_tree_root, dfs_iterative_tree, "DFS")

    # Animate BFS traversal
    animate_traversal(heap_tree_root, bfs_iterative_tree, "BFS")

if __name__ == "__main__":
    main()