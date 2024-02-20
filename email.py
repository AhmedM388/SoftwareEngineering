# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
email_list = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email_list.append(Email("email1@example.com", "Welcome to Hyperion Dev", "This is email content 1"))
    email_list.append(Email("email2@example.com", "Well Done on your excellent grades", "This is email content 2"))
    email_list.append(Email("email3@example.com", "Great Work on the bootcamp", "This is email content 3"))

def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(email_list):
        print(f"{i+1}. {email.subject_line}")

def read_email(index):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email = email_list[index]
    print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}")
    email.mark_as_read()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        # logic here to read an email
        list_emails()
        index = int(input("Enter the number of the email to read: ")) - 1
        read_email(index)
        
    elif user_choice == 2:
        # logic here to view unread emails
        unread_emails = [i for i, email in enumerate(email_list) if not email.has_been_read] #"Creates a new list containing the indices of all emails in email_list that have not been read."
        for i in unread_emails:
            print(f"{i+1}. {email_list[i].subject_line}")
            
    elif user_choice == 3:
        # logic here to quit appplication
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input.")
