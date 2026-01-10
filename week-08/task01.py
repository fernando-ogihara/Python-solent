import matplotlib.pyplot as plt
import random

# The first function should be named display_line and should take 2 parameters.
# The first parameter is a list of x values.
# The second parameter is a list of y values.
# The function should display a line plot using the arguments supplied for the parameters.
# The second function should be named run_task1 and should take 0 parameters.
# The function should create a list named x_values containing the following values: 1, 2, 3, 4, 5
# The function should then create a list named y_values containing the following values: 1, 4, 9, 16, 25
# The function should then call the first function passing x_values and y_values as arguments. 

def displayLine(x,y):
    plt.plot(x,y)
    plt.xlabel('X Val')
    plt.ylabel('Y Val')
    plt.title('My Line Plot')
    plt.show()

def run_task1():
    x_values = []
    y_values = []
    for i in range(10):
        x_values.append(random.randint(1, 20))
        y_values.append(random.randint(1, 50))
        i += 1
    displayLine(x_values, y_values)

run_task1()