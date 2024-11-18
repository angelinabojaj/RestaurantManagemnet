# Preform the following: pip install mysql-connector-python
import mysql.connector

# This will be subjected to change for everyone
connection = mysql.connector.connect(
        host="127.0.0.1", # Subject to change
        user = "root", # Subject to change
        password = "334Mommy!!", # Put your root password here
        database = "rms") # Put your database name here

mycursor = connection.cursor()

mycursor.execute("SELECT * FROM menu")

myresult = mycursor.fetchall()

for x in myresult:
        print(x)

# Functions For Different Tables
        # Import this file into the GUI (Which it is already)
        # Functions can be called by using the file import name followed my a decimal.
                # Example: SQLConnection.show_menu()
# Shows menu
def show_menu():
        mycursor.execute("SELECT * FROM menu")
        
        #  Add code to GUI for display
        
        print("Menu Shown")

# Shows notifcications     
def show_notifications():
        mycursor.execute("SELECT * FROM notifications")
        
        #  Add code to GUI for display
        
        print("Notificationa Shown")

# Show orders
def show_orders():
        mycursor.execute("SELECT * FROM orders")
        
        #  Add code to GUI for display
        
        print("Orders Shown")

# Show shift duties
def show_shiftDuties():
        mycursor.execute("SELECT * FROM shift_duties")
        
        # Add code to GUI for display
        
        print("Shift Duties Shown")     
        

# Show scheduele
def show_scheduele():
        mycursor.execute("SELECT * FROM scheduele")
        
        #  Add code to GUI for display
        
        print("Scheduele Shown")

def show_absent_request():
        mycursor.execute("SELECT * FROM absent_request")
        
        #  Add code to GUI for display
        
        print("Absent Request Shown")