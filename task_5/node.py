import uuid

class Node:
    """
    Class representing a binary tree node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
