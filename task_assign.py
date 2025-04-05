from tkinter import *

def assignTask():
    assign = Tk()
    assign.title("TaskTrek - Task Assignment View")  # Set window title
    assign.geometry("800x600")  # Set fixed window size
    assign.config(bg="orange")  # Set background color
    #Labels
    title = Label(assign, text= "ASSIGNMENT WINDOW", font = ("fixedsys", 32), bg = "orange")
    task_name = Label(assign, text = "Please give this task a name:", font=("fixedsys", 20), bg="orange")
    task_due_date = Label(assign, text = "Please enter the due date for this task:", font=("fixedsys", 20), bg="orange")
    task_description = Label(assign, text = "Please enter a brief description of the task:", font=("fixedsys", 20), bg="orange")
    task_employees = Label(assign, text = "Please select the employees to be assigned this task:", font=("fixedsys", 20), bg="orange")

    #Entry fields
    task_name_entry = Entry(assign)

    task_due_date_entry = Entry(assign)

    task_description_entry = Entry(assign)

    
    #Gridding
    title.grid(row = 0, column = 0)

    task_name.grid(row = 2, column = 0)
    task_name_entry.grid(row=3, column =0)

    task_due_date.grid(row = 4, column = 0)
    task_due_date_entry.grid(row = 5, column = 0)

    task_description.grid(row = 6, column = 0)
    task_description_entry.grid(row = 7, column = 0)

    task_employees.grid(row = 8, column = 0)
    #See if radio buttons allow multiple select
