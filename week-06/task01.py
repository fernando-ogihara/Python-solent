# WEEK 06

# with open("dataOne.txt", "r") as file:
#     content = file.read()
    # print(content)

# create new file with X
newFile = open("myfile.txt", "x")
newFile = open("myfile.txt", "w")

for i in range(1, 11): 
    newFile.write("Line " + str(i) + "\n")
newFile.close()

with open("myfile.txt", "r") as newFile:
    getFile = newFile.read()
    print(getFile)