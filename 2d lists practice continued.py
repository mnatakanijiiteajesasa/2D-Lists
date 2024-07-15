import json
sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694}, "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
         "Anne": {"N": 5239, "S": 6209, "E": 5820, "W": 1409}, "Fiona": {"N": 4398, "S": 5367, "E": 4673, "W": 7645}}

sales_json = json.dumps(sales)
print(sales_json)
# person = input("Enter a salesperson's name: ")
# region = input("Enter a region: ")
# print(sales[person][region])
# new_data = int(input("Enter new data: "))
# sales[person][region] = new_data
# print(sales[person])


