import matplotlib.pyplot as plt

# The program should consist of the following three functions:

# The first function should be named small and should have no parameters.
# The function should display a small square using a line plot.
# The line should be a red dotted line with circle markers.

# The second function should be named medium and should have no parameters. 
# The function should display a medium square around the small square using a line plot.
# The line should be a green dashed line with square markers.
# The third function should be named large and should have no parameters.
# The function should display a large square around the medium square using a line plot.
# The line should be a blue solid line with pentagon markers. 

def small():
    x = [1, 1, 2, 2, 1]
    y = [1, 2, 2, 1, 1]
    plt.plot(x, y, "r:o", label="Small Square")

def medium():
    x = [0, 0, 3, 3, 0]
    y = [0, 3, 3, 0, 0]
    plt.plot(x, y, "g--s", label="Medium Square")

def large():
    x = [-1, -1, 4, 4, -1]
    y = [-1, 4, 4, -1, -1]
    plt.plot(x, y, "b-p", label="Large Square")

def show_all():
    small()
    medium()
    large()
    plt.axis("equal")
    plt.title("All Squares")
    plt.legend()
    plt.show()

show_all()