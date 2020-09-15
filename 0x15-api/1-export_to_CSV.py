#!/usr/bin/python3
"""
Requests an API with a given employee ID
Returns information about the employee's TODO list in CSV format
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    employee_url = url + 'users/{}'.format(employee_id)
    todo_url = url + 'todos?userId={}'.format(employee_id)
    employee = requests.get(employee_url).json()
    todo = requests.get(todo_url).json()
    employee_name = employee.get('name')
    csv_file = '{}.csv'.format(employee_id)
    with open(csv_file, 'w') as f:
        for task in todo:
            csv_to_write = csv.writer(f, quoting=csv.QUOTE_ALL)
            employee_id_str = str(employee_id)
            task_finished_str = str(task.get('completed'))
            task_name = task.get('title')
            csv_to_write.writerow([employee_id_str, employee_name,
                                  task_finished_str, task_name])
