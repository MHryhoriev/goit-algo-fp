from linked_list import LinkedList
from merge_sorted_list import merge_sorted_lists

def main():
    linked_list = LinkedList()

    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(15)

    linked_list.insert_at_end(20)
    linked_list.insert_at_end(25)

    print("Linking list:")
    linked_list.print_list()

    linked_list.reverse_list()

    print("\nLinking list after reversal:")
    linked_list.print_list()

    linked_list.merge_sort()

    print("\nLinked list after sorting:")
    linked_list.print_list()

    second_linked_list = LinkedList()
    second_linked_list.insert_at_end(2)
    second_linked_list.insert_at_end(4)
    second_linked_list.insert_at_end(6)

    merged_list = merge_sorted_lists(linked_list, second_linked_list)

    print("\nMerge sorted lists:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
