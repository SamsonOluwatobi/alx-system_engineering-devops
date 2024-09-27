#!/usr/bin/python3
"""Script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user information based on provided employee ID
    user = requests.get(base_url + "users/{}".format(sys.argv[1])).json()

    # Get TODO list for the specified user
    todos = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks and extract their titles
    completed = [t["title"] for t in todos if t["completed"]]

    # Print the progress report
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print titles of completed tasks
    [print("\t{}".format(c)) for c in completed]