

# grades = [{"math": 45, "Eng": 35, "Com": 67}, {"math": 56, "Eng": 87, "Com": 75}, {"math": 65, "Eng": 78, "Com": 86}]
# print(grades[0]["Eng"])
# grades = {"Susan": {"math": 56, "Eng": 46, "Com": 79}, "peter": {"math": 45, "Eng": 76, "Com": 98}}
# print(grades)

# simple_array = [[4, 5, 6], [5, 3, 7], [4, 3, 5]]
# simple_array[2][1] = 4
# simple_array[2].append(9)
# print(simple_array)

# create a data set table

# data_set = {"mercedes": {"cabs": 100, "suv": 354, "trucks": 45}, "toyota": {"cabs": 45, "suv": 78, "trucks": 98}}
# print(data_set["mercedes"])
# for i in data_set:
#    print(data_set[i]["trucks"])
# print(data_set["toyota"]["trucks"])
# data_set["mercedes"]["cabs"] = 200
# print(data_set)

# from the nums table created, ask the user the row they would like displayed and display that row only.


nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Which row would you like displayed? "))
print(nums[row])
# extra = int(input("Enter the number you would like to add to the row you selected: "))
# nums[row].append(extra)
# print(nums[row])
column = int(input("Which column in the row do you want displayed? "))
print(nums[row][column])
new_value = input("Do you want to change the value displayed above? (y/n)")
if new_value == "y":
    new_real_value = int(input("Which number would you like to replace it?"))
    nums[row][column] = new_real_value
else:
    print(nums[row][column])

print(nums[row])






