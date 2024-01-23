from simple_http_server import server
from simple_http_server import request_map
from simple_http_server import PathValue
    
@request_map("/api/v1/user/{id}", method="GET")
def index(id=PathValue()):
    return {"user": f"Get req id is {id}"}   

@request_map("/api/v1/user", method="PUT")
def index(username, password):
    return {"user": f"Post Res user: {username}, password: {password}"}   


server.start(port=9090)