#!/usr/bin/python3
import csv
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
    
    # Write to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])
