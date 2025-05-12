# softwarefinal
Software Engineering Final Project
By: Hector Moreno, Maximiliano Trevino, Sabino Rodea, David Franco

The project we will be completing is a To-do list application.
The application will consist of a user mode and an admin mode.

User mode:
  -View the tasks assigned to them.
  -Change the completion status of tasks. (from in-progress to complete)

Admin mode:
  -Create and assign new tasks to employess.
  -Read/view the tasks assigned to a given employee.
  -Update the tasks assigned to a given employee.
  -Delete tasks assigned to a given employee.

Our app's functionality comes from SQL tables.

Admins will make their changes permanent by communicating with
an SQL database. Admins will be differentiated from regular users by a 1 in the admin
column.

Users, upon login, will have their tasks read from our database, and shown the
tasks with their corresponding userID. They can then interact with the 
user interface to alter the status of an assignment that is reflected on
both the users end and the admins.

Additionally,

Our application has a login page where users sign in with their unique employee ID.
This ID is then used to render the appropriate view/tasks for the user.
