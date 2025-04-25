from tkinter import *
import sqlite3
# List to keep track of tasks (temporary, not saved to file or DB)


dataConnector = sqlite3.connect('employeeData.db')
    
cursor = dataConnector.cursor()


def onSelect(arg, id):
    sql = "UPDATE task SET status = ? WHERE task_id = ?"
    my_status = arg
    my_task_id = id

    cursor.execute(sql, [my_status, my_task_id])
    dataConnector.commit()
    #print(arg)

def createDropDown(arg1, arg2, arg3, task_id):
    status_var = StringVar()
    status_var.set(arg1) #needs task[2]
    # Dropdown menu to change task status
    print(status_var)
    print(status_var.get())
    dropdown = OptionMenu(arg2, status_var, "Incomplete", "Complete", command=lambda value: onSelect(value, task_id)) #needs user
    dropdown.grid(row = 4 + arg3, column = 2) #needs rowcount


# FUNCTION TO DISPLAY THE USER VIEW
def print_user_view(employee):
    
    print("Hello user")

    # Create a new window for the user view
    user = Tk()
    user.title("TaskTrek - User View")  # Set window title
    user.geometry("800x600")  # Set fixed window size
    user.config(bg="orange")  # Set background color
    user_tasks = []
    task_keys = employee[3]
    #print(task_array)
    tasks = task_keys.split(",")
    print(tasks)

    

    for a_task in tasks:
        sql = "SELECT * FROM task WHERE task_id = ?"
        my_id = int(a_task)
        cursor.execute(sql, [my_id])
        my_task = cursor.fetchone()
        user_tasks.append(my_task)



    row_count = 0
    
    ########################################## TASK LIST FRAME #####################################
    # Frame to hold and display the list of tasks dynamically
    #task_list_frame = Frame(user, bg="orange")
    #task_list_frame.grid(row=3, column=0, columnspan=3, pady=20)

    

    for task in user_tasks:
        print(task)
        #print(employee_array[employee])
        task_label = Label(user, text=task[1] + " " + task[3], font=("fixedsys", 20), bg = "orange")
        task_label.grid(row = 4 + row_count, column = 1)
        
        createDropDown(task[2], user, row_count, task[0])
        #dropdown.config(font=("fixedsys", 10))
        #dropdown.grid(row=4 + row_count, column=2)

        row_count += 1


    #dataConnector = sqlite3.connect('employeeData.db')

    #cursor = dataConnector.cursor() 

    #sql = "SELECT * FROM employee WHERE id = ?"
    #my_id = int(id)
    #cursor.execute(sql, [my_id])
    ########################################## PAGE TITLE ##########################################
    # Label at the top of the page to indicate we're in User View
    user_label = Label(user, text="TaskTrek - User View", font=("fixedsys", 32), bg="orange")
    user_label.grid(row=0, column=0, columnspan=3, pady=20)
    ###############################################################################################

    ########################################## TASK ENTRY SECTION ##################################

    ###############################################################################################



    ###############################################################################################


    ########################################## FUNCTION TO ADD TASK ###############################
    #def add_task():
        # Get task text from the entry box
        #task_text = task_entry.get().strip()

        # Only add task if input is not empty
        #if task_text:
            # Create a StringVar to track the status of this task
            #status_var = StringVar()
            #status_var.set("Incomplete")  # Default status

            # Label to display the task text
            #task_display = Label(task_list_frame, text=task_text, font=("fixedsys", 12), bg="orange")
            #task_display.grid(row=len(user_tasks), column=0, padx=5, pady=5, sticky="w")

          

            # Store task and status in list for reference
            #user_tasks.append((task_text, status_var))

            # Clear the entry box after task is added
            #task_entry.delete(0, END)
    ###############################################################################################
