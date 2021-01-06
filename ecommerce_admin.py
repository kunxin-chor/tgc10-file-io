import json

data = []

while True:
    choice = input("Do you want to enter a new product (y/n)? ")
    if choice=='n':
        break
    sku = input("Please enter the SKU of the product >")
    name = input("Please enter the name of the product >")
    price = float(input("Please enter the price of the product > "))
    data.append({
        "sku": sku,
        "name": name,
        "price": price
    })     

filename = input("Please enter the filename to write to: ")
with open(filename, "w") as fileptr:
    json.dump(data, fileptr)