# We wish to create a program to help record how many of each type of item is observed (e.g. 2 skyscrapers, 5 neon signs, etc.).

# The program should consist of the following two functions:

# The first function should be named observed_items and should have no parameters.
def observed_items():
# The function should create a list named observations.
    observations= []

# The function should populate the list with 7 values read in from the user.  There should be some duplicate values.
    for l in range(7):
        item=input("Enter an observation:")
        observations.append(item)# Help to add items at end one by one
    return observations
# Finally, the function should return the list named observations.

# The second function should be named run_task2 and should have no parameters.
def run_task2():
  print("Counting Observations....")
  data=observed_items()# storing in local variable
  counts=set()
# The function should start by displaying the message "Counting observations...".
# The function should then call the first function and store the returned list in a local variable.
# The function should then create an empty set.
# For each value in the list, the function should populate the set as follows:
  for value in data:
    counts.add((value,data.count(value)))
  print(counts)
run_task2()
#     create a tuple that contains the value from the list along with a count for how many times that value appears in the list e.g.. ("Skyscraper", 2).
#     You can do this using the method count for a list.
#     For example, data.count("Sky Scraper") will return the number of times "Sky Scraper" appears in the list data.
# Finally, the function should display the content of the set.