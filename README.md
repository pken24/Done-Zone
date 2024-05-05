**Done-Zone Todo List**

This Done-Zone Todo List application allows users to add tasks with different priorities and view them in a web interface. Tasks are displayed in a list format along with their priorities, and a bar chart shows the distribution of tasks across different priority levels.

**Prerequisites**

* Python 3 installed on your system
* Flask library installed (pip install Flask)

**Installation**

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.

**Usage**

1. Run the Flask application by executing the following command:
```python
python app.py
```

2. Open your web browser and go to http://127.0.0.1:5000/.
3. You can add tasks by entering the task name and selecting the priority level (Low, Medium, or High). Click the "Add Task" button to submit.
4. The tasks will be displayed on the page along with their priority levels.
5. The bar chart shows the number of tasks per priority level.

**Files and Directory Structure**

* app.py: Contains the Flask application code.
* index.html: HTML template file for rendering the web interface.
* static/: Directory containing static files like CSS or JavaScript (currently empty).
* templates/: Directory containing HTML templates.

**Flask Routes**

* GET /: Renders the home page with the list of tasks and priority counts.
* POST /: Handles form submission to add new tasks.

**Class Structure**

* Task: Represents a single task with attributes like name, priority, and creation time.
* TodoList: Manages the list of tasks using a priority queue data structure.

**Dependencies**

* Flask: Web framework for Python.
* Plotly.js: JavaScript library for creating interactive charts.

**Customization**
* You can customize the HTML template (index.html) to change the appearance of the web interface.
* Modify the Flask routes (app.py) to add more functionality or change the behavior of existing routes.

**Contributing:**

We welcome contributions from the community to enhance our tool further. Here's how you can contribute:

1. Fork the Repository: Fork the repository to your GitHub account.

2. Pick an Issue: Choose an existing issue from our GitHub repository or create a new one.

3. Work on the Issue: Implement the necessary changes or features in your forked repository.

4. Submit a Pull Request: Once you're done, submit a pull request detailing the changes you've made and how they address the issue.

5.  Code Review: Our team will review your pull request, provide feedback, and merge it into the main codebase if everything looks good.

Thank you for your interest in our Done-Zone ToDo Lists applications. We look forward to your contributions and hope our tool proves to be valuable in your financial analysis endeavors.
