from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

class Task:
    def __init__(self, name, priority, creation_time):
        self.name = name
        self.priority = priority
        self.creation_time = creation_time

class TodoList:
    def __init__(self):
        self.tasks = []

    def new_task(self, task_name, priority):
        creation_time = len(self.tasks)
        task = Task(task_name, priority, creation_time)
        self.tasks.append(task)

    def get_tasks(self):
        return [(task.name, task.priority) for task in self.tasks]

    def count_priorities(self):
        counts = {3: 0, 2: 0, 1: 0}  # Priority levels: High, Medium, Low
        for task in self.tasks:
            counts[task.priority] += 1
        return counts

todo_list = TodoList()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_name = request.form['task_name']
        priority = int(request.form['priority'])
        todo_list.new_task(task_name, priority)
        return redirect(url_for('index'))
    tasks = todo_list.get_tasks()
    priority_counts = todo_list.count_priorities()
    return render_template('index.html', tasks=tasks, priority_counts=priority_counts)

if __name__ == '__main__':
    app.run(debug=True)
