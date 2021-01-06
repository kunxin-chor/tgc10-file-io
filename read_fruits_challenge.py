cost_table = {
    'apple':0.5,
    'orange': 0.7,
    'pineapple': 1,
    'watermelon': 2.5,
    'durian': 10
}



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
        total_cost += cost_table[f]
    print("how many apples =", count)
    print("total cost =", total_cost)