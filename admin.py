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

def editTask():
    print("Editing!!!")

def viewTasks(employee):
    view = Tk()
    view.title("TaskTrek - Admin View")  # Set window title
    view.geometry("500x300")  # Set fixed window size
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
            edit = Button(view, text="Edit Task")
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
    admin.geometry("800x600")  # Set fixed window size
    admin.config(bg="orange")  # Set background color
    
    

    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    employee_array = cursor.fetchall()
    #print(employees)
    #LABELLING
    admin_label = Label(admin, text = "WELCOME ADMIN", font=("fixedsys", 32), bg = "orange")
    
    #ASSIGN TASK BUTTON
    assignButton = Button(admin, text = "Assign New Task", command = assignTask)
    assignButton.grid(row = 2, column = 0)
    #CREATE NEW TASK WIDGET

    #POSITIONING
    admin_label.grid(row = 0, column = 0)
    
    
    row_count = 0
    for employee in employee_array:
        print(employee[1])
        #print(employee_array[employee])
        employee_label = Label(admin, text=employee[1], font=("fixedsys", 20), bg = "orange")
        employee_label.grid(row = 4 + row_count, column = 2)

        viewAssignButton = Button(admin, text = "View Existing Tasks", command= lambda employee=employee: viewTasks( employee))
        viewAssignButton.grid(row = row_count+4, column = 4)
    
        # deleteAssignButton = Button(admin, text = "Delete Task", command = deleteTask)
        # deleteAssignButton.grid(row = row_count+4, column = 6)

        row_count += 1