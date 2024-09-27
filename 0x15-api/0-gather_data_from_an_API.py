#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Get employee ID from command-line argument
    employee_id = int(sys.argv[1])
    
    # Base URL for API requests
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee data (name)
    employee_url = f"{base_url}/users/{employee_id}"
    employee = requests.get(employee_url).json()
    employee_name = employee.get("name")
    
    # Get tasks data
    tasks_url = f"{base_url}/todos?userId={employee_id}"
    tasks = requests.get(tasks_url).json()
    
    # Filter tasks
    completed_tasks = [task for task in tasks if task.get("completed")]
    total_tasks = len(tasks)
    
    # Output result
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
