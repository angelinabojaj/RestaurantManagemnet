# Preform the following: pip install mysql-connector-python
import mysql.connector

# This will be subjected to change for everyone
connection = mysql.connector.connect(
        host="127.0.0.1", # Subject to change
        user = "root", # Subject to change
        password = "334Mommy!!", # Put your root password here
        database = "rms") # Put your database name here

mycursor = connection.cursor()

mycursor.execute("SELECT * FROM employee")

myresult = mycursor.fetchall()

# Fetch_All
        # If your calling a table to be viewed be sure to call this function.
def fetch_all(query):
   try:
        connection = mysql.connector.connect(
        host="127.0.0.1", # Subject to change
        user = "root", # Subject to change
        password = "334Mommy!!", # Put your root password here
        database = "rms" # Put your database name here
        )
        mycursor = connection.cursor()
        mycursor.execute(query)
        results = mycursor.fetchall()
        connection.close()
        return results

   except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
                
# Functions For Different Tables
        # Import this file into the GUI (Which it is already)
        # Functions can be called by using the file import name followed my a decimal.
                # Example: SQLConnection.show_menu()
# Shows menu
def show_menu():
        mycursor.execute("SELECT * FROM menu")
        print("Menu Shown")

# Shows notifcications     
def show_notifications():
        mycursor.execute("SELECT * FROM notifications")
        print("Notificationa Shown")

# Show orders
def show_orders():
        mycursor.execute("SELECT * FROM orders")
        print("Orders Shown")

# Show shift duties
def show_shiftDuties():
        mycursor.execute("SELECT * FROM shift_duties")
        print("Shift Duties Shown")     
       
def show_HostDuties():
        mycursor.execute("SELECT shift, shiftDescription FROM shift_duties WHERE shift = ?") 

# Show scheduele
def show_scheduele():
        mycursor.execute("SELECT employeeIDNumber, shiftDay, shiftTime FROM scheduele WHERE shift = ?")
        print("Scheduele Shown")

def show_absent_request():
        mycursor.execute("SELECT * FROM absent_request")
        print("Absent Request Shown")

def show_inventory():
        inventory = mycursor.fetchall("SELECT * FROM inventory")
        print("Inventory Shown")
