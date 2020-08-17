# Guided Exploration No. 3
# Chau Boi Nguyen
# random library(edit)
import random
# store rap names
possible_names = []
# open the file name "rap-names-output.txt"
outputFile = open('rap-names-output.txt', 'w')
# read the data in "rap-names.txt" files
with open('rap-names.txt', 'r') as dataFile:
    # "This for loop is going to iterate through each line in the **rap-names.txt** file, one line at a time."(from readme file)
    for name in dataFile:
        # In possible_names variables add the copy of name with trailing white space removed
        possible_names.append(name.rstrip())
# This code ask the number of rap names
count = int(input('How many rap names would you like to create? '))
# This code ask the number of parts to create a whole rap
parts = int(input('How many parts should the name contain? '))
# "This code is going to use a counted loop to generate the total number of rap names the user wants to generate". (from readme file)
for i in range(count):
    # create a list to store rap name parts
    name_parts = []
    # "the counted loop will iterate for the number of rap names that the user wants as part of the names" (from readme file)
    for j in range(parts):
        # get random name start from 0 to the length of possible_names list and -1
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])
# write out a name
outputFile.write(f"{' '.join(name_parts)}\n")
# print it out
print(f"{' '.join(name_parts)}")
# closed file
outputFile.close()
