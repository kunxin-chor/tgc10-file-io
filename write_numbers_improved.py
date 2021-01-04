with open('new_numbers.txt') as fileptr:
    n = int(input("Please enter a number, or type in -99 to quit"))
    while n != -99:
        fileptr.write(str(n)+"\n")
        n = int(input("Please enter a number, or type -99 to quit"))

print("program ended")