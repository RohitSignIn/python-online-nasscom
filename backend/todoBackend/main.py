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

def addUser(username, password):
    cursor.execute(f"""
        INSERT INTO user (username, password)
        VALUES ('{username}', '{password}')
    """)
    conObj.commit()

    return True