#!/usr/bin/python3
"""
Requests an API with a given employee ID
Returns information about the employee's TODO list in JSON format
"""
if __name__ == "__main__":
    from collections import OrderedDict
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    employee_url = url + 'users/{}'.format(employee_id)
    todo_url = url + 'todos?userId={}'.format(employee_id)
    employee = requests.get(employee_url).json()
    todo = requests.get(todo_url).json()
    employee_name = employee.get('name')
    json_file = '{}.json'.format(employee_id)
    with open(json_file, 'w') as f:
        todo_list = []
        for task in todo:
            task_title = task.get('title')
            task_completed = task.get('completed')
            todo_dict = [("task", task_title), ("completed", task_completed),
                         ("username", employee_name)]
            todo_dict = OrderedDict(todo_dict)
            todo_list.append(todo_dict)
        json.dump({str(employee_id): todo_list}, f)
