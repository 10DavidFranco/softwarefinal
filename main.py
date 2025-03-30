from tkinter import *
from tkinter.font import Font #import fonts 
from admin import *
from user import *
root = Tk()
root.title('TaskTrek-Task Assignment App') #Title above the page


#THIS FILE IS FOR THE MAIN PAGE/HANDLING OF THE DIFFERENT VIEWS (USER/ADMIN)
#TASK: ASSIGN BUTTONS TO CHOOSE BETWEEN USER OR ADMIN MODE
#EVENTUALLY: IMPLEMEMNT LOGIN FUNCTIONALITY
#EVEnTUALLY: REFER TO DATABASE TO FIND ADMIN STATUS UPON LOGIN




##################(This is for setting up the window to open in the center of a users window)####################
#Setting a fixed size of the window (width x height)
#kind of a paranamic mode
width = 1200
height = 650
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
root.config(bg="orange")  # Set the background color to light gray
##################################################################################################################



#admin = False





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

########################################################################################################




############################################################ Widgets (Buttons) ###################################
#we pass it in on root because thats the parent container the window in this instance and thats where it relies in
Userbutton = Button(root, text="View Tasks",font=("fixedsys", 10),width=20, height=2, bg="#D3D3D3", fg="black", command=on_click)

Adminbutton = Button(root, text="Admin Login",font=("fixedsys", 10),width=20, height=2, bg="#D3D3D3", fg="black", command=on_clicky)
########################################################################################################





######################## Define FONTS ################
bigFont = Font(
    family="fixedsys",
    size=90,
    weight="bold",
    slant="italic"
    # underline=0,
    # overstrike=0

)
######################################################


################################################ TEXT CONTENT ##########################################
# Create the title label
#the label has its own bg as it
title_label = Label(root, text="TaskTrek", font=bigFont, bg="orange")
########################################################################################################



###################################################### GRIDDING ########################################
# Grid the title label at row 0, column 0
# 'nsew' means North, South, East, West (stretches)
title_label.grid(row=0, column=0, sticky="nsew")
# Make the row at index 0 expand vertically, keeping it at the top
root.grid_rowconfigure(0, weight=0)  # row 0 does not expand vertically
root.grid_rowconfigure(1, weight=1)  # row 1 can expand vertically if needed
# Make the columns expand horizontally to center the label
root.grid_columnconfigure(0, weight=1)  # column 0 expands horizontally




Userbutton.grid(row=1,column=0)
#item.grid(row=2,column=0)
Adminbutton.grid(row=4, column=1)
############################################################################################################



################################################### FUNCTIONS ################################################

###############################################################################################################



root.mainloop()