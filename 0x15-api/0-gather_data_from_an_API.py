#!/usr/bin/python3
"""
Requests an API with a given employee ID
Returns information about the employee's TODO list
"""
if __name__ == "__main__":
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    employee_url = url + 'users/{}'.format(employee_id)
    todo_url = url + 'todos?userId={}'.format(employee_id)
    employee = requests.get(employee_url).json()
    todo = requests.get(todo_url).json()
    employee_name = employee.get('name')
    task_finished_count = 0
    total = len(todo)
    tasks_finished = ""
    for task in todo:
        if task.get('completed'):
            task_finished_count += 1
            task_title = task.get('title')
            tasks_finished += '\t {}\n'.format(task_title)
            employee_print = 'Employee {} is done with tasks({}/{}):'.format(
                employee_name, task_finished_count, total)
    print(employee_print)
    print(tasks_finished, end="")
