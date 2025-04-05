from tkinter import *
from task_assign import *
#label = Label(root, text = "AdminView", font=(32))

#TASK: MAKE THE PAGE LOOK NICE
#TASK: CREATE FORMAT FOR DISPLAYING X TASKS
#TASK: CREATE DROP DOWN MENU TO CHANGE STATUS OF TASK

#EMPLOYEE OBJECTS SHOULD BE CREATED
    #ITERABLE TASK ATTRIBUTE ARRAY
    #UNIQUE ID SO THEY CAN BE ACCESSIBLE
    #NAME PROPERTY

#ADMIN CAN FIND EMPLOYEE IN DATABASE 

def viewTasks():
    print("Hello!")

def deleteTask():
    print("Buenos dias!")

def print_admin_view():
    #ROOT ADMIN NODE
    admin = Tk()

    admin.title("TaskTrek - Admin View")  # Set window title
    admin.geometry("800x600")  # Set fixed window size
    admin.config(bg="orange")  # Set background color
    
    #LABELLING
    admin_label = Label(admin, text = "WELCOME ADMIN", font=("fixedsys", 32), bg = "orange")
    
    #ASSIGN TASK BUTTON
    assignButton = Button(admin, text = "Assign New Task", command = assignTask)
    assignButton.grid(row = 2, column = 0)
        #CREATE NEW TASK WIDGET

    #POSITIONING
    admin_label.grid(row = 0, column = 0)
    
    employee_array= [0,1,2,3,4,5]

    for employee in employee_array:

        employee_label = Label(admin, text="Employee Name", font=("fixedsys", 20), bg = "orange")
        employee_label.grid(row = employee + 4, column = 2)

        viewAssignButton = Button(admin, text = "View Existing Tasks", command=viewTasks)
        viewAssignButton.grid(row = employee+4, column = 4)
    
        deleteAssignButton = Button(admin, text = "Delete Task", command = deleteTask)
        deleteAssignButton.grid(row = employee+4, column = 6)