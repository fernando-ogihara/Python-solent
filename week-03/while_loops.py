# [Tasks]

# We wish to create a program to simulate a robot removing apples from a box.

# Start by creating a new folder called week3 and then inside of this folder create a new python file called while_loops.py.

# The program should start by displaying the message "How many apples should I remove?".
# The program should then read in the user's response.
# The program should then create a variable to track the number of removed apples and set this to 0.
# The program should then use a while loop to do the following:
#     Display the message "Removed apple."
#     Increment the variable for tracking the number of removed apples

# numOfApples = int(input("How many apples should I remove?"))
# removedApples = 1
# while removedApples <= numOfApples:
#     print("Apple " + str(removedApples) + " removed from the box.")
#     removedApples += 1

#######################################################################################################

# [Tasks]

# We wish to create a program that allows a robot to avoid obstacles.

# The program should start by displaying the message "How many obstacles must I avoid?".
# The program should then read in the user's response.
# The program should then create a variable to track the number of obstacles and set this to 0.
# The program should then use a while loop to do the following:
#     Display the message "Avoiding..." at the start of each iteration
#     Increment the variable for tracking the number of obstacles
#     Display the message "...Done! [n] obstacles avoided!" at the end of each iteration where [n] should be replaced by the current number of obstacles.
# Finally, the program should display the message "All obstacles have been avoided."

#############################################################################################################

# [Tasks]

# We wish to create a program that simulates a robot charging it's battery.

# The program should start by displaying the message "How many bars should be charged?".
# The program should then read the user's response.
# The program should then create a variable to track the number of bars charged and set this to 0.
# The program should then use a while loop to do the following:
#     Display the message "Charging:".
#     Increment the variable for tracking the number of charged bars.
#     Display the number of charged bars.
# Finally, the program should display the message "The battery is fully charged."

# An example run of such a program is shown below:

# How many bars should be charged?
# 5
 
# Charging: █
# Charging: █ █
# Charging: █ █ █
# Charging: █ █ █ █
# Charging: █ █ █ █ █

# The battery is fully charged.


numOfBars = int(input("How many bars would you like to charge? "))
chargedBars = 0

while chargedBars < numOfBars:
    print("Charging: " + "█ " * (chargedBars + 1))
    print("")
    chargedBars += 1

print("Battery fully charged.")
