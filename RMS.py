from tkinter import *
import customtkinter
from PIL import Image

#Interface for Manager
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("CustomColor.json")

RMS_Logo_image= Image.open('RMS_logo_no_background.png')
RMS_Logo_image = customtkinter.CTkImage(light_image=RMS_Logo_image, size=(300,110))
burgerPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\All American Burger.jpg'), size=(50, 50)) # Example for burgerPic

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
managementUI.grid_columnconfigure(0, weight=1)
managementUI.grid_columnconfigure(1, weight=1)

# Create a top frame across the screen width 
top_frame = customtkinter.CTkFrame(managementUI, width=screen_width, height=150, fg_color="#525fc7") 
top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

top_label = customtkinter.CTkLabel(top_frame, text="The Anything Coney Island", text_color="black", font=("Hanuman", 78)) 
top_label.grid(row=0, column=2, pady=35, padx=180) #the pady and padx controls the height of the top rectangle box

top_frame.grid_rowconfigure(0,weight=1)
top_frame.grid_columnconfigure(0,weight=1)


# Create a frame to act as the rectangle (background for buttons)
left_frame = customtkinter.CTkFrame(managementUI, width=rect_width, height=rect_height, fg_color="#525fc7")
left_frame.grid(row=0, column=0, rowspan=8, sticky="nsw")

# Create a main content frame for dynamic content 
content_frame = customtkinter.CTkFrame(managementUI,width=1350, fg_color="red") 
content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")


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
    content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="green") 
    content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

    
    # Employee Button Definitions
    
    # Look Up Button
    def lookUpButton_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Look Up", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
    # Buttons (In Order They Appear)
    def lookUpButton_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Look Up", font=(Hanuman, 80), text_color="black",underline= True)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
        # Start Order Button
    def startOrder_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        burgerPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\All American Burger.jpg'), size=(100, 80)) # Example for burgerPic

        specialsTitle_label = customtkinter.CTkLabel(content_frame, text="Place Order", font=(Hanuman, 80), text_color="black")
        specialsTitle_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame

        burgerPic_button = customtkinter.CTkButton(content_frame, image=burgerPic, text="", width=100, height=80) 
        burgerPic_button.grid(row=1, column=0)
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
    # View Order Button
    def viewOrder_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        burgerPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\All American Burger.jpg'), size=(100, 80)) # Example for burgerPic

        specialsTitle_label = customtkinter.CTkLabel(content_frame, text="View Order", font=(Hanuman, 80), text_color="black")
        specialsTitle_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame

        burgerPic_button = customtkinter.CTkButton(content_frame, image=burgerPic, text="", width=100, height=80) 
        burgerPic_button.grid(row=1, column=0)
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
    def tableManagement_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Table Management", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
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

# Manager Button Definitions
    def scheduleButton_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Scheduele", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    
    def earningsButton_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        LookUp_label = customtkinter.CTkLabel(content_frame, text="Earnings", font=(Hanuman, 80), text_color="black",underline= False)
        LookUp_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
    


# Employee Buttons Defined
    # Command Already Added
    logo = customtkinter.CTkLabel(left_frame, text="", image=RMS_Logo_image, width=100, height=100) # Just Logo No Command
    homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100,command= homeButton_click)
    lookUpButton = customtkinter.CTkButton(left_frame, text="Look Up (Allergies)", width=200, height=100, command = lookUpButton_clicked)
    startOrderButton = customtkinter.CTkButton(left_frame, text="Start Order", width=200, height=100,command=startOrder_clicked)
    viewOrdersButton = customtkinter.CTkButton(left_frame, text="View Active Orders", width=200, height=100, command = viewOrder_clicked)
    tableManagementButton = customtkinter.CTkButton(left_frame, text="Table Management", width=200, height=100, command = tableManagement_clicked)
    specialsButton = customtkinter.CTkButton(left_frame, text="Specials", width=200, height=100,command=specialsButton_clicked)

    for i in range(8): 
        left_frame.grid_rowconfigure(i, weight=1) 
    left_frame.grid_columnconfigure(0, weight=1)

    logo.grid(row=0, column=0, pady=30, padx=10)
    homeButton.grid(row=2, column=0, pady=10, padx=10)
    lookUpButton.grid(row=3, column=0, pady=10, padx=10)
    startOrderButton.grid(row=4, column=0, pady=10, padx=10)
    viewOrdersButton.grid(row=5, column=0, pady=10, padx=10)
    tableManagementButton.grid(row=6, column=0, pady=10, padx=10)
    specialsButton.grid(row=7, column=0, pady=10, padx=10,)

    employeeUI.mainloop()

# Manager Buttons
    # Command Already Added
logo = customtkinter.CTkLabel(left_frame, text="", image=RMS_Logo_image, width=100, height=100)
homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100,command= homeButton_click)
scheduleButton = customtkinter.CTkButton(left_frame, text="Schedule", width=200, height=100)
earningsButton = customtkinter.CTkButton(left_frame, text="Earnings", width=200, height=100)
transactionButton = customtkinter.CTkButton(left_frame, text="Transaction", width=200, height=100)
utilitiesButton = customtkinter.CTkButton(left_frame, text="Utilities", width=200, height=100)
TimeClockButton = customtkinter.CTkButton(left_frame, text="TimeClock", width=200, height=100)

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