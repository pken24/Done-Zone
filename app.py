from flask import Flask, render_template, request, redirect, url_for
import heapq
import matplotlib.pyplot as plt

app = Flask(__name__)

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

HIGH_PRIORITY = 3
MEDIUM_PRIORITY = 2
LOW_PRIORITY = 1

def compare_tasks(task1, task2):
    if task1.priority == task2.priority:
        return task1.creation_time - task2.creation_time
    else:
        return task2.priority - task1.priority

class Task:
    def __init__(self, name, priority, creation_time):
        self.name = name
        self.priority = priority
        self.creation_time = creation_time

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.creation_time < other.creation_time
        else:
            return self.priority < other.priority

class TodoList:
    def __init__(self):
        self.pq = PriorityQueue(compare_tasks)

    def new_task(self, task_name, priority):
        creation_time = len(self.pq.elements)
        task = Task(task_name, priority, creation_time)
        self.pq.enqueue(task, priority)

    def next_task(self):
        return self.pq.dequeue()
    
    def count_priorities(self):
        priority_counts = {}
        for task in self.pq.elements:
            if task.priority in priority_counts:
                priority_counts[task.priority] += 1
            else:
                priority_counts[task.priority] = 1
        return priority_counts

    def plot_priority_counts(self):
        priority_counts = self.count_priorities()
        priorities = list(priority_counts.keys())
        counts = list(priority_counts.values())

        plt.bar(priorities, counts)
        plt.xlabel('Priority')
        plt.ylabel('Number of Tasks')
        plt.title('Number of Tasks per Priority Level')
        plt.show()
        
    def peek_next_task(self):
        return self.pq.peek()

    def is_empty(self):
        return self.pq.is_empty()

    def get_tasks(self):
        tasks = []
        pq_copy = self.pq.elements.copy()
        while not self.pq.is_empty():
            task = self.pq.dequeue()
            tasks.append((task.name, task.priority))
        self.pq.elements = pq_copy
        return tasks

todo_list = TodoList()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_name = request.form['task_name']
        priority = int(request.form['priority'])
        todo_list.new_task(task_name, priority)
        return redirect(url_for('index'))
    tasks = todo_list.get_tasks()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
