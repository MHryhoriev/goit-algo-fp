from node import Node
from linked_list import LinkedList

def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """
    Merge two sorted linked lists into one sorted linked list.

    Parameters:
        list1 : LinkedList
            The first sorted linked list.
        list2 : LinkedList
            The second sorted linked list.

    Returns:
        LinkedList
            A new LinkedList instance containing all elements from both input lists,
            sorted in ascending order.

    """
    merged_list = LinkedList()
    dummy = Node(0)
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    merged_list.head = dummy.next
    return merged_list