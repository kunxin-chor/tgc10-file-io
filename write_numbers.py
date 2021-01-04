# the second argument, 'w', means we want to open the file for writing
# if the file does not exist, Python will create the file
# if the file exists, then all the existing content in the file deleted
fileptr = open('new_numbers.txt',  "w")

n = int(input("Please enter a number, enter -99 to stop"))
while n != -99:
    fileptr.write(str(n)+"\n")
    n = int(input("Please enter a number, enter -99 to stop"))

print("Program ended")
fileptr.close()