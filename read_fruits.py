with open('fruits.txt') as fileptr:
    # state variable
    # supposed to hold the answer at the end 
    # of the for-loop
    total_cost = 0
    count = 0
    for f in fileptr:
        f = f.strip().lower()
        print(f)
        if f == 'apple':
            count += 1
        if f == 'orange':
            total_cost += 0.7
        if f == 'apple':
            total_cost +=0.5
        if f == 'pineapple':
            total_cost+=1
        if f == 'watermelon':
            total_cost+=2.5
        if f == 'durian':
            total_cost +=10
    print("how many apples =", count)
    print("total cost =", total_cost)