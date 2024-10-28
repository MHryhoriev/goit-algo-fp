from node import Node
from typing import Optional

class LinkedList:
    def __init__(self) -> None:
        """
        Initialize the linked list with no head node.
        """
        self.head = None

    def insert_at_beginning(self, data: int) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Parameters:
            data (int): Data to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int) -> None:
        """
        Insert a new node at the end of the list.
        
        Parameters:
            data (int): Data to store in the new node.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node

    def insert_after(self, prev_node: Node, data: int) -> None:
        """
        Insert a new node after a given node.
        
        Parameters:
            prev_node (Node): The node after which the new node should be inserted.
            data (int): Data to store in the new node.
        """
        if prev_node is None:
            print("The previous node does not exist.")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int) -> None:
        """
        Delete the first occurrence of a node by value.
        
        Parameters:
            key (int): The data value of the node to delete.
        """
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        
        prev.next = current.next
        current = None

    def search_element(self, data: int) -> Optional[Node]:
        """
        Search for a node with the specified data value.
        
        Parameters:
            data (int): The data value to search for.
            
        Returns:
            Node | None: The node containing the data, or None if not found.
        """
        current = self.head

        while current:
            if current.data == data:
                return current
            current = current.next

        return None
    
    def reverse_list(self) -> None:
        """
        Reverse the linked list in place.
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def merge_sort(self) -> None:
        """
        Sort the linked list in ascending order using merge sort.
        """
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head: Optional[Node]) -> Optional[Node]:
        """
        Recursive merge sort implementation for linked list nodes.
        
        Parameters:
            head (Node): The starting node of the list to sort.
            
        Returns:
            Node: The sorted linked list.
        """
        if head is None or head.next is None:
            return head
        
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head: Node) -> Node:
        """
        Find the middle node of the linked list using the slow and fast pointer approach.
        
        Parameters:
            head (Node): The starting node of the list.
            
        Returns:
            Node: The middle node of the list.
        """
        if head is None:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _sorted_merge(self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        """
        Merge two sorted linked lists.
        
        Parameters:
            a (Node): The head of the first sorted list.
            b (Node): The head of the second sorted list.
            
        Returns:
            Node: The merged sorted list.
        """
        if a is None:
            return b
        
        if b is None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)

        return result

    def print_list(self) -> None:
        """
        Print all elements in the linked list.
        """
        current = self.head

        while current:
            print(current.data)
            current = current.next