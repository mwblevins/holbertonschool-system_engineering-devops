#!/usr/bin/python3
"""Write a Python script that for a given ID returns information
about their TODO list progress"""

import requests
import sys

# Check if employee ID is provided as argument
if len(sys.argv) != 2:
    print("Please provide employee ID as argument")
    sys.exit()

# Get employee ID from command line argument
employee_id = sys.argv[1]

# Define the API endpoint URL
url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

# Make a request to the API endpoint and get the response
response = requests.get(url)

# Convert the response to JSON format
json_data = response.json()

# Get the employee name
employee_name = json_data[0]["name"]

# Count the number of completed and total tasks
num_completed_tasks = 0
total_num_tasks = len(json_data)
completed_task_titles = []
for task in json_data:
    if task["completed"]:
        num_completed_tasks += 1
        completed_task_titles.append(task["title"])

# Print the employee TODO list progress
print(f"Employee {employee_name} is done with {num_completed_tasks}/{total_num_tasks} tasks:")
for title in completed_task_titles:
    print(f"\t {title}")
