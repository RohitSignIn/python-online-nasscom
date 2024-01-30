from simple_http_server import server
from simple_http_server import request_map
from simple_http_server import PathValue

import main
# USER APIs --START-- 
# Create USER Route 
@request_map("/api/v1/user", method="POST")
def index(username, password):
    return {"res": f"user={username}&password={password}"}


# Update USER Route 
@request_map("/api/v1/user", method="PUT")
def index(update, to, userId):
    return {"res": f"Update Column={update} to={to}, userId={userId}"}

# DELETE USER Route 
@request_map("/api/v1/user", method="DELETE")
def index(userId):
    return {"res": f"Delete user UserId={userId}"}

# Fetch All users
@request_map("/api/v1/users", method="GET")
def index():
    return {"res": f"Fetch All user called"}

# Fetch user by userId
@request_map("/api/v1/user/{userId}", method="GET")
def index(userId = PathValue()):
    return {"res": f"Fetch user by userId={userId}"}
# USER APIs --END-- 





server.start(port=9090)