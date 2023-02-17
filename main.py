import pandas as pd

#
# cars_models = {
#     'cars': ["Subaru", "Seat", "Honda"],
#     'models': ['Forester', 'Tarraco', 'Pilot']
# }
#
# my_data = pd.DataFrame(cars_models)
#
# print(my_data)
#
# print(f"Current version of PANDAS is {(pd.__version__)}")
# ###########################
#
# a = [1, 7, 2, 5, 3, 4, 6, 8, 9]
# myvar = pd.Series(a)
# print(myvar)
#
# #################
#
# a = ['Stan', 'The', 'Man']
# myvar = pd.Series(a)
#
# b = ['Stan', 'The', 'Man']
# myvar_b = pd.Series(a, index=['a', 'b', 'c'])
#
# c = ['Stan', 'The', 'Man']
# myvar_c = pd.Series(c, index=[100, 101, 102])
#
#
# print(myvar)
# print(myvar_b)
# print(myvar_c)
# ###################

# students = ['Adam', 'John', 'Mary', 'Mike', 'Sarah', 'Jane']
# my_table = pd.Series(students, index=[x for x in range(100, 106)])
#
# print(students[0])
# print(my_table[100])
###########

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)
################

# cars = {'Subaru': 'Forester', 'Seat': 'Tarraco', 'Honda': 'Pilot'}
# table = pd.Series(cars)
# print(table)
#########################

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45],
# }
#
# myvar = pd.DataFrame(data, index=)
# print(myvar)
#################
#
# def number_of_keys(dict):
#     count = 0
#
#     for key, value in dict.items():
#         count += 1
#
#     return count
#
#
#
#
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45],
# }
#
# ranger = number_of_keys(data)
#
# myvar = pd.DataFrame(data, index=[x for x in range(ranger+1)])
# print(myvar)
#########################

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=[x for x in range(1, 4)])

print(df)
