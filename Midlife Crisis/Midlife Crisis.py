print("Welcome to the show!")
movie = input("What rating of movie would you like to see? ")
bill = 0
tickets = 0

if movie == "R":
    age = int(input("How old are you? "))
    bill +=10
    if age >= 17:
        total_tickets = int(input("How many tickets would you like to buy? "))
        if total_tickets >= 1:
            amount = bill*total_tickets
            print(f"That will be ${amount}. ")
if movie == "X":
    age = int(input("How old are you? "))
    bill +=15
    if age >= 35 and age < 45:
        total_tickets = int(input("How many tickets would you like to buy? "))
        if total_tickets >= 1:
            amount = bill*total_tickets
            print(f"That will be ${amount}. ")
    else:
        print("You will need to pick another movie.")
if movie == "PG-13":
    age = int(input("How old are you? "))
    bill +=7
    if age >= 12:
        total_tickets = int(input("How many tickets would you like to buy? "))
        if total_tickets >= 1:
            amount = bill*total_tickets
            print(f"That will be ${amount}. ")
    else:
        print("You will need to pick another movie.")
if movie == "G":
    age = int(input("How old are you? "))
    bill +=3
    if age > 0:
        total_tickets = int(input("How many tickets would you like to buy? "))
        if total_tickets >= 1:
            amount = bill*total_tickets
            print(f"That will be ${amount}. ")
    else:
        print("You will need to pick another movie.")
else:
    print("Sorry, we do not have that rating.")




