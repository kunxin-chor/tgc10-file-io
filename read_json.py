import json
with open('ecommerce.json') as fileptr:
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

