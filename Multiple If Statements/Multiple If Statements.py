# print("Welcome to this wonderful theme park!")
# height = int(input("What is your height? "))
# bill = 0
#
# if height >=120:
#     age=int(input("What is your age? "))
#     if age >=18:
#         bill = 5
#         print("Your ticket is $5")
#     if age <=17:
#         bill = 3
#         print("Your ticket is $3")
#     picture = input("What you like a picture? Yes or No? ")
#     if picture == "Y":
#         bill += 3
#         print(f"Your bill is ${bill}")
# else:
#     print("You cannot ride.")
# print("Welcome to the theme park!")
# height = int(input("What is your height? "))
# bill = 0
#
# if height >= 120:
#     age = int(input("What is your age? "))
#     if age >=18:
#         bill = 5
#         print("Your ticket is $5")
#     if age <=17:
#         bill = 3
#         print("Your ticket is $3")
#     picture = input("Would you like a picture? Yes or No? ")
#     if picture == "Yes":
#         bill += 3
#         print(f"Your bill is ${bill}")
#     if picture == "yes":
#         bill += 3
#         print(f"Your bill is ${bill}")
#     else:
#         print(f"Your bill is ${bill}")
# else:
#     print("You cannot ride.")
print("Welcome to the theme park!")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age >=18:
        bill = 5
        print(f"Your ticket price is ${bill}")
    if age <=17:
        bill = 3
        print(f"Your ticket cost is ${bill}")
    picture = input("Would you like to add a picture? ")
    if picture == "Yes":
        bill +=3
        print(f"Your total bill is ${bill}")
    if picture == "yes":
        bill +=3
        print(f"Your total bill is ${bill}")
else:
    print("You aren't tall enough.")
