# open the file 'data.txt' for writing
with open('data.txt', 'w') as fileptr:
    while True:
        fruit = input("Enter the name of a fruit ")
        if fruit == 'apple' or fruit == 'orange' or fruit =='pineapple' or fruit =='watermelon' or fruit =='durian':
            fileptr.write(fruit + "\n")
        else:
            break
