#!/usr/bin/python3
"""Write a Python script that for a given ID returns information
about their TODO list progress"""

import requests
import sys

import urllib.request
import json
import sys

# Check if employee ID is provided as argument
if len(sys.argv) != 2:
    print("Please provide employee ID as argument")
    sys.exit()

# Get employee ID from command line argument
employee_id = sys.argv[1]

# Define the API endpoint URL
url = "https://jsonplaceholder.typicode.com/todos?userId=" + employee_id

# Make a request to the API endpoint and get the response
response = urllib.request.urlopen(url).read().decode()

# Convert the response to JSON format
json_data = json.loads(response)

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
print("Employee " + employee_name +
      " is done with " + str(num_completed_tasks) +
      "/" + str(total_num_tasks) + " tasks:")
for title in completed_task_titles:
    print("\t" + title)
