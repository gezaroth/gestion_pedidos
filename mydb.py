import mysql.connector

dataBase = mysql.connector.connect(
    host = 'host',
    user= 'user',
    passwd = 'passwrd'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE pedidos")

print("all done")
