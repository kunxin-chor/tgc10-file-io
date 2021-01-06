import json
filename = input("Please enter the json file to read from: ")
with open(filename) as fileptr:
    data = json.load(fileptr)
    while True:
        sku = input("Please enter a product SKU: ")
        if sku=='stop':
            break
        for product in data:
            if product['sku'] == sku:
                print("product found:")
                print(product['name'])
                print(product['price'])

