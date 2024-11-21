from tkinter import *
from tkinter import Menu

def show_option(event, menu):
    x = event.x_root
    y = event.y_root
    menu.post(x, y)

def read_notif():
    print("Read notification")
    
def reply_notif():
    print("Reply to notification")
    
def delete_notif():
    print("Delete notification")

root = Tk()
root.title("Manager Home Screen - View Notifications")
root.geometry("1200x800")

content = Frame(root, bg="light blue")
content.pack(expand=True, fill="both", padx=15, pady=15)

font_time = ("Times New Roman", 14)
font_message = ("Times New Roman", 16)
font_title = ("Times New Roman", 20)
font_button = ("Times New Roman", 14)

# Grid Layout
    # You missed this part originally
content.grid_rowconfigure(0, weight = 1)
content.grid_rowconfigure(1, weight = 1)
content.grid_columnconfigure(0, weight = 1)

# create the first notification frame
notif_frame = Frame(content, bg="white", width=1000, height=200, bd=2, relief="solid")
# notif_frame.pack_propagate(False)
notif_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

notif_time = Label(notif_frame, text="5 days ago", anchor="ne", bg="white", fg="black", font=font_time)
notif_time.grid(row=0, column=0, sticky="e")

notif_title = Label(notif_frame, text="New Schedule Update", anchor="nw", bg="white", fg="black", font=font_title)
notif_title.grid(row=0, column=1, sticky="w")

notif_message = Label(
    notif_frame, 
    text="Employee Azra Ferris has requested time off on Nov. 16-20. Please review and approve or deny.", 
    wraplength=200, bg="white", fg="black", font=font_message
)
notif_message.grid(row=1, column=0, columnspan=2, sticky="nsew")

option_button = Button(notif_frame, text=":", bg="white", font=font_button)
option_button.grid(row=2, column=0, pady=10, sticky="w")

menu = Menu(root, tearoff=0)
menu.add_command(label="Read", command=read_notif)
menu.add_command(label="Reply", command=reply_notif)
menu.add_command(label="Delete", command=delete_notif)

option_button.bind("<Button-1>", lambda event: show_option(event, menu))

# create the second notification frame
notif_frame1 = Frame(content, bg="white", width=100, height=200, bd=2, relief="solid")
# notif_frame1.pack_propagate(False)
notif_frame1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

notif_time1 = Label(notif_frame1, text="11:52 AM", anchor="ne", bg="white", fg="black", font=font_time)
notif_time1.grid(row=0, column=0, sticky="e")

notif_title1 = Label(notif_frame1, text="Shift Swap", anchor="nw", bg="white", fg="black", font=font_title)
notif_title1.grid(row=0, column=1, sticky="w")

notif_message1 = Label(
    notif_frame1, 
    text="Employee Navy Arbor has a shift scheduled for tomorrow at 4. Please send a reminder to ensure they’re aware of their start time.", 
    wraplength=400, bg="white", fg="black", font=font_message)

notif_message1.grid(row=1, column=0, columnspan=2, sticky="nsew")

option_button1 = Button(notif_frame, text=":", bg="white", font=font_button)
option_button.grid(row=2, column=0, pady=10, sticky="w")

menu1 = Menu(root, tearoff=0)
menu1.add_command(label="Read", command=read_notif)
menu1.add_command(label="Reply", command=reply_notif)
menu1.add_command(label="Delete", command=delete_notif)

option_button1.bind("<Button-1>", lambda event: show_option(event, menu1))

root.mainloop()
