# [Tasks]

# We wish to create a program that allows us to display a grid of ASCII emoji.

# Start by creating a new python file called nested_loops.py and storing it in the week3 folder you created previously:

# The program should start by asking the user how many rows and columns they would like.
# The program should then display a grid of ascii emoji where the size of grid matches the number of rows and columns specified by the user. 

import random

emojisList = ["\U0001f305", "\U0001f634", '\u2601', "\U0001f326", "\U0001f329", '\U0001f308', "\U0001F321", '\U0001f31e', "\U0001f31d", "\u26C8", "\u2744"]

numOfRows = int(input("Enter number of rows: "))
numOfCols = int(input("Enter number of columns: ")) 

for r in range(numOfRows):
    for c in range(numOfCols):
        print(random.choice(emojisList), end=" | ")
    print()


