# from tkinter import *
# import sqlite3
# dataConnector = sqlite3.connect('employeeData.db')

# cursor = dataConnector.cursor() 

# def on_date():
#     print("date added")

# def on_description():
#     print("description added")

# def on_employee():
#     print("employees added")

# def assignTask():
#     # We need to create a new task and pass the id into the functions...
#     #Create the new task
#     #And then... in functions, once the submit button is clicked for each field, find the task and set the information
#     print("Hello!")
#     assign = Tk()
#     assign.title("TaskTrek - Task Assignment View")  # Set window title
#     assign.geometry("400x300")  # Set fixed window size
#     assign.config(bg="orange")  # Set background color
#     #Labels
#     title = Label(assign, text= "ASSIGNMENT WINDOW", font = ("fixedsys", 32), bg = "orange")
#     task_due_date = Label(assign, text = "Due Date:", font=("fixedsys", 20), bg="orange")
#     task_due_date_button = Button(assign, text="Submit", command= on_date)
#     task_description = Label(assign, text = "Brief Description:", font=("fixedsys", 20), bg="orange")
#     task_description_button = Button(assign, text= "Submit", command= on_description)
#     task_employees = Label(assign, text = "Employees:", font=("fixedsys", 20), bg="orange")
#     task_employees_button = Button(assign, text="Submit", command= on_employee)

#     #Entry fields
#     task_name_entry = Entry(assign)

#     task_due_date_entry = Entry(assign)

#     task_description_entry = Entry(assign)

    
#     #Gridding
#     title.grid(row = 0, column = 0)

    

#     task_due_date.grid(row = 1, column = 0)
#     task_due_date_entry.grid(row = 2, column = 0)
#     task_due_date_button.grid(row = 3, column = 0)
#     task_description.grid(row = 4, column = 0)
#     task_description_button.grid(row = 5, column = 0)
#     task_description_entry.grid(row = 6, column = 0)

#     task_employees.grid(row = 7, column = 0)
#     task_employees_button.grid(row = 8, column = 0)
#     #See if radio buttons allow multiple select
from tkinter import *
import sqlite3

dataConnector = sqlite3.connect('employeeData.db')

cursor = dataConnector.cursor() 

def mysubmit(description, due_date, employees):
    ####To get the accurate id####
    sql = "SELECT * FROM task"
    cursor.execute(sql)
    current_tasks = []
    #my_tasks = cursor.fetchall()
    #print("EMPLOYEEESSS")
    #print(my_tasks)
    #print(len(my_tasks))

    #correct_id = len(my_tasks) + 1

    cursor.execute("INSERT INTO task (description, status, due_date) VALUES (?,?,?)",(
        description.get(),
        "Incomplete",
        due_date.get(),
    )
    )



    #my_new_task = cursor.fetchone()
    #print(my_new_task)

    dataConnector.commit()



    
    #Still need to get the task ID and append to tasks field of employees
    assigned_employees = employees.get()
    print("HAHAHAHA")
    print(assigned_employees)
    #cursor.execute("SELECT * FROM employee WHERE id = ?", {})
    my_employees = assigned_employees.split(",")
    print(my_employees)
    #Set tasks to include new assignment
    task_id = cursor.lastrowid
    print(task_id)

    for worker in my_employees:
        print(worker)
        cursor.execute("SELECT tasks FROM employee WHERE id = ?", [worker])
        current_tasks_check = list(cursor.fetchone())
        if current_tasks_check != None:
            current_tasks = current_tasks_check
        else:
            current_tasks = []
        print(current_tasks)
        print(type(current_tasks))
        print(len(current_tasks))
        current_tasks.append(str(task_id))
        #It's the task ID we need to adfd!!!!!!!
        print("////////////////")
        print(current_tasks)
        print(type(current_tasks))
        print(len(current_tasks))
        # for task in current_tasks:
        #     print("PRINTING")
        #     print(task)
        #     print(type(task))
        #     #and then turn each index to strings
        if current_tasks[0] != None:
            current_tasks_text = ",".join(current_tasks)
        else:
            print("Got you...")
            current_tasks_text = str(task_id)
        #I need to get the task ID, and append it to the list in the employee tasks field.
        #Look into payloads, 
        cursor.execute("UPDATE employee SET tasks = ? WHERE id = ?", [current_tasks_text, worker])
        dataConnector.commit()
    
    
    
    
    
    
    description.delete(0,END)
    due_date.delete(0,END)
    employees.delete(0,END)
    # Save and close connection to database
    


def assignTask():
    assign = Tk()
    assign.title("TaskTrek - Task Assignment View")  # Set window title
    assign.geometry("400x300")  # Set fixed window size
    assign.config(bg="orange")  # Set background color
    ##### Create widgets
    description = Entry(assign, width = 30)
    due_date = Entry(assign, width = 30)
    employees = Entry(assign, width = 30)
    

    description_label = Label(assign, text = "Description", bg="orange")
    due_date_label = Label(assign, text = "Due Date", bg="orange")
    employees_label= Label(assign, text = "Employees", bg="orange")
    

    submit = Button(assign, text="Add Task", command =lambda: mysubmit(description, due_date, employees))
    delete = Button(assign, text="Delete Task")


    ##### Call widgets
    description.grid(row = 0, column = 1)
    due_date.grid(row = 1, column = 1)
    employees.grid(row = 2, column = 1)
   

    description_label.grid(row = 0, column = 0)
    due_date_label.grid(row = 1, column = 0)
    employees_label.grid(row = 2, column = 0)
   

    submit.grid(row = 4, column = 0)
  
    