# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
def writing():
    with open("tasks.txt", "w") as task_file:
            for t in task_list:
                task_list_to_write = []
                str_attrs = [ 
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                    ]
                task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
                task_file.write("\n")
            print("Task successfully updated.")

def taskoverview1():
    with open("task_overview.txt","w") as task_overview: #opens file in writing mode
            total_tasks = len(task_list)
            uncompleted_tasks = 0
            completed_tasks = 0
            overdue_tasks = 0
            curr_date = date.today()
            num_tasks = len(task_list)

            for t in task_list:
                date_due = str(t['due_date']).split()
                if not t['completed'] and date_due[0] <= str(curr_date): #checking if tasks are overdue
                    overdue_tasks +=1

                if t['completed']:
                    completed_tasks +=1
                else:
                    uncompleted_tasks +=1
            
            task_overview.write(f"{num_tasks} total tasks \n")
            task_overview.write(f"{overdue_tasks} total tasks overdue \n")
            task_overview.write(f"{uncompleted_tasks} total tasks uncompleted \n")
            task_overview.write(f"{completed_tasks} total tasks Completed \n")
                
            if len(task_list) > 0:
                task_overview.write(f"{(uncompleted_tasks/total_tasks)*100} percent tasks uncompleted \n")
                task_overview.write(f"{(overdue_tasks/total_tasks)*100} percent tasks overdue")

def useroverview1():
    with open("user_overview.txt","w") as user_overview:
            total_tasks = len(task_list)
            uncompleted_tasks = 0
            completed_tasks = 0
            overdue_tasks = 0
            user_tasks = 0
            num_users = len(username_password.keys())
            num_tasks = len(task_list)
            users = []
            curr_date = date.today()
            for t in task_list:
                users.append(t['username'])

                if t['username'] == curr_user and not t['completed']:
                    uncompleted_tasks +=1
                if t['username'] == curr_user:
                    user_tasks +=1
                if t['username'] == curr_user and t['completed']:
                    completed_tasks +=1
                

                date_due = str(t['due_date']).split()
                if not t['completed'] and date_due[0] <= str(curr_date) and t['username'] == curr_user:
                    overdue_tasks +=1

            user_overview.write(f"{num_users} Users \n")
            user_overview.write(f"{num_tasks} total Tasks \n")
            user_overview.write(f"{user_tasks} Tasks that you have \n")
                
            if (user_tasks) > 0:
                user_overview.write(f"{(user_tasks/total_tasks)*100} percent tasks assigned to you \n")
                user_overview.write(f"{(completed_tasks/user_tasks)*100} percent tasks completed \n")
                user_overview.write(f"{(uncompleted_tasks/user_tasks)*100} percent tasks uncompleted by you \n")
                user_overview.write(f"{(overdue_tasks/user_tasks)*100} percent tasks overdue")
            user_overview.close()

def creatingtasks():
     if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass


def creatingusers():
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

# Read in user_data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
     



DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
creatingtasks()

with open("tasks.txt", 'r') as task_file:
         task_data = task_file.read().split("\n")
         task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
creatingusers()
with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
# Convert to a dictionary
username_password = {}
for user in user_data:
    username,password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    
    def menu1():
        global menu
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generating reports
ds - Display statistics
e - Exit
: ''').lower()
        
        
    menu1()
    if menu == 'r':
        while True:
            '''Add a new user to the user.txt file'''
        # - Request input of a new username
            new_username = input("New Username: ")

        # - Request input of a new password
            new_password = input("New Password: ")

        # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")
            if new_username in username_password.keys():
                print("This is already in use. Try again.")
            else:
                break

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
              # - If they are the same, add them to the user.txt file,
              print("New user added")
              username_password[new_username] = new_password
            
              with open("user.txt", "a") as out_file:
                user_data = []
                out_file.write(f'\n{new_username};{new_password}')
        else:
              print("Passwords does not match. The user account was not created")




    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        id = []
        i = 0
        for t in task_list:
            i = i+1
            if t['username'] == curr_user:
                 id.append(i)
            if t['username'] == curr_user:
                disp_str = f"Task {i}\n"
                disp_str += f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
        user_input = int(input("Please enter the task number to see a task. If not, please enter -1 to return to the home menu. "))
        global check
        check = input("Type Complete to complete task or Edit to edit the task due date and user ")
        for t in range(len(task_list)):
             for x in id:
                if user_input == -1:
                    menu1()
                elif user_input == x and check == 'Complete' and (x-1) == t:
                    task_list[t]['completed'] = True
                    writing()
                    menu1()
                elif user_input == x and check == 'Edit' and (x-1) == t:
                    task_due_date = input("Enter the new due date, (YYYY-MM-DD)")
                    task_due_date1 = datetime.strptime(task_due_date, '%Y-%m-%d').date()
                    new_user = input("Change who this task is assigned to")
                    if task_list[t]['completed'] == True:
                            print("This task has been completed and cannot be edited")
                    else:
                            task_list[t]['due_date'] = task_due_date1
                            task_list[t]['username'] = new_user
                            print(task_list)
                            writing()
                
                        
           
                            
    elif menu == "gr":
         taskoverview1()
         useroverview1()
         

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        creatingtasks()
        creatingusers()
        num_users = 0
        num_tasks = 0
        taskoverview1()
        useroverview1()

        with open("task_overview.txt", 'r') as taskoverview:
             print("Task Overview")

             print(taskoverview.read() )
        print("-----------------------------------")

        with open("user_overview.txt", 'r') as useroverview:
             print("User Overview")
             print(useroverview.read() )

        with open("tasks.txt", 'r') as task_file:
         for i in task_file:
              num_tasks +=1 

         with open("user.txt", 'r') as user_file:
             for i in user_file:
                  num_users +=1


        
             

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

  

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
