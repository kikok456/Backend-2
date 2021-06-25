import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

if con.is_connected():
    print("Sukses")

db = con.cursor()
db.execute("create database user_manag")