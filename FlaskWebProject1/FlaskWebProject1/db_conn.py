import pymssql
server = "138.68.87.1"
user = "SA"
password = "Diakov989"
conn = pymssql.connect(server, user, password, "database")
users_conn = pymssql.connect(server, user, password, "users")

def users_connect():
    users_conn=pymssql.connect(server, user, password, "users")

def users_disconect():
    users_conn.close() 

