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
    # Centering the window
    screen_width = assign.winfo_screenwidth()
    screen_height = assign.winfo_screenheight()
    window_width = 400
    window_height = 300
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    assign.geometry(f"{window_width}x{window_height}+{x}+{y}")
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
  
    