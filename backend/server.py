from simple_http_server import route, server
    
@route("/")
def index():
    return {"Home": "I am home"}   

@route("/about")
def index():
    return {"About": "I am about"}    

@route("/contact")
def index():
    return {"Contact": "I am contact"}    

server.start(port=7772)