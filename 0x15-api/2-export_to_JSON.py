#!/usr/bin/python3
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
