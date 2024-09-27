#!/usr/bin/python3
"""Script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress and exports it to CSV.
"""
import requests
from sys import argv


if __name__ == "__main__":
    # Get the user ID from the command-line arguments
    employee_id = argv[1]

    # Fetch user data from the API
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(base_url)

    # Extract the username from the response
    user_name = response.json().get('username')

    # Fetch user's tasks from the API
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    url_content = requests.get(base_url)
    tasks = url_content.json()

    # Write user's tasks to a CSV file
    with open('{}.csv'.format(employee_id), 'w') as file:
        # Iterate over each task and write it to the CSV file
        for task in tasks:

            # Convert completion status to string (True/False)
            completed = str(task.get('completed'))

            # Write task details in CSV format
            file.write('"{}","{}","{}","{}"\n'.format(
                       employee_id, user_name, completed, task.get('title')))