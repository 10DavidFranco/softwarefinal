from tkinter import *
from tkinter.font import Font #import fonts 
from admin import *
from user import *
import sqlite3
import tkinter as tk
root = Tk()
root.title('TaskTrek-Task Assignment App') #Title above the page

dataConnector = sqlite3.connect('employeeData.db')

cursor = dataConnector.cursor()

#THIS FILE IS FOR THE MAIN PAGE/HANDLING OF THE DIFFERENT VIEWS (USER/ADMIN)
#TASK: ASSIGN BUTTONS TO CHOOSE BETWEEN USER OR ADMIN MODE
#EVENTUALLY: IMPLEMEMNT LOGIN FUNCTIONALITY
#EVEnTUALLY: REFER TO DATABASE TO FIND ADMIN STATUS UPON LOGIN


##################(This is for setting up the window to open in the center of a users window)####################
#Setting a fixed size of the window (width x height)
#kind of a paranamic mode
width = 900
height = 700
# Getting the screen computers width and height (this would be the users own computer dimensions)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
# Set the geometry of the window to be centered
# width x height will be the size of the window when it opens (area of a rectangle is base x height) 
#x and y will be where the window opens up so in this case the center of the users screen
root.geometry(f"{width}x{height}+{x}+{y}")


# Change background color of the root window
root.config(bg="orange")  # Set the background color
##################################################################################################################


############################################################ Methods ###################################
# Function for User button click
def on_click():
    print("User Has been selected")
    # Display user view
    print_user_view()  
    
    # You can add more logic here if necessary (e.g., fetch data)


# Function for Admin button click
def on_clicky():
    print("Admin Has been selected")
    # Display admin view
    print_admin_view() 
    


def on_submit():
    text = item.get()
    print(text)
    
    sql = "SELECT * FROM employee WHERE id = ?"
    my_id = int(text)
    cursor.execute(sql, [my_id])

    my_employee = cursor.fetchone()


  

    if(my_employee):
        print("hi")
        
    else:
        item.delete(0, tk.END)
        item.insert(0, "invalid ID")
        return -1



    print(my_employee[2])
    is_admin = my_employee[2]
    #Extract admin value
    print(type(my_employee))

    if(is_admin):
        print_admin_view()
        #else if user, print user view
    else:
        print("ENTERING USER VIEW")
        print(my_employee)
        print_user_view(my_employee)
        #Find employee id
    
    #pass in ID as parameter for user view so tasks can be generated
########################################################################################################



############################################################ Widgets (Buttons) ###################################
#we pass it in on root because thats the parent container the window in this instance and thats where it relies in
Userbutton = Button(root, text="View Tasks",font=("fixedsys", 10),width=20, height=2, bg="#D3D3D3", fg="black", command=on_click)

Adminbutton = Button(root, text="Admin Login",font=("fixedsys", 10),width=20, height=2, bg="#D3D3D3", fg="black", command=on_clicky)
########################################################################################################
item = Entry(root)
#item.pack()
Submitbutton = Button(root, text="Submit", command=on_submit)
item.insert(0,"Enter your employeeID")




######################## FONTS/TEXT CONTENT ################
bigFont = Font(
    family="fixedsys",
    size=90,
    weight="bold",
    slant="italic"
    # underline=0,
    # overstrike=0
)
# Create the title label
#the label has its own bg as it
title_label = Label(root, text="TaskTrek", font=bigFont, bg="orange")
###################################################################



###################################################### GRIDDING/FRAMEING ########################################
# Grid config to allow stretching
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
# Title label setup
title_label = Label(root, text="TaskTrek", font=bigFont, bg="orange")
# Span both columns and center
title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")


input_frame = Frame(root, bg="orange")
input_frame.grid(row=1, column=0, columnspan=2, pady=20)
# Center it
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
item = Entry(input_frame)
item.insert(0, "Enter your employeeID")
item.pack(side="left", padx=5)
Submitbutton = Button(input_frame, text="Submit", command=on_submit)
Submitbutton.pack(side="left", padx=5)

############################################################################################################

root.mainloop()