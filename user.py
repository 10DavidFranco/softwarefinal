from tkinter import *

# List to keep track of tasks (temporary, not saved to file or DB)
user_tasks = []

# FUNCTION TO DISPLAY THE USER VIEW
def print_user_view():
    print("Hello user")

    # Create a new window for the user view
    user = Tk()
    user.title("TaskTrek - User View")  # Set window title
    user.geometry("800x600")  # Set fixed window size
    user.config(bg="orange")  # Set background color

    ########################################## PAGE TITLE ##########################################
    # Label at the top of the page to indicate we're in User View
    user_label = Label(user, text="TaskTrek - User View", font=("fixedsys", 32), bg="orange")
    user_label.grid(row=0, column=0, columnspan=3, pady=20)
    ###############################################################################################


    ########################################## TASK ENTRY SECTION ##################################
    # Label to indicate where to type a new task
    task_label = Label(user, text="Enter New Task:", font=("fixedsys", 14), bg="orange")
    task_label.grid(row=1, column=0, sticky="e", padx=10)

    # Entry box for user to type in the task
    task_entry = Entry(user, font=("fixedsys", 14), width=30)
    task_entry.grid(row=1, column=1, padx=10)

    # Button to add the task (calls add_task when clicked)
    add_button = Button(user, text="Add Task", font=("fixedsys", 12), command=lambda: add_task(), bg="#D3D3D3")
    add_button.grid(row=1, column=2, padx=10)
    ###############################################################################################


    ########################################## TASK LIST FRAME #####################################
    # Frame to hold and display the list of tasks dynamically
    task_list_frame = Frame(user, bg="orange")
    task_list_frame.grid(row=3, column=0, columnspan=3, pady=20)
    ###############################################################################################


    ########################################## FUNCTION TO ADD TASK ###############################
    def add_task():
        # Get task text from the entry box
        task_text = task_entry.get().strip()

        # Only add task if input is not empty
        if task_text:
            # Create a StringVar to track the status of this task
            status_var = StringVar()
            status_var.set("Incomplete")  # Default status

            # Label to display the task text
            task_display = Label(task_list_frame, text=task_text, font=("fixedsys", 12), bg="orange")
            task_display.grid(row=len(user_tasks), column=0, padx=5, pady=5, sticky="w")

            # Dropdown menu to change task status
            dropdown = OptionMenu(task_list_frame, status_var, "Incomplete", "Complete")
            dropdown.config(font=("fixedsys", 10))
            dropdown.grid(row=len(user_tasks), column=1, padx=10, pady=5)

            # Store task and status in list for reference
            user_tasks.append((task_text, status_var))

            # Clear the entry box after task is added
            task_entry.delete(0, END)
    ###############################################################################################
