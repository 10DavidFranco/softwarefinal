# database.py

# Simulated in-memory database of employees and their tasks

# Each employee has:
# - unique_id (int)
# - is_admin (bool)
# - name (str)
# - tasks (list of strings)

database = {
    1001: {
        "is_admin": True,
        "name": "Alice Johnson",
        "tasks": ["Update client report", "Review Q2 budget"]
    },
    1002: {
        "is_admin": False,
        "name": "Bob Martinez",
        "tasks": ["Fix login bug", "Write documentation"]
    },
    1003: {
        "is_admin": False,
        "name": "Clara Zhang",
        "tasks": ["Implement feature X", "Test new release"]
    },
    1004: {
        "is_admin": True,
        "name": "David Franco",
        "tasks": []
    },
    1005: {
        "is_admin": False,
        "name": "Ella Rivera",
        "tasks": ["Clean data logs"]
    }
}

# Utility functions

def get_employee(employee_id):
    return database.get(employee_id)

def get_all_employees():
    return database

def get_admins():
    return {eid: info for eid, info in database.items() if info["is_admin"]}

def assign_task(employee_id, task):
    if employee_id in database:
        database[employee_id]["tasks"].append(task)
        return True
    return False

def delete_task(employee_id, task):
    if employee_id in database and task in database[employee_id]["tasks"]:
        database[employee_id]["tasks"].remove(task)
        return True
    return False
