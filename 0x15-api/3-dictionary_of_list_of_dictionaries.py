#!/usr/bin/python3
"""
Requests an API with to get data about all employees
Returns information about the employees TODO list in JSON format
"""
if __name__ == "__main__":
    from collections import OrderedDict
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/'
    employees_url = url + 'users'
    employees = requests.get(employees_url).json()
    json_file = 'todo_all_employees.json'
    with open(json_file, 'w') as f:
        employees_dict = OrderedDict()
        for employee in employees:
            employee_id = employee.get('id')
            employee_name = employee.get('name')
            todo_url = url + 'todos?userId={}'.format(employee_id)
            todo = requests.get(todo_url).json()
            todo_list = []
            for task in todo:
                task_title = task.get('title')
                task_completed = task.get('completed')
                todo_dict = [("username", employee_name), ("task", task_title),
                             ("completed", task_completed)]
                todo_dict = OrderedDict(todo_dict)
                todo_list.append(todo_dict)
            employees_dict[str(employee_id)] = todo_list
        json.dump(employees_dict, f)
