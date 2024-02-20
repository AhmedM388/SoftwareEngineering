def calculator(): #creates the function
    operations = ["*","+","-","/"] #limiting operations to 4 
    while True: #while loop continues until the user enters 2 numbers
        try:
            number1 = int(input("Please enter a number "))
            number2 = int(input("Please enter a number "))
            break
        except ValueError: #if the user doesn't enter a correct number, it will print out this sentence and start again.
            print("This is not a valid integer. Please start again and enter both numbers. ")
    while True:
        try:
            operation = input("Please enter a operation ")
            if operation in operations:
                break
        except: pass
                   
    answer = 0
    file = open('calculator.txt','a') #opens text file
    if operation == "*": #checks user input
        answer = number1 * number2 
        print(answer) 
        file.writelines(f'{number1}*{number2}={answer}''\n') #writes the following line into the text file
        file.close() #closes the file
    elif operation == "/":
       while True: #checks whether if the equation is actually divisable
        try:
            answer = number1/number2 
            print(answer)
            file.writelines((f'{number1}/{number2}={answer}''\n'))
            file.close()
            break
        except ZeroDivisionError:  #if the user divides by zero, it prints out the statement and ends the program
            print("You cannot divide by zero.")
            break
    
    elif operation == "+":
        answer = number1+number2 
        print(answer)
        file.writelines(f'{number1}+{number2}={answer}''\n')
        file.close()
    elif operation == "-":
        answer = number1 - number2 
        print(answer)
        file.writelines(f'{number1}-{number2}={answer}''\n')
        file.close()


while True: #gives the user a choice to add new equation or read a text file. Continues until they answer either yes or no.
    choice = input("Do you want to create a new equation. If so, type yes, otherwise type no. ")
    if choice == "yes" or choice == "no":
        break

file1 = None
data = ""
if choice == "yes":
    calculator() #calls the function
elif choice == "no":
    while True:
        try:
            textfile = input("Please enter the name of the text file you wish to see.")
            file1 = open(textfile,"r") #opens text file in read mode
            data = file1.read() #reads the contents of the file.
            print(data) 
            file1.close() #closes said file
            break
        except FileNotFoundError as SyntaxError: #if the file is not found, it will print out this error message
            print("This file doesn't exist.")


    
        




