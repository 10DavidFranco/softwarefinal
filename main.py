from tkinter import *
from softwarefinal.admin import *
from softwarefinal.user import *
root = Tk()
root.title('Task Assignment App')
admin = False
###### THIS FILE IS FOR THE MAIN PAGE/HANDLING OF THE DIFFERENT VIEWS (USER/ADMIN)




#TASK: ASSIGN BUTTONS TO CHOOSE BETWEEN USER OR ADMIN MODE

#EVENTUALLY: IMPLEMEMNT LOGIN FUNCTIONALITY
#EVEnTUALLY: REFER TO DATABASE TO FIND ADMIN STATUS UPON LOGIN


##### CONTENT ###### (lines 7 - 49)
title_label = Label(root, text="TASK MANAGING APP", font=(32))

##### GRIDDING #####
title_label.grid(row=0, column=0)

##### FUNCTIONS #####
if(admin):
    print_admin_view()
else:
    print_user_view()

root.mainloop()