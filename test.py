import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    passwd="",
    database="testdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE replays")
