# open the file 'data.txt' for writing
valid_fruits = ['apple', 'orange', 'pineapple', 'watermelon', 'durian']
with open('data.txt', 'w') as fileptr:
    while True:
        fruit = input("Enter the name of a fruit ")
        # if fruit == 'apple' or fruit == 'orange' or fruit =='pineapple' or fruit =='watermelon' or fruit =='durian':
        if fruit in valid_fruits:
            fileptr.write(fruit + "\n")
        else:
            break
