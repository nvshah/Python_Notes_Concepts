import requests
import json

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers




def get():
    # GET ----
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print(response.json())
    print(response.status_code)
    print(response.headers["Content-Type"])

def post_1():
    # POST ----
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=todo)
    # requests.post() automatically sets the request’s HTTP header Content-Type to application/json
    print(response.json())

def post_2():
    # POST ----
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    # (Alternative ) to post data when json data is available instead of dict
    #    In this case we need to manually mention the headers & data (serialized json string)
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    print(response.json())
    print(response.status_code)  # 201 -> new resrc was created

def put():
    # To modifiy any existinng todo
    # PUT ----
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.get(api_url)
    data = response.json()
    print(data)  # Get Data for todo 10

    userId = data['userId']

    todo = {"userId": userId, "title": "Wash car", "completed": True}
    response = requests.put(api_url, json=todo)
    print(response.json())
    print(response.status_code) # 200

def patch():
    # to modify specific field on existing todo
    '''
    PATCH differs from PUT in that it doesn’t completely replace the existing resource. 
    It only modifies the values set in the JSON sent with the request.
    '''

    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    todo = {"title": "Mow lawn"}
    response = requests.patch(api_url, json=todo)
    print(response.json())
    print(response.status_code)

def delete():
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.delete(api_url)
    print(response.json())
    print(response.status_code)




