cheese =50.00
milk =30.00
bread =15.00
price =0.00

print("cheese: Php R50.00")
print("milk: Php R30.00")
print("bread: Php R15.00")

while True:
    choice=input('\nChoose an item: cheese, milk, bread\n')
    if choice == 'cheese':
        choice=input('Would you like to pick another product? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an product: cheese, milk, bread\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    
    elif choice == 'milk':
        choice=input('Would you like to pick another product? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an product: cheese, milk, bread\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")

    elif choice == 'bread':
        choice=input('Would you like to pick another product? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an product: cheese, milk, bread\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")

    else:
        print("Error!")
        break
#create our dictionary, shopping products as keys and price of product as value
shoppingDict = {"cheese":50.00,"milk":30.00,"bread":15.00}
#iterate through the dictionaries products printing them out in a certain format
for k,v in shoppingDict.products():print(f'{k}: Php {v}')
while True:
    #promp user to enter an product
    choice=input('\nChoose an product: cheese, milk, bread\n')
    #if so add the key's value(price)to price
    try:price += shoppingDict.get(choice)
    #if the user does not enter a valid product, we print a error
    except KeyError:print('Error')
    #ask them if they want to try again
    if input('Would you like to try again? y/n') == 'n':
        print(f'Total Cost: {price}')
        break
    