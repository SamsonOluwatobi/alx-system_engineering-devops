#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get all employees
    users_url = f"{base_url}/users"
    users = requests.get(users_url).json()
    
    # Create dictionary for all tasks
    all_tasks = {}
    
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        
        # Get tasks data for each user
        tasks_url = f"{base_url}/todos?userId={user_id}"
        tasks = requests.get(tasks_url).json()
        
        # Prepare tasks for JSON export
        all_tasks[user_id] = [{
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in tasks]
    
    # Write all data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file)
