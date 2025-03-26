from tkinter import *

# Creating the main window widget
root = Tk()
root.title("Desktop project")
root.geometry("600x400")
root.configure(bg="#2E2E2E")  # Dark mode 

# Adding a centered title label
title_label = Label(root, text="Welcome to ( were working on a title :)", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

# Method to handle dropdown selection
def on_select(event):
    selected1 = drop_var1.get()
    selected2 = drop_var2.get()
    selected3 = drop_var3.get()
    label3 = Label(root, text=f"Selections: {selected1}, {selected2}, {selected3}", font=("Arial", 12))
    label3.grid(row=6, column=0, columnspan=2)
    print("Selected options:", selected1, selected2, selected3)

# Labels
label1 = Label(root, text="Select option 1:", font=("Arial", 12))
label1.grid(row=1, column=0)

label2 = Label(root, text="Select option 2:", font=("Arial", 12))
label2.grid(row=2, column=0)

label3 = Label(root, text="Select option 3:", font=("Arial", 12))
label3.grid(row=3, column=0)

# Drop Menu Setup
drop_var1 = StringVar()
drop_var1.set("Choose an option")
drop_menu1 = OptionMenu(root, drop_var1, "Option 1", "Option 2", "Option 3", "Option 4", command=on_select)
drop_menu1.grid(row=1, column=1)

drop_var2 = StringVar()
drop_var2.set("Choose an option")
drop_menu2 = OptionMenu(root, drop_var2, "Option 1", "Option 2", "Option 3", "Option 4", command=on_select)
drop_menu2.grid(row=2, column=1)

drop_var3 = StringVar()
drop_var3.set("Choose an option")
drop_menu3 = OptionMenu(root, drop_var3, "Option 1", "Option 2", "Option 3", "Option 4", command=on_select)
drop_menu3.grid(row=3, column=1)

# Call the main loop for displaying the root window
root.mainloop()
