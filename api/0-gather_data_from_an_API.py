import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    total_tasks = 0
    completed_tasks = 0

    for item in todos_response:
        if item.get('userId') == int(employee_id):
            total_tasks += 1
        if item.get('completed'):
            completed_tasks += 1
    print("Employee {} is done with tasks ({}/{}):".format(user_response.get('name'),
                                                           completed_tasks, total_tasks))
    for todo in todos_response:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))

    # res = requests.get(todos_url)
    # try:
    #     todos_response = res.json()
    # except requests.exceptions.JSONDecodeError:
    #     print("exfjkhlk")
    #
    # print(todos_response)
