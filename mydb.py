import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = 'koda0621'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE pedidos")

print("all done")