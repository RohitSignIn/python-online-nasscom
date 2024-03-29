import mysql.connector 

config = {
    "port": 7777,
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "tododb"
}

conObj = mysql.connector.connect(**config)

myCursor = conObj.cursor()

myCursor.execute("""
create table if not exists user ( 
	id int auto_increment primary key,
    username text,
    password text
)
""")

myCursor.execute("""
create table if not exists todo (
	id int auto_increment primary key,
    task text,
    status text,
	userId int,
    foreign key(userId) references user(id)
)
""")

# query = """
# INSERT INTO todo 
# (task, status, userId) 
# VALUES(%s, %s, %s)
# """

# values = ("go to Gym", "pending", 2)
# myCursor.execute(query, values)

# conObj.commit()


myCursor.execute("select * from todo")

res = myCursor.fetchall()
print(res)