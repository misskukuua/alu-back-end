#!/usr/bin/python3

"""Export to CSV"""
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos" \
        .format(employee_id)
    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    total_             for todo in todos_response]
