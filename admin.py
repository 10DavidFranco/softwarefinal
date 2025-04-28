from tkinter import *
from task_assign import *
import sqlite3
#label = Label(root, text = "AdminView", font=(32))
dataConnector = sqlite3.connect('employeeData.db')

cursor = dataConnector.cursor() 
#TASK: MAKE THE PAGE LOOK NICE
#TASK: CREATE FORMAT FOR DISPLAYING X TASKS
#TASK: CREATE DROP DOWN MENU TO CHANGE STATUS OF TASK

#EMPLOYEE OBJECTS SHOULD BE CREATED
    #ITERABLE TASK ATTRIBUTE ARRAY
    #UNIQUE ID SO THEY CAN BE ACCESSIBLE
    #NAME PROPERTY

#ADMIN CAN FIND EMPLOYEE IN DATABASE 

def editSubmit(new_description, new_due_date, task_id):
    print("hi")
    print(task_id)

    cursor.execute("UPDATE task SET (description, due_date) = (?,?) WHERE task_id = ?",(
        new_description.get(),
        new_due_date.get(),
        task_id
    )
    )

    dataConnector.commit()


    new_description.delete(0,END)
    new_due_date.delete(0,END)

def deleteTask(task_id, employee_id):
    # We need to pass in the taskID and the employee ID
    print("deleting")
    print(task_id)
    print(employee_id)
    #Get task string
    cursor.execute("SELECT tasks FROM employee WHERE id = ?", [employee_id])
    task_fetch = cursor.fetchone()
    print(task_fetch)
    print(type(task_fetch))

    task_string = task_fetch[0]

    #Make into array
    task_list = task_string.split(",")
    print(task_list)
    print(type(task_list))

    if task_list[0] == "" and len(task_list) > 1:
        task_list = task_list[1:]

    new_tasks = []
    #Filter array and leave out the task to be deleted using its id
    for task in task_list:
        print(task)
        print(type(task))
        task_check = int(task)
        print(type(task_id))
        if(task_check != task_id):
            new_tasks.append(task)

    print(new_tasks)
    #make array into a string
    task_entry = ""
    for task in new_tasks:
        task_entry += str(task)
        task_entry += ","

    task_entry= task_entry[:-1]
    print(task_entry)
    print(type(task_entry))
    #Update the task of the employee with the new string of tasks
    cursor.execute("UPDATE employee SET tasks = ? WHERE id = ?",[task_entry, employee_id])
    dataConnector.commit()

def editTask(task_id):
    print("Editing!!!")
    edit = Tk()
    edit.title("TaskTrek - Edit View")  # Set window title
    edit.geometry("300x200")  # Set fixed window size
    edit.config(bg="orange")  # Set background color

    edit_title = Label(edit, text="Editing Task...",font=("fixedsys", 32), bg = "orange")
    edit_label = Label(edit, text="Please enter a description for the task", bg="orange")
    new_description = Entry(edit, width=30)
    date_edit_label = Label(edit, text="Please enter a due date for the task", bg="orange")
    date_new_description = Entry(edit, width=30)
    submit_button = Button(edit, text="Submit", command = lambda: editSubmit(new_description, date_new_description, task_id))

    edit_title.grid(row=0, column = 0)
    edit_label.grid(row=1, column = 0)
    new_description.grid(row=2, column = 0)
    date_edit_label.grid(row=3, column = 0)
    date_new_description.grid(row=4, column = 0)
    submit_button.grid(row = 5, column = 0)

def viewTasks(employee):
    view = Tk()
    view.title("TaskTrek - Admin View")  # Set window title
    view.geometry("500x300")  # Set fixed window size
    # Centering the window
    screen_width = view.winfo_screenwidth()
    screen_height = view.winfo_screenheight()
    window_width = 600
    window_height = 300
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    view.geometry(f"{window_width}x{window_height}+{x}+{y}")
    view.config(bg="orange")  # Set background color
    #print(employee)
    user_tasks = []
    task_keys = employee[3]
    tasks = []
    #print(task_array)
    print("Employee at 3")
    print(employee[3])
    print(type(employee[3]))
    if(employee[3] != None):
        tasks = task_keys.split(",")
    else:
        tasks = []
    print(tasks)
    #print(tasks[0])

    #IF the first index is blank AND length is greater than 1, reduce array to >0 indeices

    if(len(tasks) > 0):
        if tasks[0] == "" and len(tasks) > 1:
            tasks = tasks[1:]
        print(tasks)
        for a_task in tasks:
            sql = "SELECT * FROM task WHERE task_id = ?"
            if(a_task == ""):
                break
            else:
                my_id = int(a_task)
                cursor.execute(sql, [my_id])
                my_task = cursor.fetchone()
                user_tasks.append(my_task)

        row_count = 0

        for task in user_tasks:
            print("Printing!!!")
            print(task[0])
            print(employee[0])
            task_label = Label(view, text=task[1], font=("fixedsys", 20), bg = "orange")
            delete = Button(view, text="Delete Task", command = lambda task=task: deleteTask(task[0], employee[0]))
            edit = Button(view, text="Edit Task", command = lambda task=task: editTask(task[0]))
            task_label.grid(row = 4 + row_count, column = 1)
            delete.grid(row = 4 + row_count, column = 2)
            edit.grid(row = 4 + row_count, column= 3)
            
            #createDropDown(task[2], user, row_count, task[0])
            #dropdown.config(font=("fixedsys", 10))
            #dropdown.grid(row=4 + row_count, column=2)

            row_count += 1
    else:
        print("lucky you, nothing to do")



def print_admin_view():
    #ROOT ADMIN NODE
    admin = Tk()

    admin.title("TaskTrek - Admin View")  # Set window title
    admin.geometry("1000x600")  # Set fixed window size
    # Centering the window
    screen_width = admin.winfo_screenwidth()
    screen_height = admin.winfo_screenheight()
    window_width = 1000
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    admin.geometry(f"{window_width}x{window_height}+{x}+{y}")
    admin.config(bg="orange")  # Set background color
    
    

    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    employee_array = cursor.fetchall()
    #print(employees)
    #LABELLING
    # Configure columns to expand (important for centering)
    admin.grid_columnconfigure(0, weight=1)
    admin.grid_columnconfigure(1, weight=1)
    admin.grid_columnconfigure(2, weight=1)
    admin.grid_columnconfigure(3, weight=1)
    admin.grid_columnconfigure(4, weight=1)

    # Centered label
    admin_label = Label(admin, text="WELCOME ADMIN", font=("fixedsys", 32), bg="orange")
    admin_label.grid(row=0, column=0, columnspan=5, pady=20, sticky="nsew")
        
    #ASSIGN TASK BUTTON
    assignButton = Button(admin, text="Assign New Task", command=assignTask)
    assignButton.grid(row=1, column=2, pady=10, sticky="n")
   #CREATE NEW TASK WIDGET
    
    
    row_count = 0
    for employee in employee_array:
        print(employee[1])
        #print(employee_array[employee])
        employee_label = Label(admin, text=employee[1], font=("fixedsys", 20), bg = "orange")
        employee_label.grid(row=4 + row_count, column=2, sticky="w")

        viewAssignButton = Button(admin, text = "View Existing Tasks", command= lambda employee=employee: viewTasks( employee))
        viewAssignButton.grid(row=4 + row_count, column=3, padx=10, sticky="w")
    
        # deleteAssignButton = Button(admin, text = "Delete Task", command = deleteTask)
        # deleteAssignButton.grid(row = row_count+4, column = 6)

        row_count += 1