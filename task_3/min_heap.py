import heapq

class MinHeap:
    def __init__(self):
        """
        Initialize an empty min heap.
        """
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = 0

    def add_task(self, task, priority=0):
        """
        Add a new task or update the priority of an existing task.

        Parameters:
            task: The task to add or update.
            priority (int): The priority of the task.
        """
        if task in self.entry_finder:
            self.remove_task(task)
        entry = [priority, self.counter, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.heap, entry)
        self.counter += 1

    def remove_task(self, task):
        """
        Remove a task from the heap.

        Parameters:
            task: The task to remove.
        """
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """
        Pop the task with the lowest priority.

        Returns:
            The task with the lowest priority.

        Raises:
            KeyError: If the heap is empty.
        """
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')

    def is_empty(self):
        """
        Check if the heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.
        """
        return not self.entry_finder
