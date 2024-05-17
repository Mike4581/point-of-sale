total =0.00 #declare viarables
output = ""

def addCheese(): #functions
    return 50.00
    

def addBread():
    return 15.00
    

def addMilk():
    return 30.00
    
    
mylist =["1. cheese: R50.00","2. milk: R30.00","3. bread: R15.00"] #declare list

done = False #Sentinel viarable

while done == False: 
    

    for x in mylist: #for loop 
        print(x) #display list
    
    choice=input('\nEnter a item number (Enter 0 to check out):  \n') #get user input


    if input ==1:                       
        total += addCheese()                #increase total
        output += "cheese: R50.00\n"
    elif input ==2:
        total += addMilk()
        output += "milk: R30.00\n"
    elif input ==3:
         total += addBread()
         output += "bread: R15.00\n"
    else:
        done = True

print(str(output))      #display total
print("_____________")

print("total: " + str(total))