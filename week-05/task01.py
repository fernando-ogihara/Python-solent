# 🐍 Python Lists & Tuples — Interactive Lab (2-Hour Session)

# Welcome to this hands-on lab for **Python lists and tuples**.

# This session includes:

# - Guided explanations
# - Practice exercises
# - Interactive widgets
# - Mini-project
# - Quizzes
# - Challenges

# Run each code cell using **Shift + Enter**.

## 2️⃣ Python Lists — Basics

# A **list** is:

# - ordered
# - mutable (can change)
# - written with **[ ]**
# - can store mixed types

# TASK:
# numbers = [18, 32, 65, 80]
# names = ["John", "Maria", "Charlie", "Steven"]
# for number, name in zip(numbers, names):
#     print(f"{name} is {number} yo.")

###  Exercise 2 — Index & Slice

# Given:

# nums = [5, 10, 15, 20, 25, 30]
# Print 2nd element
# Print last using negative index
# Print slice [10, 15, 20]
# Print every second element
# print(len(nums))
# print(nums[-5])
# x = slice(1, 4)
# print(nums[x])

# Exercise 3

# scores =  [88,92,75,94,81]

# append new score
# scores.append(74)
# print("APPEND = " + str(scores))

# remove a score
# scores.remove(94)
# print("Remove = " + str(scores))

# sort
# scores.sort()
# print("Remove = " + str(scores))

# print highest & lowest
# print("Highest = " + str(max(scores)))
# print("Lowest = " + str(min(scores)))

########################### Shopping List Program  ###########################

# Create an empty list called shopping.
# Ask the user (or pretend to ask) to:
# c = "yes"
# shoppingList = []
# while c == "yes":
#     item = input("Add an item to your shopping list: ")
#     shoppingList.append(item)
#     c = input("Add another item? (yes/no): ")
# # Add at least 3 items
# print("Your current shopping list is: " + str(shoppingList))
# # Remove 1 item
# removeItem = input("Would you like to remove any item? (yes/no): ")
# while removeItem == "yes" and len(shoppingList) > 0:
#     itemToRemove = input("Which item?: ")
#     if itemToRemove in shoppingList:
#         shoppingList.remove(itemToRemove)
#         print(f"{itemToRemove} has been removed.")
#     else:
#         print(f"{itemToRemove} is not in the shopping list.")
#     print("Updated shopping list: " + str(shoppingList))
#     removeItem = input("Would you like to remove another item? (yes/no): ") 
# # Print the final list
# print("Final shopping list: " + str(shoppingList))

################ Exercise 1 — Player Inventory System (List Practice) ################

# A game player starts with this inventory:
inventory = ["sword", "shield", "potion"]
# Tasks:
# Add "bow" to the inventory
inventory.append("bow")
print(inventory)
# Replace "potion" with "mega potion"
inventory[2] = "mega potion"
print(inventory)
# Remove "shield"
inventory.remove(inventory[1])
# Print the final inventory
print(inventory)
# Print the first and last items
print(inventory[0], inventory[-1])

################ Exercise 3 — Racing Game Lap Times (Tuple Practice) ################

# Lap times in seconds:
lap_times = (62.1, 60.5, 61.2, 59.9)
# Tasks:

# Print the fastest lap
flap = max(lap_times)
print(f"Fastest lap: {flap}")
# Print the slowest lap

# Convert to a list and add a new lap time

# Convert back to a tuple

# Print the new tuple