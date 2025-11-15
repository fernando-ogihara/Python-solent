import time
import random as rnd

# param = input("What's your favorite color? ")

# def name(param):
#     return f"Your favorite color is {param}!"

# print(name(param))

# listNames = ["Alice", "Fernando", "Chloe"]

# for i in listNames:
#     print(name(i))

# loading = "Loading..."
# gameOver = """
#          _____       ___       ___  ___   _____  
#         /  ___|     /   |     /   |/   | |  ___| 
#         | |        / /| |    / /|   /| | | |__   
#         | |  _    / ___ |   / / |__/ | | |  __|  
#         | |_| |  / /  | |  / /       | | | |___  
#         \_____/ /_/   |_| /_/        |_| |_____|
         
#          _____   _     _   _____   _____   
#         /  _  \ | |   / / |  ___| |  _  \  
#         | | | | | |  / /  | |__   | |_| |  
#         | | | | | | / /   |  __|  |  _  /  
#         | |_| | | |/ /    | |___  | | \ \  
#         \_____/ |___/     |_____| |_|  \_\ """

# right = "R"
# left = "L"
# straight = "U"

# treasure = ["R", "U", "U", "L"]
# success = "You found the treasure!"

# def startGame():
#     print("Game stating!")
#     print(loading)
#     time.sleep(1)

# def endGame():
#     print(gameOver)

# def playGame():
#     startGame()
#     for step in treasure:
#         choice = input("Choose your path! Left(L), Right(R) or Straight(U): ").upper()
#         if choice == step:
#             print("Good choice!")
#         else:
#             endGame()
#             return
#     print(success)

# playGame()

# We wish to create a program to play a game of "Guess the Number".
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image
import io

gameStartUrl = "https://lilyandpaulatakemke.wordpress.com/wp-content/uploads/2015/12/saw-blog-7.gif"
makeYourChoiceUrl = "https://lilyandpaulatakemke.wordpress.com/wp-content/uploads/2015/12/saw-blog-8.gif"  # Changed to match the variable name used
gameOverUrl = "https://lilyandpaulatakemke.wordpress.com/wp-content/uploads/2015/12/blog-saw.gif"  # Changed to match the variable name used

def defineImage(url):
    with urllib.request.urlopen(url) as response:
        image_data = response.read()
        return image_data  # Return the image data

def loadImage(url):
    try:
        image_data = defineImage(url)
        image = Image.open(io.BytesIO(image_data))
        plt.figure(figsize=(4, 4))
        plt.imshow(image)
        plt.axis('off')  # Hide axes
        plt.show()
    except Exception as e:
        print(f"Error loading image: {e}")

def guessNumGame():
    secretNum = rnd.randint(1, 5)
    attempts = 3
    loadImage(gameStartUrl)
    print("I'm thinking in a number between 1 and 5")
    for attempt in range(attempts):
        guess = int(input("Please, type a number between 1 and 5: "))
        if (guess < 1 or guess > 5):
            print("invalid number (must be 1 and 5 jackass)")
        elif guess == secretNum:
            print("Boss mate....Congrats")
            break
        else:
            loadImage(makeYourChoiceUrl)
            attempts -= 1
    loadImage(gameOverUrl)

guessNumGame()