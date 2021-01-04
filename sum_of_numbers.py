fileptr = open('numbers.txt')
total = 0
smallest = None
for line in fileptr:
    number = int(line.strip())
    if smallest == None:
        smallest = number
    elif number < smallest:
        smallest = number
    
    total = total + number

print("Smallest number=", smallest)
print("Sum of all the numbers=", total)

fileptr.close()
        