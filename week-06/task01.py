# WEEK 06

# with open("dataOne.txt", "r") as file:
#     content = file.read()
    # print(content)

# create new file with X
newFile = open("myfile.txt", "x")
newFile = open("myfile.txt", "w")
newFile.write("Line 01 Added\n")
newFile.write("Line 02 Added\n")
newFile.write("Line 03 Added\n")
newFile.close()

newFile = open("dataOne.txt", "r")
print(newFile.read())