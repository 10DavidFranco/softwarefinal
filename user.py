from tkinter import *
import sqlite3

# Connect to the database
dataConnector = sqlite3.connect('employeeData.db')
cursor = dataConnector.cursor()

def onSelect(arg, id):
    sql = "UPDATE task SET status = ? WHERE task_id = ?"
    my_status = arg
    my_task_id = id
    cursor.execute(sql, [my_status, my_task_id])
    dataConnector.commit()

def createDropDown(current_status, parent_frame, row_num, task_id, task_frame):
    status_var = StringVar()
    status_var.set(current_status)

    def on_status_change(new_status):
        onSelect(new_status, task_id)
        task_frame.config(bg="green" if new_status == "Complete" else "red")

    dropdown = OptionMenu(parent_frame, status_var, "Incomplete", "Complete", command=on_status_change)
    dropdown.pack(side=RIGHT, padx=10)

# FUNCTION TO DISPLAY THE USER VIEW
def print_user_view(employee):
    
    print("Hello user")

    # Create a new window for the user view
    user = Tk()
    user.title("TaskTrek - User View")  # Set window title
    user.geometry("1000x600")  # Set fixed window size
    # Centering the window
    screen_width = user.winfo_screenwidth()
    screen_height = user.winfo_screenheight()
    window_width = 1000
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    user.geometry(f"{window_width}x{window_height}+{x}+{y}")

    user.config(bg="orange")  # Set background color
    user_tasks = []
    task_keys = employee[3]  # Assuming employee[3] is a string of task IDs (comma-separated)
    tasks = task_keys.split(",")
    print(tasks)

    # Fetch task details for each task ID
    for a_task in tasks:
        sql = "SELECT * FROM task WHERE task_id = ?"
        my_id = int(a_task)
        cursor.execute(sql, [my_id])
        my_task = cursor.fetchone()
        user_tasks.append(my_task)

    row_count = 0
    
    # Display the list of tasks dynamically
    for task in user_tasks:
        task_frame = Frame(user, bg="green" if task[2] == "Complete" else "red", padx=10, pady=10, bd=2, relief="groove")
        task_frame.grid(row=4 + row_count, column=1, pady=5, sticky="")

        # Task label inside the frame
        task_label = Label(task_frame, text=task[1] + " | Due: " + task[3], font=("fixedsys", 16), bg="white", anchor="w", width=40)
        task_label.pack(side=LEFT, fill=BOTH, expand=True)

        # Create dropdown for task status change
        createDropDown(task[2], task_frame, row_count, task[0], task_frame)

        row_count += 1

    ########################################## PAGE TITLE ##########################################
    # Configure grid columns to expand evenly
    user.grid_columnconfigure(0, weight=1)
    user.grid_columnconfigure(1, weight=1)
    user.grid_columnconfigure(2, weight=1)

    # Fetch the employee's name from the database (assuming employee[0] is employee_id)
    employee_id = employee[0]  # employee[0] should be the ID
    cursor.execute("SELECT name FROM employee WHERE id = ?", (employee_id,))
    employee_name = cursor.fetchone()[0]  # Fetch employee name

    # Centered label with employee's name in the title
    user_label = Label(user, text=f"TaskTrek - Welcome, {employee_name}!", font=("fixedsys", 32), bg="orange")
    user_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")
