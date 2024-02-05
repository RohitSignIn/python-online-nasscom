from simple_http_server import server
from simple_http_server import request_map
from simple_http_server import PathValue
from simple_http_server import Headers

import main
# USER APIs --START-- 
# Get USERS Route 
@request_map("/api/v1/users", method="GET")
def index():
    res = main.getUsers()
    return 200, Headers({"access-control-allow-origin": "*"}), {"res": res}

# Get USER By Id 
@request_map("/api/v1/user/{id}", method="GET")
def index(id = PathValue()):
    res = main.getUserById(id)
    return 200, Headers({"access-control-allow-origin": "*"}), {"res": res}


# Create User
@request_map("/api/v1/user", method="POST")
def index(username, password):
    main.addUser(username, password)
    return 201, Headers({"access-control-allow-origin": "*"}), {
        "success": "true",
        "message": "User created successfully",
        "user": username
        }


# Update USER Route 
@request_map("/api/v1/user", method="PUT")
def index(update, to, userId):
    main.userUpdate(update, to, userId)
    return 201,  Headers({"access-control-allow-origin": "*"}), {
        "success": "true",
    }

# DELETE USER Route 
@request_map("/api/v1/user", method="DELETE")
def index(userId):
    main.userDelete(userId)    
    return 201,  Headers({"access-control-allow-origin": "*"}), {
        "success": "true",
    }
# USER APIs --START-- 






# TODO APIs --START-- 

# Get Todos
@request_map("/api/v1/todos", method="GET")
def index():
    res = main.getTodos()
    return 200, Headers({"access-control-allow-origin": "*"}), {"res": res}

# Get Todo By id
@request_map("/api/v1/todo/{id}", method="GET")
def index(id = PathValue()):
    res = main.getTodoById(id)
    return 200, Headers({"access-control-allow-origin": "*"}), {"res": res}

# Create Todo
@request_map("/api/v1/todo", method="POST")
def index(task, userId):
    main.createTodo(task, userId)
    return 201, Headers({"access-control-allow-origin": "*"}), {"success": "true"}

# Update Todo
@request_map("/api/v1/todo", method="PUT")
def index(update, to, todoId):
    main.updateTodo(update, to, todoId)
    return 201, Headers({"access-control-allow-origin": "*"}), {"success": "true"}

# DELETE Todo
@request_map("/api/v1/todo", method="DELETE")
def index(todoId):
    main.deleteTodo(todoId)
    return 201, Headers({"access-control-allow-origin": "*"}), {"success": "true"}

# TODO APIs --ENDS-- 

server.start(port=9090)