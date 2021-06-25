import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db="user_manag",
)

if con.is_connected():
    print("Sukses")

tabel = con.cursor()
tabel.execute("create table if not exists users(id int NOT NULL auto_increment, "
                "username varchar(100), password varchar(100), name varchar(100), PRIMARY KEY(id), CONSTRAINT UNIQUE (username))")
                
                
