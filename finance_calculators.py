#This is a program that calculates either returns on investments or repayments on home loans
#user inputs whether they want to work out investment or bond repayment
import math
choice = input("invesment - to calculate the amount of interest you'll earn on your interest\n bond - to calculate the amount you'll have to pay on a home loan \n Enter either 'investment or 'bond' from the menu above to proceed: ")
choice2 = choice.lower() #changes user input to all lowercase to avoid users writing Bond and the program not recognising it
return1 = 0
repayment = 0
if choice2 != "investment" and choice2 != "bond":
    print("You have not picked a correct choice") #checks whether the user inputted the right command
if choice2 == "investment":
    deposit = int(input("Please enter the amount you are depositing"))
    rate = int(input("Please enter the interest rate"))
    years =int(input("Please enter the number of years that you are investing for"))
    interest = input("Do you want simple or compound interest?")
    if interest == "simple": #checks whether the user wants simple or compound interest
        return1 = deposit * (1+((rate/100)*years))
    else:
        return1 = deposit * math.pow((1+rate/100),years)
    print(return1)
elif choice2 == "bond":
    PV = int(input("Please enter the present value of the house"))
    rate = float(input("Please enter the interest rate"))
    i = (rate/100)/12  #calculates the monthly interest rate 
    months = int(input("Please enter the number of months it will take to repay the loan"))
    repayment = (i * PV)/(1-(1+i)**(-months)) #works out monthly repayment
    print(repayment)

