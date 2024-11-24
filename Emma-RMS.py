from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image
import SQLConnection
import Email_Inventory_Supplier

#Interface for Manager
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("CustomColor.json")

RMS_Logo_image= Image.open('RMS_logo_no_background.png')
RMS_Logo_image = customtkinter.CTkImage(light_image=RMS_Logo_image, size=(300,110))
burgerPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/All American Burger.jpg'), size=(110, 100)) 
SteakPic = customtkinter.CTkImage(light_image=Image.open(r'RMS_Database_Pictures/100% Totally Steak.png'), size=(110, 100))
saladPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Ceaser Salad.jpg'), size=(110, 100))
cevapiPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Cevapi.jpg'), size=(110, 100))
CocaColaPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Coca Cola.jpg'), size=(110, 100))
chickenFingersPic =  customtkinter.CTkImage(light_image=Image.open("RMS_Database_Pictures/Coney's Chicken Fingers.jpg"), size=(110, 100))
eggsPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Eggs Benedict.jpg'), size=(110, 100))
salmonPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Just Caught Salmon.jpg'), size=(110, 100))
lavenderlemonadePic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Lavendar Lemonade.jpg'), size=(110, 100))
lemonadePic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Lemonade.jpg'), size=(110, 100))
meditteranPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Meditteran Delight.jpg'), size=(110, 100))
peppermintMochaPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Peppermint Mocha.jpg'), size=(110, 100))
RoyalToastPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Royal Toast.jpg'), size=(110, 100))
mocktailPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Sunrise Mocktail.jpg'), size=(110, 100))
waterPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures/Water.jpg'), size=(110, 100))

managementUI = customtkinter.CTk()

screen_width = managementUI.winfo_screenwidth()
screen_height = managementUI.winfo_screenheight()

managementUI.title("Restaurant Management Solutions")
managementUI.geometry(f"{screen_width}x{screen_height - 100}+0+0")

# background_frame = customtkinter.CTkFrame(managementUI, width=screen_width, height=screen_height, fg_color="black") 
# background_frame.grid(row=0,column=0, rowspan=9, columnspan=2, sticky='nswe')

# Set dimensions for the "rectangle"
rect_width = 225
rect_height = screen_height 

managementUI.grid_rowconfigure(0, weight=0)
managementUI.grid_rowconfigure(1, weight=1)
managementUI.grid_columnconfigure(0, weight=0)
managementUI.grid_columnconfigure(1, weight=1)

# Create a top frame across the screen width 
top_frame = customtkinter.CTkFrame(managementUI, width=screen_width, height=150, fg_color="#525fc7") 
top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

top_label = customtkinter.CTkLabel(top_frame, text="The Anything Coney Island", text_color="black", font=("Hanuman", 78)) 
top_label.grid(row=0, column=2, pady=55, padx=180) #the pady and padx controls the height of the top rectangle box

top_frame.grid_rowconfigure(0,weight=1)
top_frame.grid_columnconfigure(0,weight=1)

# Create a frame to act as the rectangle (background for buttons)
left_frame = customtkinter.CTkFrame(managementUI, width=rect_width, height=rect_height, fg_color="#525fc7")
left_frame.grid(row=0, column=0, rowspan=8, sticky="nsw")

# Create a main content frame for dynamic content 
content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0")
content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

# Making Notifications Layout For Rita
notificationsLabel = customtkinter.CTkLabel(content_frame, text="Notification Manager", text_color="black", font=("Hanuman", 40)) 
notificationsLabel.grid(row = 1, column = 0, rowspan = 4,  padx = 20, pady = 20)


# Manager Button Definitions

# Schedule Button & Its Corresponding Buttons
def scheduleButton_clicked():
        customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, rowspan = 3, columnspan=8, sticky="nswe")

        schedueleTitle_label = customtkinter.CTkLabel(content_frame, text="Scheduele", font=(Hanuman, 40), text_color="black")
        schedueleTitle_label.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        
        schedueleTitle_description = customtkinter.CTkLabel(content_frame, text="Shifts are created on Google Calendars and imported into the table. Time off requests are made to be sent to the manager via email.", width = 150, font=(Hanuman, 18), text_color="black", anchor = "w", justify = "left")
        schedueleTitle_description.grid(row=1, column=0, padx=20, pady=20, sticky="nw")
    
        scheduele = SQLConnection.fetch_all("SELECT * FROM scheduele")
        print(scheduele)
        
        schedueleTable = ttk.Treeview(content_frame, columns=("Employee ID Number", "Employee Name","Shift Type", "Shift Time"), show = "headings")
        
        schedueleTable.heading("Employee ID Number", text = "Employee ID Number")
        schedueleTable.heading("Employee Name", text = "Employee Name")
        schedueleTable.heading("Shift Type", text = "Shift Time")
        schedueleTable.heading("Shift Time", text = "Shift Time")
        
        schedueleTable.column("Employee ID Number", anchor="center", width=60)
        schedueleTable.column("Employee Name", anchor="center", width=60)
        schedueleTable.column("Shift Type", anchor="center", width=60)
        schedueleTable.column("Shift Time", anchor="center", width=60)
        
        for item in scheduele:
            schedueleTable.insert("", "end", values=item)
        
        scrollbar = ttk.Scrollbar(schedueleTable, orient="vertical", command = schedueleTable.yview)
        schedueleTable.configure(yscroll = scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        schedueleTable.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = "nsew")
        scrollbar.grid(row = 2, column = 1, sticky = "ns")
        
        inventoryButtons_frame = customtkinter.CTkFrame(content_frame, fg_color = "#97B9E0")
        inventoryButtons_frame.grid(row = 3, column = 0, padx = 20, pady = 20, columnspan = 2, sticky="ew")
        
        makeChanges_button = customtkinter.CTkButton(inventoryButtons_frame, text = "Make Scheduele Changes", command = makeScheduele_clicked)
        shiftDuties_button = customtkinter.CTkButton(inventoryButtons_frame, text = "Shift Duties Checklist", command = shiftDuties_clicked)
        viewEmployeePerformance_button = customtkinter.CTkButton(inventoryButtons_frame, text = "View Employee Performance", command = viewEmployeePerformance_clicked)
        
        makeChanges_button.grid(row = 0, column = 0, padx = 15, pady= 15)
        shiftDuties_button.grid(row = 0, column = 1, padx = 15, pady = 15)
        viewEmployeePerformance_button.grid(row = 0, column = 2, padx = 15, pady = 15)
        
        content_frame.grid_rowconfigure(0, weight = 0)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_rowconfigure(2, weight=3)
        content_frame.grid_rowconfigure(3, weight=0)
        
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=0)

# Make Scheduele Changes Button
def makeScheduele_clicked():
    print("Clicked Make Scheduele")

# Shift Duties Button
def shiftDuties_clicked():
    print("Clicked Shift Duties")
    customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
    Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
    content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0") 
    content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

    LookUp_label = customtkinter.CTkLabel(content_frame, text="Shift Duties Checklist", font=(Hanuman, 80), text_color="black",underline= False)
    LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
    # Ensure the row and column in content_frame can expand to fill the space
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)
    

def viewEmployeePerformance_clicked():
    print("Clicked View Employee Performance")
        
# Earnings Button
def earningsButton_clicked():
        customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Earnings", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

# Transaction Button
def transactionsButton_clicked():
        customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Transaction", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

# Utilities
def utilitiesButton_clicked():
        customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        utilitiesLabel = customtkinter.CTkLabel(content_frame, text="Inventory Mangement", font=(Hanuman, 40), text_color="black")
        utilitiesLabel.grid(row=0, column=0, padx=20, pady=20, sticky="nw")  # Center the label within the frame

        inventory = SQLConnection.fetch_all("SELECT * FROM inventory")
        print(inventory)
        
        inventoryTable = ttk.Treeview(content_frame, columns=("Item ID", "Item Name","Item Quantity", "Ran Out"), show = "headings")
        
        inventoryTable.heading("Item ID", text = "Item ID")
        inventoryTable.heading("Item Name", text = "Item Name")
        inventoryTable.heading("Item Quantity", text = "Item Quantity")
        inventoryTable.heading("Ran Out", text = "Ran Out")
        
        inventoryTable.column("Item ID", anchor="center", width=60)
        inventoryTable.column("Item Name", anchor="center", width=60)
        inventoryTable.column("Item Quantity", anchor="center", width=60)
        inventoryTable.column("Ran Out", anchor="center", width=60)
        
        for item in inventory:
            inventoryTable.insert("", "end", values=item)
        
        scrollbar = ttk.Scrollbar(inventoryTable, orient="vertical", command = inventoryTable.yview)
        inventoryTable.configure(yscroll = scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        inventoryTable.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "nsew")
        scrollbar.grid(row = 1, column = 1, sticky = "ns")
        
        inventoryButtons_frame = customtkinter.CTkFrame(content_frame, fg_color = "#97B9E0")
        inventoryButtons_frame.grid(row = 2, column = 0, padx = 20, pady = 20, columnspan = 2, sticky="ew")
        
        contactSupplier_button = customtkinter.CTkButton(inventoryButtons_frame, text = "Contact Inventory Supplier", command = contactInventory_clicked)
        placeOrder_button = customtkinter.CTkButton(inventoryButtons_frame, text = "Place Order Restock")
        
        contactSupplier_button.grid(row = 0, column = 0, padx = 15, pady= 15)
        placeOrder_button.grid(row = 0, column = 1, padx = 15, pady = 15)
        
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_rowconfigure(2, weight=0)
        content_frame.grid_columnconfigure(0, weight=1)
def contactInventory_clicked():
    print("Clicked Contact Inventory Supplier")
    Email_Inventory_Supplier.sendEmail()

def placeOrder_clicked():
    print("Clicked Place Order")

# Time Clock
def timeClockButton_clciked():
        customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
        content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Time Clock", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)


#Commands for Buttons clicks
def homeButton_click(): # this button will switch from manager to employee view for now
#Start 
    customtkinter.set_appearance_mode("Light")
    customtkinter.set_default_color_theme("CustomColor.json")

    RMS_Logo_image= Image.open('RMS_logo_no_background.png')
    RMS_Logo_image = customtkinter.CTkImage(light_image=RMS_Logo_image, size=(300,110))

    customFont = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
    Hanuman = customtkinter.CTkFont(family="hanuman",size=40, slant= "italic")
    
    managementUI.destroy()
    employeeUI = customtkinter.CTk()

    screen_width = employeeUI.winfo_screenwidth()
    screen_height = employeeUI.winfo_screenheight()

    employeeUI.title("Restaurant Management Solutions")
    employeeUI.geometry(f"{screen_width}x{screen_height - 100}+0+0")

    # Set dimensions for the "rectangle"
    rect_width = 225
    rect_height = screen_height 

    employeeUI.grid_rowconfigure(0, weight=0)
    employeeUI.grid_rowconfigure(1, weight=1)
    employeeUI.grid_columnconfigure(0, weight=1)

    # Create a top frame across the screen width 
    top_frame = customtkinter.CTkFrame(employeeUI, width=screen_width, height=150, fg_color="#525fc7") 
    top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

    employeeUI.grid_columnconfigure(0, weight=1)
    employeeUI.grid_columnconfigure(1,weight=1)

    top_label = customtkinter.CTkLabel(top_frame, text="The Anything Coney Island", text_color="black", font=(Hanuman, 78)) 
    top_label.grid(row=0, column=2, pady=35, padx=180) #the pady and padx controls the height of the top rectangle box

    top_frame.grid_rowconfigure(0,weight=1)
    top_frame.grid_columnconfigure(0,weight=1)
    # Create a frame to act as the rectangle (background for buttons)
    left_frame = customtkinter.CTkFrame(employeeUI, width=rect_width, height=rect_height, fg_color="#525fc7")
    left_frame.grid(row=0, column=0, rowspan=8, sticky="nsw")

    # Create a main content frame for dynamic content 
    content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="white") 
    content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

    def clear_content_frame():
        for widget in content_frame.winfo_children():
            widget.destroy()

    #Food items class
    class FoodItem:
        def __init__(self,name,description,price,image_path):
            self.name = name 
            self.price = price
            self.description = description
            self.image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100,80))

    menu_items= [
        FoodItem("All American Burger","Meat, Bun, Lettuce, Tomato\n Onion, Pickle","$10.99","RMS_Database_Pictures/All American Burger.jpg" ),
        FoodItem("Eggs Benedict","Really Fancy Egss","$27.99","RMS_Database_Pictures/Eggs Benedict.jpg"),
        FoodItem("Meditteran Delight","A taste of the meditteranean sea","$14.99","RMS_Database_Pictures/Meditteran Delight.jpg"),
        FoodItem("Cevapi","An Albanian staple food","$8.99","RMS_Database_Pictures/Cevapi.jpg"),
        FoodItem("Chicken Fingers"," 3 Piece Chicken, French fries\n and ketchup","$9.99","RMS_Database_Pictures/Coney's Chicken Fingers.jpg"),
        FoodItem("100% Totally Steak","Steak, mashed potatoes\n and choice of vegetable","$22.99","RMS_Database_Pictures/100% Totally Steak.png"),
        FoodItem("Ceaser Salad","Lettuce, Crutons, Ceaser Dressing","$5.99","RMS_Database_Pictures/Ceaser Salad.jpg"),
        FoodItem("Salmon","Salmon, Brocolini, Potatoes, Rice","$18.99","RMS_Database_Pictures/Just Caught Salmon.jpg"),
        FoodItem("Water","PH 8 Water (H2O)","Free","RMS_Database_Pictures/Water.jpg"),
        FoodItem("Lemonade","Lemon and Sugar","$2.99","RMS_Database_Pictures/Lemonade.jpg"),
        FoodItem("Coca Cola","Coca Cola Products","$4.99","RMS_Database_Pictures/Coca Cola.jpg"),
        FoodItem("Lavender Lemonade","Lavender, Lemonade, and Lime","$6.99","RMS_Database_Pictures/Lavendar Lemonade.jpg"),
        FoodItem("Sunset Rise","Orange Juice, Lemons, Oranges\n Lime, and Mocktail Concentrate","$12.99","RMS_Database_Pictures/Sunrise Mocktail.jpg"),
        FoodItem("Peppermint Mocha Latte","Peppermint, Coffe Beans\n, Choice of Milk","$4.99","RMS_Database_Pictures/Peppermint Mocha.jpg"),
    ]
    # Button definitions 
    table_orders = {table: "" for table in ["1","2","3","4","5","6","7","8"]}
    order_counts = {item.name:0 for item in menu_items}
    # selected_table = "5"

    #Function to update the display text with the current order
    def update_order_display(content_frame, order_display, table_dropdown):
        selected_table = table_dropdown.get()
        order_text = "Current Order:\n"
        for item, count in order_counts.items():
            if count > 0:
                order_text += f"{item}: {count}\n"
        order_display.configure(text=order_text)
        if selected_table:
             table_orders[selected_table] = order_text

    def food_button_clicked(food_item, content_frame, order_display, table_dropdown):
        order_counts[food_item.name] += 1
        update_order_display(content_frame, order_display,table_dropdown)

    def specialsButton_clicked():
        pass #Specials interface
    
    # Employee Button Definitions

    def set_table(selection):
        print(f'Selected table: {selection}')
    
    # Look Up Button
        def lookUpButton_clicked():
            content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
            content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

            LookUp_label = customtkinter.CTkLabel(content_frame, text="Look Up", font=(Hanuman, 80), text_color="black",underline= True)
            LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
            
            # Ensure the row and column in content_frame can expand to fill the space
            content_frame.grid_rowconfigure(0, weight=1)
            content_frame.grid_columnconfigure(0, weight=1)

    def send_order_to_kitchen(content_frame, order_display,table_dropdown):
        selected_table = table_dropdown.get()  # Get the selected table from the dropdown

    # If no valid table is selected (i.e., "Select a Table"), do nothing
        if selected_table == "Select a Table":
            for item in order_counts:
                order_counts[item] = 0
            table_orders[selected_table] = ""
            return  # Exit early, do nothing
        else:
            print(f"Order sent to kitchen for table {selected_table}")
            print(f"Order details:\n{table_orders[selected_table]}")

    # Reset all order counts to zero
            for item in order_counts:
                order_counts[item] = 0
    
    # Clear the order for the selected table
            table_orders[selected_table] = ""

    # Update the order display to reflect the cleared order
            update_order_display(content_frame, order_display, table_dropdown)

    # Optional: Display confirmation message
            success_label = customtkinter.CTkLabel(
                content_frame,
                text=f"Order for table {selected_table} sent to kitchen successfully!",
                font=("Hanuman", 15),
                text_color="green",
            )
            success_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    # Reset the order display label text
            order_display.configure(text="Current Order:\n")  # Reset the display to indicate no order is active
                
    
    
    # Start Order Button
    def startOrder_clicked():

        employeeUI.grid_rowconfigure(1,weight=1)
        employeeUI.grid_columnconfigure(1,weight=1)
        

        for widget in content_frame.winfo_children():
             widget.destroy()

        content_frame1 = customtkinter.CTkFrame(employeeUI,width=1350,height=600, fg_color="#97B9E0") 
        content_frame1.grid(row=1, column=1, columnspan=8, sticky="nswe")
      

        order_display = customtkinter.CTkLabel(content_frame1, text="Current Order:", font=("Hanuman", 15), text_color="black")
        order_display.grid(row=5, column=3)

        tablenums = ['1','2','3','4','5','6','7','8']
        TableDropBox = customtkinter.CTkComboBox(content_frame1, values=tablenums,command=set_table)
        TableDropBox.set("Select a Table")
        TableDropBox.grid(row=0 , column=0 )

        SendToKitchenButton= customtkinter.CTkButton(content_frame1,text="Send To Kitchen",font=(Hanuman,25),command=send_order_to_kitchen(content_frame, order_display, TableDropBox))
        SendToKitchenButton.grid(row=5, column=0)

        specialsTitle_label = customtkinter.CTkLabel(content_frame1, text="Place Order", font=(Hanuman, 30), text_color="black")
        specialsTitle_label.grid(row=0, column=3)  # Center the label within the frame

        quantities_button = customtkinter.CTkButton(content_frame1, text='Check Quantities', font=('Hanuman', 20), command=quantities_clicked)
        quantities_button.grid(row=0, column=6, padx=20, sticky='e')

        order_display = customtkinter.CTkLabel(content_frame1,text= "Current Order:\n", font=(Hanuman,15), text_color="black")
        order_display.grid(row=5, column=3)

        burgerPic_button = customtkinter.CTkButton(content_frame1, image=burgerPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[0],content_frame1, order_display, TableDropBox)) 
        burgerPic_button.grid(row=1, column=0)
        burgerDescription = customtkinter.CTkLabel(content_frame1, text="All American\n Burger",font=(Hanuman,15), text_color="black")
        burgerDescription.grid(row=2,column=0)

        steakPic_button = customtkinter.CTkButton(content_frame1, image=SteakPic, text="", width=30, height=100,command=lambda: food_button_clicked(menu_items[5],content_frame1, order_display, TableDropBox))
        steakPic_button.grid(row=1, column=1)
        steakDescription = customtkinter.CTkLabel(content_frame1, text="100% Totally Steak",font=(Hanuman,15), text_color="black")
        steakDescription.grid(row=2, column=1)

        salmonPic_button = customtkinter.CTkButton(content_frame1, image=saladPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[7],content_frame1, order_display, TableDropBox))
        salmonPic_button.grid(row=1, column=2)
        salmonDescription = customtkinter.CTkLabel(content_frame1, text="Just Caught Salmon",font=(Hanuman,15), text_color="black")
        salmonDescription.grid(row=2, column=2)

        cevapiPic_button = customtkinter.CTkButton(content_frame1, image=cevapiPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[3],content_frame1, order_display, TableDropBox))
        cevapiPic_button.grid(row=1, column=3)
        cevapiDescription = customtkinter.CTkLabel(content_frame1, text="Cevapi",font=(Hanuman,15), text_color="black")
        cevapiDescription.grid(row=2, column=3)

        CocaColaPic_button = customtkinter.CTkButton(content_frame1, image=CocaColaPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[10],content_frame1, order_display, TableDropBox))
        CocaColaPic_button.grid(row=3, column=3)
        CocaColaPicDescription = customtkinter.CTkLabel(content_frame1, text="CocaCola",font=(Hanuman,15), text_color="black")
        CocaColaPicDescription.grid(row=4, column=3)
        
        chickenFingersPic_button = customtkinter.CTkButton(content_frame1, image=chickenFingersPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[4],content_frame1, order_display, TableDropBox))
        chickenFingersPic_button.grid(row=1, column=5)
        chickenFingersPicDescription = customtkinter.CTkLabel(content_frame1, text="Chicken Fingers",font=(Hanuman,15), text_color="black")
        chickenFingersPicDescription.grid(row=2, column=5)
        
        eggsPic_button = customtkinter.CTkButton(content_frame1, image=eggsPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[1],content_frame1, order_display, TableDropBox))
        eggsPic_button.grid(row=1, column=6)
        eggsPicDescription = customtkinter.CTkLabel(content_frame1, text="Eggs Benedict",font=(Hanuman,15), text_color="black")
        eggsPicDescription.grid(row=2, column=6)
        
        saladPic_button = customtkinter.CTkButton(content_frame1, image=salmonPic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[6],content_frame1, order_display, TableDropBox))
        saladPic_button.grid(row=3, column=0)
        saladPicDescription = customtkinter.CTkLabel(content_frame1, text="Ceaser Salad",font=(Hanuman,15), text_color="black")
        saladPicDescription.grid(row=4, column=0)
        
        lavenderlemonadePic_button = customtkinter.CTkButton(content_frame1, image=lavenderlemonadePic, text="", width=110, height=100,command=lambda: food_button_clicked(menu_items[11],content_frame1, order_display, TableDropBox))
        lavenderlemonadePic_button.grid(row=3, column=1)
        lavenderlemonadePicDescription = customtkinter.CTkLabel(content_frame1, text="Lavendar Lemonade",font=(Hanuman,15), text_color="black")
        lavenderlemonadePicDescription.grid(row=4, column=1)
        
        lemonadePic_button = customtkinter.CTkButton(content_frame1, image=lemonadePic, text="", width=100, height=80,command=lambda: food_button_clicked(menu_items[9],content_frame1, order_display, TableDropBox))
        lemonadePic_button.grid(row=3, column=2)
        lemonadePicDescription = customtkinter.CTkLabel(content_frame1, text="Lemonade",font=(Hanuman,15), text_color="black")
        lemonadePicDescription.grid(row=4, column=2)
        
        meditteranPic_button = customtkinter.CTkButton(content_frame1, image=meditteranPic, text="", width=100, height=80,command=lambda: food_button_clicked(menu_items[2],content_frame1, order_display, TableDropBox))
        meditteranPic_button.grid(row=1, column=4)
        meditteranPicDescription = customtkinter.CTkLabel(content_frame1, text="Meditteran Dish",font=(Hanuman,15), text_color="black")
        meditteranPicDescription.grid(row=2, column=4)
        
        peppermintMochaPic_button = customtkinter.CTkButton(content_frame1, image=peppermintMochaPic, text="", width=100, height=80,command=lambda: food_button_clicked(menu_items[13],content_frame1, order_display, TableDropBox))
        peppermintMochaPic_button.grid(row=3, column=4)
        peppermintMochaPicDescription = customtkinter.CTkLabel(content_frame1, text="Peppermint Mocha",font=(Hanuman,15), text_color="black")
        peppermintMochaPicDescription.grid(row=4, column=4)
        
        mocktailPic_button = customtkinter.CTkButton(content_frame1, image=mocktailPic, text="", width=100, height=80,command=lambda: food_button_clicked(menu_items[12],content_frame1, order_display, TableDropBox))
        mocktailPic_button.grid(row=3, column=5)
        mocktailPicDescription = customtkinter.CTkLabel(content_frame1, text="Mocktail",font=(Hanuman,15), text_color="black")
        mocktailPicDescription.grid(row=4, column=5)
       
        waterPic_button = customtkinter.CTkButton(content_frame1, image=waterPic, text="", width=100, height=80,command=lambda: food_button_clicked(menu_items[8],content_frame1, order_display, TableDropBox))
        waterPic_button.grid(row=3, column=6)
        waterPicDescription = customtkinter.CTkLabel(content_frame1, text="Water",font=(Hanuman,15), text_color="black")
        waterPicDescription.grid(row=4, column=6)

        for i in range(5):
            content_frame1.grid_rowconfigure(i, weight=1)
        for i in range(7):
            content_frame1.grid_columnconfigure(i, weight=1)


    def menuButton_clicked():


        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E1") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_rowconfigure(2, weight=1)
        content_frame.grid_rowconfigure(3, weight=1)
        content_frame.grid_rowconfigure(4, weight=1)
        content_frame.grid_rowconfigure(6, weight=1) 
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_columnconfigure(2, weight=1)
        content_frame.grid_columnconfigure(3, weight=1)
        content_frame.grid_columnconfigure(4, weight=1)
        content_frame.grid_columnconfigure(5, weight=1)
        content_frame.grid_columnconfigure(6, weight=1) 
        
        specialsTitle_label = customtkinter.CTkLabel(content_frame, text="                     Anything Coney Island's Menu", font=("Hanuman", 20), text_color="black",height=70) 
        specialsTitle_label.grid(row=0, column=1, columnspan=3, pady=20, sticky="nsew")

        for i, item in enumerate(menu_items): 
            row = (i // 3) + 1 # Adjust the row based on the number of columns (3 in this example) 
            col_image = (i % 3) * 2 + 1
            col_Label = col_image -1 
            
            # Create a button for the image 
            item_button = customtkinter.CTkLabel(content_frame, image=item.image, text="", width=110, height=100) 
            item_button.grid(row=row*2-1, column=col_image, padx=10, pady=10, sticky="e") 
            # Create a label for the item details 
            item_label = customtkinter.CTkLabel(content_frame, text=f"{item.name}\n{item.description}\n{item.price}", font=("Hanuman", 15), text_color="black")
            item_label.grid(row=row*2-1, column=col_Label, sticky="w") 
            
            # Ensure the rows and columns in content_frame can expand to fill the space 
            for i in range((len(menu_items) // 3 + 1) * 2): # Adjust based on the number of rows used 
                content_frame.grid_rowconfigure(i, weight=1) 
                for i in range(6): # Adjust based on the number of columns used (3 items per row, each with 2 columns: label and image) 
                    content_frame.grid_columnconfigure(i, weight=1)
        

    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_rowconfigure(2, weight=1)
        content_frame.grid_rowconfigure(3, weight=1)
        content_frame.grid_rowconfigure(4, weight=1)
        content_frame.grid_rowconfigure(5, weight=1)
        content_frame.grid_rowconfigure(6, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_columnconfigure(2, weight=1)
        content_frame.grid_columnconfigure(3, weight=1)
        content_frame.grid_columnconfigure(4, weight=1)
        content_frame.grid_columnconfigure(5, weight=1)
        content_frame.grid_columnconfigure(6, weight=1)
        content_frame.grid_columnconfigure(7, weight=1)
        content_frame.grid_columnconfigure(8, weight=1)
    
    # View Order Button
    def viewOrder_clicked():
    
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        viewOrdersTitle_label = customtkinter.CTkLabel(content_frame, text="All Active orders", font=(Hanuman, 30), text_color="black")
        viewOrdersTitle_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame

        row = 1
        for table, order in table_orders.items():
            if table == "Select a Table":
                break
            else:
             table_label = customtkinter.CTkLabel(content_frame, text=f"Table {table} Order", font=(Hanuman,20), text_color="black")
             table_label.grid(row=row, column = 0, padx = 10,pady=10, sticky="w")


             order_display = customtkinter.CTkLabel(content_frame, text=order, font=(Hanuman,15),text_color="black")
             order_display.grid(row=row, column=1, padx=10, pady=10, sticky="w")
             row += 1 
        for i in range(row):
             content_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
             content_frame.grid_columnconfigure(i, weight=1)
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
    # Table Mangement Button
    def tableManagement_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nsew")

        # table_label = customtkinter.CTkLabel(content_frame, text="Table Map", font=(Hanuman, 60), text_color="black")
        # table_label.grid(row=0, column=0, padx=20, pady=20,  sticky="n")

        tableMap = customtkinter.CTkImage(light_image=Image.open('table-map.png'), size=(782, 506))
        tableMap_label = customtkinter.CTkLabel(content_frame, image=tableMap, text="")
        tableMap_label.grid(row=2, column=0, sticky='nsew')

        yourTables_label = customtkinter.CTkLabel(content_frame, text="Your Tables:\n1 2 3", font=(customFont), text_color="black")
        yourTables_label.grid(row=3, column=0, padx=20, pady=20, sticky="s")

        capacity_button = customtkinter.CTkButton(content_frame, text="Check Capacity", width=100, height=60, command=capacity_clicked)
        capacity_button.grid(row=3, column=0, padx=20, sticky='w')
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

    # Capacity Button, found on Table Management Page
    def capacity_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nsew")

        capacityTitle_label = customtkinter.CTkLabel(content_frame, text="Restaurant Capacity", font=(Hanuman, 60), text_color="black")
        capacityTitle_label.grid(row=0, column=0, padx=20, pady=30,  sticky="n")

        table = ttk.Treeview(content_frame, columns=("Table #", "Guests"), show="headings", height=8)
        table.heading("Table #", text="Table #")
        table.heading("Guests", text="Guests")
        table.column("Table #", width=300, anchor="center")
        table.column("Guests", width=300, anchor="center")

        style = ttk.Style()
        style.configure("Treeview", rowheight=40, font=("Hanuman", 20))  # Change font for table content
        style.configure("Treeview.Heading", font=("Hanuman", 30, "bold"))

        data = [
            (1, 4),
            (2, 2),
            (3, 4),
            (4, 3),
            (5, 2),
            (6, 0),
            (7, 0),
            (8, 0)
        ]

        for row in data:
            table.insert("", "end", values=row)

        table.grid(row=1, column=0)

        capacity_label = customtkinter.CTkLabel(content_frame, text="Customers: 15/32\nEmployees: 5/10\nTotal Occupants: 20/42", font=('Hanuman', 30), text_color="black")
        capacity_label.grid(row=3, column=0, padx=20, pady=20, sticky="s")

        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

    # Quantities Button
    def quantities_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nsew")

        quantities_label = customtkinter.CTkLabel(content_frame, text="Be Aware", font=("Hanuman", 60), text_color="black")
        quantities_label.grid(row=0, column=0, padx=20, pady=20,  sticky="nsew")

        itemQuantities_label = customtkinter.CTkLabel(content_frame, font=("Hanuman", 25), text="We are low on:\nLemonade (3 portions left)\nChicken Fingers (2 portions left)\nCevapi (1 portion left)")
        itemQuantities_label.grid(row=1, column=0, pady=200, sticky='nsew')

        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
    # Specials Button
    def specialsButton_clicked(): #Specials interface
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        specialsTitle_label = customtkinter.CTkLabel(content_frame, text="Specials", font=(Hanuman, 80), text_color="black",underline= True)
        specialsTitle_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame

        specials_label = customtkinter.CTkLabel(content_frame, text="Monday:\n $1 Koney Dogs\n Tuesday\n$1 Chicken Lemon Rice Soup\nWednesday\n Free Side of chili cheese fries with every meal\nThursday\n Free desert of your choice after spending $40\nFriday\n $3 Gyros(chicken or Lamb)", font=(customFont), text_color="black")
        specials_label.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

    def managerCode():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        code_label = customtkinter.CTkLabel(content_frame, text="Enter passcode:", font=(Hanuman, 50), text_color="black")
        code_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        password_field = customtkinter.CTkEntry(content_frame, placeholder_text="Manager ID Login", show="*", width=200, font=("Hanuman", 14))
        password_field.grid(row=0, column=0)

        submit_Button = customtkinter.CTkButton(content_frame, text="Submit", width=200, height=50)
        submit_Button.grid(row=1, column=0, pady=20, sticky='s')

        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

    switchToManager_Button = customtkinter.CTkButton(top_frame, text="Manager\nView", width=100, height= 60, command=managerCode)
    switchToManager_Button.grid(row = 0, column = 3, rowspan = 8, sticky = "nswe")

# Employee Buttons Defined
    # Command Already Added
    logo = customtkinter.CTkLabel(left_frame, text="", image=RMS_Logo_image, width=100, height=100) # Just Logo No Command
    homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100,command= homeButton_click)
    MenuButton = customtkinter.CTkButton(left_frame, text="Menu", width=200, height=100,command=menuButton_clicked)
    # lookUpButton = customtkinter.CTkButton(left_frame, text="Look Up (Allergies)", width=200, height=100, command = lookUpButton_clicked)
    # lookUpButton = customtkinter.CTkButton(left_frame, text="Look Up (Allergies)", width=200, height=100, command = lookUpButton_clicked)
    startOrderButton = customtkinter.CTkButton(left_frame, text="Start Order", width=200, height=100,command=startOrder_clicked)
    viewOrdersButton = customtkinter.CTkButton(left_frame, text="View Active Orders", width=200, height=100, command = viewOrder_clicked)
    tableManagementButton = customtkinter.CTkButton(left_frame, text="Table Management", width=200, height=100, command = tableManagement_clicked)
    viewOrdersButton = customtkinter.CTkButton(left_frame, text="View Active Orders", width=200, height=100, command = viewOrder_clicked)
    tableManagementButton = customtkinter.CTkButton(left_frame, text="Table Management", width=200, height=100, command = tableManagement_clicked)
    specialsButton = customtkinter.CTkButton(left_frame, text="Specials", width=200, height=100,command=specialsButton_clicked)

    for i in range(8): 
        left_frame.grid_rowconfigure(i, weight=1) 
    left_frame.grid_columnconfigure(0, weight=1)

    logo.grid(row=0, column=0, pady=30, padx=10)
    homeButton.grid(row=2, column=0, pady=10, padx=10)
    MenuButton.grid(row=3, column=0, pady=10, padx=10)
    startOrderButton.grid(row=4, column=0, pady=10, padx=10)
    viewOrdersButton.grid(row=5, column=0, pady=10, padx=10)
    tableManagementButton.grid(row=6, column=0, pady=10, padx=10)
    specialsButton.grid(row=7, column=0, pady=10, padx=10,)

    employeeUI.mainloop()

# Manager Buttons
    # Command Already Added
# Manager Buttons
    # Command Already Added
logo = customtkinter.CTkLabel(left_frame, text="", image=RMS_Logo_image, width=100, height=100)
homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100)
scheduleButton = customtkinter.CTkButton(left_frame, text="Schedule", width=200, height=100, command = scheduleButton_clicked)
earningsButton = customtkinter.CTkButton(left_frame, text="Earnings", width=200, height=100, command = earningsButton_clicked)
transactionButton = customtkinter.CTkButton(left_frame, text="Transaction", width=200, height=100, command = transactionsButton_clicked)
utilitiesButton = customtkinter.CTkButton(left_frame, text="Utilities", width=200, height=100, command = utilitiesButton_clicked)
TimeClockButton = customtkinter.CTkButton(left_frame, text="TimeClock", width=200, height=100, command = timeClockButton_clciked)

# Button For Manager Switch -> Employee on manager screen
switchToEmployee_Button = customtkinter.CTkButton(top_frame, text="Switch\nView", width=100, height= 60, command=homeButton_click)
switchToEmployee_Button.grid(row = 0, column = 3, rowspan = 8, padx=15)

# Button to switch to manager view from employee view



for i in range(8): 
    left_frame.grid_rowconfigure(i, weight=1) 
left_frame.grid_columnconfigure(0, weight=1)

logo.grid(row=0, column=0, pady=30, padx=10)
homeButton.grid(row=2, column=0, pady=10, padx=10)
scheduleButton.grid(row=3, column=0, pady=10, padx=10)
earningsButton.grid(row=4, column=0, pady=10, padx=10)
transactionButton.grid(row=5, column=0, pady=10, padx=10)
utilitiesButton.grid(row=6, column=0, pady=10, padx=10)
TimeClockButton.grid(row=7, column=0, pady=10, padx=10)

managementUI.mainloop()