#!/usr/bin/python3
"""
This module fetches task data for all employees
from a REST API and exports it to a JSON file.
"""
from json import dump
from requests import get


if __name__ == '__main__':
    # URL for fetching user data
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    # Fetch user data from the API
    users_response = get(base_url)
    # Extract user information
    users = users_response.json()

    # Dictionary to store user tasks
    all_tasks = {}

    # Iterate over each user
    for user in users:
        # Get user ID and username
        user_id = user.get('id')
        username = user.get('username')

        # URL for fetching user's tasks
        user_tasks_url = (
            'https://jsonplaceholder.typicode.com/users/{}/todos/'
            .format(user_id)
        )
        # Fetch user's tasks from the API
        user_tasks_response = get(user_tasks_url)

        # Extract user's tasks
        tasks = user_tasks_response.json()

        # Initialize task list for the user
        all_tasks[user_id] = []

        # Iterate over each task of the user
        for task in tasks:
            # Add task details to the user's task list
            all_tasks[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    # Write the dictionary containing all user tasks to a JSON file
    with open('todo_all_employees.json', 'w') as file:
        dump(all_tasks, file)