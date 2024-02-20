swimming = int(input("Please enter your swimming time"))
cycling = int(input("Please enter your cycling time"))
running = int(input("Please enter your running time"))
qualifying = swimming + cycling + running
print("This is your qualifying time,", qualifying, "minutes")
if qualifying <= 100: #checks if total qualifying time is less than 100 minutes
    print("You have recieved the Provincial Colours")
elif 101 <= qualifying <= 105: #checks if total qualifying time is between 101 and 105 minutes
    print("You have recieved the Provincial Half Colours")
elif 106 <= qualifying <= 110: #checks if total qualifying time is between 106 and 110 minutes 
    print("You have recieved the Provincial Scroll award")
else:
    print("You have recieved no award")