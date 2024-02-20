f = open("DOB.txt",'r+') #opens the file in read mode
names = ""
DOB = ""
line2 = ""
for line in f: #for each line in the text file 
    line2 = line.split() #separates the lines into words
    names += f'{line2[0]} {line2[1]}''\n' #names are separated and joined together 
    DOB += f'{line2[2]} {line2[3]} {line2[4]}''\n' #DOBs are separated and joined together

print("Names:",'\n',names) #prints names
print("Date of Birth:",'\n',DOB) #prints DOB


