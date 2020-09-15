#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''

    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    response = requests.get(base_url + 'users/' + eid)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()
    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]

    user_todos = [{'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': user.get('username')}
                  for todo in user_todos]
    data = {eid: user_todos}
    with open(eid + '.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    do_request()
