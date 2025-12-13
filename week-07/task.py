# The program should consist of the following two functions:

# The first function should be named observed and should have no parameters.
# def observed()
# The function should create a set named observations.
# The function should populate the set with the following items:
#     "Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"
# Finally, the function should return the set observations.

# The second function should be named run_task1 and should have no parameters.
# The function should call the first function and display the set returned by the call.


# An example run of such a program is shown below:

# {'Car', 'Sky Scraper', 'Bike', 'House'}

# Code your solution and be sure to include appropriate comments in your code.

# This program defines two functions to create and display a set of observations.

def observed():
    # populate the set
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations

def run_task1():
    observation_set = observed()
    print(observation_set)

if __name__ == "__main__":
    run_task1()