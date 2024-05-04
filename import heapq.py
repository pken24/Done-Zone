import heapq

class PriorityQueue:
    def __init__(self, compare_fn):
        self.elements = []
        self.compare_fn = compare_fn

    def enqueue(self, element, priority):
        heapq.heappush(self.elements, (priority, element))

    def dequeue(self):
        return heapq.heappop(self.elements)[1]

    def is_empty(self):
        return len(self.elements) == 0

    def peek(self):
        if not self.is_empty():
            return self.elements[0][1]
        return None


# Define priority levels
HIGH_PRIORITY = 3
MEDIUM_PRIORITY = 2
LOW_PRIORITY = 1

# Custom comparison function for tasks with the same priority
def compare_tasks(task1, task2):
    if task1.priority == task2.priority:
        # Serve tasks with the same priority based on their creation time
        return task1.creation_time - task2.creation_time
    else:
        # Serve tasks with higher priority first
        return task2.priority - task1.priority

class Task:
    def __init__(self, name, priority, creation_time):
        self.name = name
        self.priority = priority
        self.creation_time = creation_time
    def __lt__(self, other):
        # Define comparison based on priority and creation time
        if self.priority == other.priority:
            return self.creation_time < other.creation_time
        else:
            return self.priority < other.priority

class TodoList:
    def __init__(self):
        self.pq = PriorityQueue(compare_tasks)

    def new_task(self):
        task_name = input("Enter the task name: ")
        priority = int(input("Enter the priority level (1: Low, 2: Medium, 3: High): "))
        creation_time = len(self.pq.elements)
        task = Task(task_name, priority, creation_time)
        self.pq.enqueue(task, priority)

    def next_task(self):
        return self.pq.dequeue()

    def peek_next_task(self):
        return self.pq.peek()

    def is_empty(self):
        return self.pq.is_empty()

    def print_tasks(self):
        tasks = []
        pq_copy = self.pq.elements.copy()
        while not self.pq.is_empty():
            task = self.pq.dequeue()
            tasks.append((task.name, task.priority))
        self.pq.elements = pq_copy
        print("Tasks:")
        for i, (task, priority) in enumerate(tasks, 1):
            priority_level = "High" if priority == HIGH_PRIORITY else "Medium" if priority == MEDIUM_PRIORITY else "Low"
            print(f"{i}. {task} (Priority: {priority_level})")

# Example usage:
todo_list = TodoList()

todo_list.new_task()
todo_list.new_task()
todo_list.new_task()

todo_list.print_tasks()