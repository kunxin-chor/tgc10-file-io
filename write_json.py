import json
data = [
    {
        "sku": "WALMART-01",
        "name": "Frozen Rubber Chicken",
        "price":25
    },
    {
        "sku": "WALMART-02",
        "name": "Rubber ball",
        "price": 5
    },
    {
        "sku": "WALMART-03",
        "name": "Broom",
        "price": 15
    }
]

with open('ecommerce2.json', 'w') as filepointer:
    json.dump(data, filepointer)