import mysql.connector

config = {
    "port": 7777,
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "tododb"
}

conObj = mysql.connector.connect(**config)

cursor = conObj.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id int auto_increment primary key,
        username text NOT NULL,
        password text NOT NULL
    )
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS todo (
                id int auto_increment primary key,
                task text NOT NULL,
                status text NOT NULL,
                userId int NOT NULL,
                foreign key(userId) references user(id)
               )
               """)


# USER QUERIES STARTED
def getUsers():
    cursor.execute("""
    SELECT * FROM user
    """)

    res = cursor.fetchall()

    print(res)
    return res 

def getUserById(id):
    cursor.execute(f"""
    SELECT * FROM user
    where id = {id}
    """)

    res = cursor.fetchone()
    return res

def addUser(username, password):
    cursor.execute(f"""
        INSERT INTO user (username, password)
        VALUES ('{username}', '{password}')
    """)
    conObj.commit()

def userUpdate(update, to, userId):
    cursor.execute(f"""
        UPDATE user SET {update} = '{to}'
        WHERE id = '{userId}'
    """)
    conObj.commit()

def userDelete(userId):
    cursor.execute(f"""
    DELETE FROM user
    WHERE id = {userId}
    """)
    conObj.commit()
# USER QUERIES STARTED



# TODOS QUERIES STARTED
    
# Get All Todos
def getTodos():
    cursor.execute(f"""
    SELECT * FROM todo
    """)
    
    res = cursor.fetchall()
    print(res)
    return res


def getTodoById(id):
    cursor.execute(f"""
    SELECT * FROM todo
    WHERE id = {id}
    """)

    res = cursor.fetchone()
    return res

def createTodo(task, userId):
    cursor.execute(f"""
    INSERT INTO todo
    (task, status, userId)
    VALUES('{task}', 'pending', '{userId}')
    """)
    conObj.commit()


def updateTodo(update, to, todoId):
    cursor.execute(f"""
    UPDATE todo SET {update} = '{to}'
    WHERE id = {todoId}
    """)
    conObj.commit()


def deleteTodo(todoId):
    cursor.execute(f"""
    DELETE FROM todo 
    WHERE id = {todoId}
    """)
    conObj.commit()
