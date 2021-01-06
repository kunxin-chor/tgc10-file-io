fileptr = open("holidays.txt")
# for each line in the file represented by the fileptr variable
for line in fileptr:
    # print out the line
    print(line.strip())
fileptr.close()