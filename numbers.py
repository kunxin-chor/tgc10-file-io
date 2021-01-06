choice = input("Do you want to (r)ead from file or (a)ppend to file: ")

# three ways to open a file
# 1. (default) r --> reading, to fetch/read data from a file
# 2. w --> write, write data to file, overwrite if a file already exists
# 3. a --> append, write data to END of file

if choice=='r':
    # read from file
    with open('numbers.txt') as fileptr:
        total = 0
        for line in fileptr:
            # must convert each line read from the file as integer
            total += int(line)
            print(line.strip())
        print("total: ", total)
elif choice=='a':
    # append to file
    # if the file does not exist, then Python will create it
    # if the file exists, Python will add new lines to its back
    with open('numbers.txt', 'a') as fileptr:
        while True:
            number = input("Enter a number, type 'stop' to end: ")
            if number=='stop':
                break
            else:
                fileptr.write(number+"\n")
else:
    print("Command not recongized")