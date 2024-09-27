#!/usr/bin/python3
"""
This module fetches employee task data from a
REST API and exports it to a JSON file.
"""
from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    # Get user ID from command-line arguments
    employee_id = argv[1]

    # Fetch user data from the API
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    user_response = get(base_url)
    username = user_response.json().get('username')

    # Fetch user's tasks from the API
    tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                 employee_id)
    tasks_response = get(tasks_url)
    tasks = tasks_response.json()

    # Create a dictionary to store user's tasks
    user_tasks = {employee_id: []}

    # Iterate over each task and store it in the dictionary
    for task in tasks:
        user_tasks[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    # Write the dictionary to a JSON file
    with open('{}.json'.format(employee_id), 'w') as file:
        dump(user_tasks, file)