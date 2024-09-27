#!/usr/bin/python3
"""
This module fetches employee task data from a REST API and exports it to a JSON file.

Usage:
    ./2-export_to_JSON.py <employee_id>

Arguments:
    employee_id: The ID of the employee whose task data is being exported.

Output:
    Exports the employee's tasks to a JSON file named USER_ID.json with the format:
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}] }.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee data
    employee_url = f"{base_url}/users/{employee_id}"
    employee = requests.get(employee_url).json()
    username = employee.get("username")
    
    # Get tasks data
    tasks_url = f"{base_url}/todos?userId={employee_id}"
    tasks = requests.get(tasks_url).json()
    
    # Prepare data for JSON export
    json_data = {employee_id: [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    } for task in tasks]}
    
    # Write to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as file:
        json.dump(json_data, file)
