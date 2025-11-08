#multiplication up to 20

# userNum = int(input("Enter a number to see its multiplication table up to 10: "))

# for i in range(1,11):
#     result = userNum * i
#     print(f"{userNum} x {i} = {result}")

####################################################################################

#count steps

# numOfSteps = int(input("Enter the number of steps: "))
# for i in range(numOfSteps, 0, -1):
#     print(f"{i} steps remaining")

#######################################################################################
word = str(input("Enter a word: "))
# for position in range(0, len(word)):
#     print(f"Letter at position {position} is {word[position]}")

# write the work from backwards in the same line
print("Now backwards:")
for position in range(len(word)-1, -1, -1):
    print(f"{word[position]}", end=" ")