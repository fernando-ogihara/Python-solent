import time

# continueApp = "no"

# loading = "Doing calculation..."

# while continueApp != "yes":
#     continueApp = input("Would you like to perform another calculation? (yes/no) ")
#     if continueApp == "no":
#         print("Thanks")
#         break
#     else:
#         print("What calculation would you like to perform? (add, subtract, multiply, divide)")
#         calculation = input()
#         print("Enter the first number: ")
#         firstNum = input()
#         print("Enter the second number: ")
#         secondNum = input()

#         if calculation == "add":
#             result = float(firstNum) + float(secondNum)
#             print(loading)
#             time.sleep(1)
#             print("The result is: " + str(result))
#         elif calculation == "subtract":
#             result = float(firstNum) - float(secondNum)
#             print(loading)
#             time.sleep(1)
#             print("The result is: " + str(result)) 
#         elif calculation == "multiply":
#             result = float(firstNum) * float(secondNum)
#             print(loading)
#             time.sleep(1)
#             print("The result is: " + str(result)) 
#         elif calculation == "divide":
#             result = float(firstNum) / float(secondNum)
#             print(loading)
#             time.sleep(1)
#             print("The result is: " + str(result)) 
#         else:
#             print("Calculation type invalid.")
#             continueApp = input("Would you like to perform another calculation? (yes/no) ")
#             if continueApp == "no":
#                 break
#             else:
#                 continueApp = input("Would you like to perform another calculation? (yes/no) ")
#         continueApp = "no"
        
# print("Thanks")

# PIZZA TASK

# users = int(input("Enter the number of users: "))
# if users < 1:
#     print("Please, you must type a number bigger than 0.")
# elif users < 3:
#     print("A small pizza for your party is suitable.")
# elif users >= 3 and users <6:
#     print("A medium pizza for your party is suitable.")
# elif users >= 6 and users <10:
#     print("A large pizza for your party is suitable.")
# else:
#     print("Invald input.")

# Password checker
# def getAttempts(attempt):
#     if attempt < 2:
#         print("You have " + str(2 - attempt) + " tries left.")
#     else: 
#         print("no more tries left.")

# correctPassword = "fernando123"

# for attempt in range(3):
#     password = input("Enter your password: ")
#     if password == correctPassword:
#         print("User allowed")
#         getAttempts(attempt)
#         break
#     elif password == "Fernando123" or password == "FERNANDO123":
#         getAttempts(attempt)
#         print("Password is case sensitive.")
#     else:
#         getAttempts(attempt)
#         print("User not allowed")
    
    
# Hogwart sorting hat

print("Welcome to the Hogwarts Sorting Hat Ceremony!")
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

hatInput = input("Please type your value: (bravery, loyalty, intelligence, ambition)")

def loading():
    print("Loading...")
    time.sleep(1)

def getValue (value):
    match value:
        case "bravery":
            return houses[0]
        case "loyalty":
            return houses[1]
        case "intelligence":
            return houses[2]
        case "ambition":
            return houses[3]
        case _:
            return "Invalid input."

name = input("Enter your name: ")
print("Hello, " + name + "!")
getHouse = getValue(hatInput)
loading()
print("You have been sorted into: " + getHouse)
