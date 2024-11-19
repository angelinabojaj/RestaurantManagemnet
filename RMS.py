from tkinter import *
import customtkinter
from PIL import Image

#Interface for Manager
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("CustomColor.json")

RMS_Logo_image= Image.open('RMS_logo_no_background.png')
RMS_Logo_image = customtkinter.CTkImage(light_image=RMS_Logo_image, size=(300,110))
burgerPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\All American Burger.jpg'), size=(110, 100)) 
SteakPic = customtkinter.CTkImage(light_image=Image.open(r'RMS_Database_Pictures\100% Totally Steak.png'), size=(110, 100))
saladPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Ceaser Salad.jpg'), size=(110, 100))
cevapiPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Cevapi.jpg'), size=(110, 100))
CocaColaPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Coca Cola.jpg'), size=(110, 100))
chickenFingersPic =  customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Coney\'s Chicken Fingers.jpg'), size=(110, 100))
eggsPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Eggs Benedict.jpg'), size=(110, 100))
salmonPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Just Caught Salmon.jpg'), size=(110, 100))
lavenderlemonadePic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Lavendar Lemonade.jpg'), size=(110, 100))
lemonadePic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Lemonade.jpg'), size=(110, 100))
meditteranPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Meditteran Delight.jpg'), size=(110, 100))
peppermintMochaPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Peppermint Mocha.jpg'), size=(110, 100))
RoyalToastPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Royal Toast.jpg'), size=(110, 100))
mocktailPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Sunrise Mocktail.jpg'), size=(110, 100))
waterPic = customtkinter.CTkImage(light_image=Image.open('RMS_Database_Pictures\Water.jpg'), size=(110, 100))

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

    #Food items class
    class FoodItem:
        def __init__(self,name,description,price,image_path):
            self.name = name 
            self.price = price
            self.description = description
            self.image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100,80))

    menu_items= [
        FoodItem("All American Burger","Meat, Bun, Lettuce, Tomato\n Onion, Pickle","$10.99","RMS_Database_Pictures\All American Burger.jpg" ),
        FoodItem("Eggs Benedict","Really Fancy Egss","$27.99","RMS_Database_Pictures\Eggs Benedict.jpg"),
        FoodItem("Meditteran Delight","A taste of the meditteranean sea","$14.99","RMS_Database_Pictures\Meditteran Delight.jpg"),
        FoodItem("Cevapi","An Albanian staple food","$8.99","RMS_Database_Pictures\Cevapi.jpg"),
        FoodItem("Chicken Fingers"," 3 Piece Chicken, French fries\n and ketchup","$9.99","RMS_Database_Pictures\Coney's Chicken Fingers.jpg"),
        FoodItem("100% Totally Steak","Steak, mashed potatoes\n and choice of vegetable","$22.99",r"RMS_Database_Pictures\100% Totally Steak.png"),
        FoodItem("Ceaser Salad","Lettuce, Crutons, Ceaser Dressing","$5.99","RMS_Database_Pictures\Ceaser Salad.jpg"),
        FoodItem("Salmon","Salmon, Brocolini, Potatoes, Rice","$18.99","RMS_Database_Pictures\Just Caught Salmon.jpg"),
        FoodItem("Water","PH 8 Water (H2O)","Free","RMS_Database_Pictures\Water.jpg"),
        FoodItem("Lemonade","Lemon and Sugar","$2.99","RMS_Database_Pictures\Lemonade.jpg"),
        FoodItem("Coca Cola","Coca Cola Products","$4.99","RMS_Database_Pictures\Coca Cola.jpg"),
        FoodItem("Lavender Lemonade","Lavender, Lemonade, and Lime","$6.99","RMS_Database_Pictures\Lavendar Lemonade.jpg"),
        FoodItem("Sunset Rise","Orange Juice, Lemons, Oranges\n Lime, and Mocktail Concentrate","$12.99","RMS_Database_Pictures\Sunrise Mocktail.jpg"),
        FoodItem("Peppermint Mocha Latte","Peppermint, Coffe Beans\n, Choice of Milk","$4.99","RMS_Database_Pictures\Peppermint Mocha.jpg"),
    ]
    # Button definitions 

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
    
    def startOrder_clicked():
        content_frame = customtkinter.CTkFrame(employeeUI,width=1350, fg_color="#97B9E0") 
        content_frame.grid(row=1, column=1, columnspan=8, sticky="nswe")

        SendToKitchenButton= customtkinter.CTkButton(content_frame,text="Send To Kitchen",font=(Hanuman,25))
        SendToKitchenButton.grid(row=5, column=0)

        tablenums = ['1','2','3','4','5','6','7','8']
        TableDropBox = customtkinter.CTkComboBox(content_frame, values=tablenums)
        TableDropBox.set("Select a Table")
        TableDropBox.grid(row=0 , column=0 )

        specialsTitle_label = customtkinter.CTkLabel(content_frame, text="Place Order", font=(Hanuman, 30), text_color="black")
        specialsTitle_label.grid(row=0, column=3)  # Center the label within the frame

        burgerPic_button = customtkinter.CTkButton(content_frame, image=burgerPic, text="", width=110, height=100) 
        burgerPic_button.grid(row=1, column=0)
        burgerDescription = customtkinter.CTkLabel(content_frame, text="All American\n Burger",font=(Hanuman,15), text_color="black")
        burgerDescription.grid(row=2,column=0)

        steakPic_button = customtkinter.CTkButton(content_frame, image=SteakPic, text="", width=30, height=10)
        steakPic_button.grid(row=1, column=1)
        steakDescription = customtkinter.CTkLabel(content_frame, text="100% Totally Steak",font=(Hanuman,15), text_color="black")
        steakDescription.grid(row=2, column=1)

        salmonPic_button = customtkinter.CTkButton(content_frame, image=saladPic, text="", width=110, height=100)
        salmonPic_button.grid(row=1, column=2)
        salmonDescription = customtkinter.CTkLabel(content_frame, text="Just Caught Salmon",font=(Hanuman,15), text_color="black")
        salmonDescription.grid(row=2, column=2)

        cevapiPic_button = customtkinter.CTkButton(content_frame, image=cevapiPic, text="", width=110, height=100)
        cevapiPic_button.grid(row=1, column=3)
        cevapiDescription = customtkinter.CTkLabel(content_frame, text="Cevapi",font=(Hanuman,15), text_color="black")
        cevapiDescription.grid(row=2, column=3)

        CocaColaPic_button = customtkinter.CTkButton(content_frame, image=CocaColaPic, text="", width=110, height=100)
        CocaColaPic_button.grid(row=3, column=3)
        CocaColaPicDescription = customtkinter.CTkLabel(content_frame, text="CocaCola",font=(Hanuman,15), text_color="black")
        CocaColaPicDescription.grid(row=4, column=3)
        
        chickenFingersPic_button = customtkinter.CTkButton(content_frame, image=chickenFingersPic, text="", width=110, height=100)
        chickenFingersPic_button.grid(row=1, column=5)
        chickenFingersPicDescription = customtkinter.CTkLabel(content_frame, text="Chicken Fingers",font=(Hanuman,15), text_color="black")
        chickenFingersPicDescription.grid(row=2, column=5)
        
        eggsPic_button = customtkinter.CTkButton(content_frame, image=eggsPic, text="", width=110, height=100)
        eggsPic_button.grid(row=1, column=6)
        eggsPicDescription = customtkinter.CTkLabel(content_frame, text="Eggs Benedict",font=(Hanuman,15), text_color="black")
        eggsPicDescription.grid(row=2, column=6)
        
        saladPic_button = customtkinter.CTkButton(content_frame, image=salmonPic, text="", width=110, height=100)
        saladPic_button.grid(row=3, column=0)
        saladPicDescription = customtkinter.CTkLabel(content_frame, text="Ceaser Salad",font=(Hanuman,15), text_color="black")
        saladPicDescription.grid(row=4, column=0)
        
        lavenderlemonadePic_button = customtkinter.CTkButton(content_frame, image=lavenderlemonadePic, text="", width=110, height=100)
        lavenderlemonadePic_button.grid(row=3, column=1)
        lavenderlemonadePicDescription = customtkinter.CTkLabel(content_frame, text="Lavendar Lemonade",font=(Hanuman,15), text_color="black")
        lavenderlemonadePicDescription.grid(row=4, column=1)
        
        lemonadePic_button = customtkinter.CTkButton(content_frame, image=lemonadePic, text="", width=100, height=80)
        lemonadePic_button.grid(row=3, column=2)
        lemonadePicDescription = customtkinter.CTkLabel(content_frame, text="Lemonade",font=(Hanuman,15), text_color="black")
        lemonadePicDescription.grid(row=4, column=2)
        
        meditteranPic_button = customtkinter.CTkButton(content_frame, image=meditteranPic, text="", width=100, height=80)
        meditteranPic_button.grid(row=1, column=4)
        meditteranPicDescription = customtkinter.CTkLabel(content_frame, text="Meditteran Dish",font=(Hanuman,15), text_color="black")
        meditteranPicDescription.grid(row=2, column=4)
        
        peppermintMochaPic_button = customtkinter.CTkButton(content_frame, image=peppermintMochaPic, text="", width=100, height=80)
        peppermintMochaPic_button.grid(row=3, column=4)
        peppermintMochaPicDescription = customtkinter.CTkLabel(content_frame, text="Peppermint Mocha",font=(Hanuman,15), text_color="black")
        peppermintMochaPicDescription.grid(row=4, column=4)
        
        mocktailPic_button = customtkinter.CTkButton(content_frame, image=mocktailPic, text="", width=100, height=80)
        mocktailPic_button.grid(row=3, column=5)
        mocktailPicDescription = customtkinter.CTkLabel(content_frame, text="Mocktail",font=(Hanuman,15), text_color="black")
        mocktailPicDescription.grid(row=4, column=5)
       
        waterPic_button = customtkinter.CTkButton(content_frame, image=waterPic, text="", width=100, height=80)
        waterPic_button.grid(row=3, column=6)
        waterPicDescription = customtkinter.CTkLabel(content_frame, text="Water",font=(Hanuman,15), text_color="black")
        waterPicDescription.grid(row=4, column=6)

        for i in range(5):
            content_frame.grid_rowconfigure(i, weight=1)
        for i in range(7):
            content_frame.grid_columnconfigure(i, weight=1)


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
    


    logo = customtkinter.CTkLabel(left_frame, text="", image=RMS_Logo_image, width=100, height=100)
    homeButton = customtkinter.CTkButton(left_frame, text="Home", width=200, height=100,command= homeButton_click)
    MenuButton = customtkinter.CTkButton(left_frame, text="Menu", width=200, height=100,command=menuButton_clicked)
    startOrderButton = customtkinter.CTkButton(left_frame, text="Start Order", width=200, height=100,command=startOrder_clicked)
    viewOrdersButton = customtkinter.CTkButton(left_frame, text="View Active Orders", width=200, height=100)
    tableManagementButton = customtkinter.CTkButton(left_frame, text="Table Management", width=200, height=100)
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




#Stop
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
