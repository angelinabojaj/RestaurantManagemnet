from tkinter import *
import customtkinter

#Interface for Manager
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("CustomColor.json")

managementUI = customtkinter.CTk()

screen_width = managementUI.winfo_screenwidth()
screen_height = managementUI.winfo_screenheight()

managementUI.title("Restaurant Management Solutions")
managementUI.geometry(f"{screen_width}x{screen_height - 100}+0+0")

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

    def specialsButton_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        specialsTitle_label = customtkinter.CTkLabel(content_frame, text="Specials", font=(Hanuman, 80), text_color="black",underline= True)
        specialsTitle_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame

        specials_label = customtkinter.CTkLabel(content_frame, text="Monday:\n $1 Koney Dogs\n Tuesday\n$1 Chicken Lemon Rice Soup\nWednesday\n Free Side of chili cheese fries with every meal\nThursday\n Free desert of your choice after spending $40\nFriday\n $3 Gyros(chicken or Lamb)", font=(customFont), text_color="black")
        specials_label.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")  # Center the label within the frame
    
        # Ensure the row and column in content_frame can expand to fill the space
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

    logo = customtkinter.CTkButton(left_frame, text="RMS LOGO INSERT HERE", width=100, height=100)
    spacer = customtkinter.CTkLabel(left_frame, text="", width=rect_width, height= 100, fg_color="#525fc7")
    homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100,command= homeButton_click)
    lookUpButton = customtkinter.CTkButton(left_frame, text="Look Up (Allergies)", width=200, height=100)
    startOrderButton = customtkinter.CTkButton(left_frame, text="Start Order", width=200, height=100)
    viewOrdersButton = customtkinter.CTkButton(left_frame, text="View Active Orders", width=200, height=100)
    tableManagementButton = customtkinter.CTkButton(left_frame, text="Table Management", width=200, height=100)
    DeliveriesButton = customtkinter.CTkButton(left_frame, text="Deliveries", width=200, height=100,command=specialsButton_clicked)

    for i in range(8): 
        left_frame.grid_rowconfigure(i, weight=1) 
    left_frame.grid_columnconfigure(0, weight=1)

    logo.grid(row=0, column=0, pady=10, padx=10)
    spacer.grid(row=1, column=0)
    homeButton.grid(row=2, column=0, pady=10, padx=10)
    lookUpButton.grid(row=3, column=0, pady=10, padx=10)
    startOrderButton.grid(row=4, column=0, pady=10, padx=10)
    viewOrdersButton.grid(row=5, column=0, pady=10, padx=10)
    tableManagementButton.grid(row=6, column=0, pady=10, padx=10)
    DeliveriesButton.grid(row=7, column=0, pady=10, padx=10,)

    employeeUI.mainloop()




#Stop
logo = customtkinter.CTkButton(left_frame, text="RMS LOGO INSERT HERE", width=100, height=100)
spacer = customtkinter.CTkLabel(left_frame, text="", width=rect_width, height= 100, fg_color="#525fc7")
homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100,command= homeButton_click)
scheduleButton = customtkinter.CTkButton(left_frame, text="Schedule", width=200, height=100)
earningsButton = customtkinter.CTkButton(left_frame, text="Earnings", width=200, height=100)
transactionButton = customtkinter.CTkButton(left_frame, text="Transaction", width=200, height=100)
utilitiesButton = customtkinter.CTkButton(left_frame, text="Utilities", width=200, height=100)
TimeClockButton = customtkinter.CTkButton(left_frame, text="TimeClock", width=200, height=100)

for i in range(8): 
    left_frame.grid_rowconfigure(i, weight=1) 
left_frame.grid_columnconfigure(0, weight=1)

logo.grid(row=0, column=0, pady=10, padx=10)
spacer.grid(row=1, column=0)
homeButton.grid(row=2, column=0, pady=10, padx=10)
scheduleButton.grid(row=3, column=0, pady=10, padx=10)
earningsButton.grid(row=4, column=0, pady=10, padx=10)
transactionButton.grid(row=5, column=0, pady=10, padx=10)
utilitiesButton.grid(row=6, column=0, pady=10, padx=10)
TimeClockButton.grid(row=7, column=0, pady=10, padx=10)



managementUI.mainloop()
