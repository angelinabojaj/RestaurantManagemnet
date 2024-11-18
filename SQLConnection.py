# Preform the following: pip install mysql-connector-python
import mysql.connector

# This will be subjected to change for everyone
connection = mysql.connector.connect(
        host="127.0.0.1", # Subject to change
        user = "root", # Subject to change
        password = "334Mommy!!", # Put your root password here
        database = "rma") # Put your database name here

mycursor = connection.cursor()

mycursor.execute("SELECT * FROM employee")

myresult = mycursor.fetchall()

for x in myresult:
        print(x)