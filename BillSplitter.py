
header = r"""
██████  ██ ██      ██          ███████ ██████  ██      ██ ████████ ████████ ███████ ██████  
██   ██ ██ ██      ██          ██      ██   ██ ██      ██    ██       ██    ██      ██   ██ 
██████  ██ ██      ██          ███████ ██████  ██      ██    ██       ██    █████   ██████  
██   ██ ██ ██      ██               ██ ██      ██      ██    ██       ██    ██      ██   ██ 
██████  ██ ███████ ███████     ███████ ██      ███████ ██    ██       ██    ███████ ██   ██ 


"""
def initial():
    print(header)
    start = input('Are you ready to split the bill?: ').lower()
    while start != 'no' and start != 'yes':
        print("Invalid Input. Try again")
        start = input('Are you ready to split the bill?: ').lower()
    if start == 'no':
        print("Ok thank you. Goodbye!")
        exit()
    bill = float(input("How much is the bill without tax and tip?: "))
    tax = float(input("How much tax did you pay?: "))
    tip = float(input("How much tip did you pay?: "))
    print("_________________________________________")
    edit_initial(bill, tax, tip)

def edit_initial(bill, tax, tip):
    print(f"\nYour total bill is: {round(bill + tax + tip, 2)}")
    double_check = input("Is this correct?: ").lower()
    if double_check != 'yes':
        change = input("Which would you like to change?: ").lower()
        amount = float(input("What is the new amount?: "))
        if change == 'bill':
            bill = amount
        elif change == 'tax':
            tax = amount
        elif change == 'tip':
            tip = amount
        else:
            print("Invalid Input. Try again")
        print(f"Got it. The new {change} is {amount}")
        edit_initial(bill, tax, tip)
    people(bill, tax, tip)

def people(bill, tax, tip):
    total_people = int(input(f"\nHow many people should we split {round(bill + tax + tip, 2)} by?: "))
    check_people = input(f"Got it. There are {total_people} is this correct?: ").lower()
    if check_people == 'yes':
        pass
    else:
        people(bill, tax, tip)




initial()