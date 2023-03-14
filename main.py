import pandas as pd

# from numpy import partition
from pandas import read_csv


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

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index=[x for x in range(1, 4)])
#
# print(df)
####################################

# class Car:
#     '''This is my class'''
#     def __init__(domat, model, year):
#         domat.year = year
#         domat.model = model
#
#
# Suabru = Car('Subaru', 2018)
# print(Suabru.year)
# print(Car.__doc__)
##########

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
#
# # load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)
###########

# cars = {
#     "Honda's HP": [120, 140, 160, 180],
#     'Seat HP': [150, 180, 200, 215],
# }
# range_len = len(cars["Honda's HP"])
# table = pd.DataFrame(cars, index=[x for x in range(100, 107, 2)])
#
# print(f'The whole table: \n {table}\n')
#
# print(f'Just index 100 and 103: \n {table.loc[[100, 106]]}')
######################
#
# cars = {
#     "Honda's HP": [120, 140],
#     'Seat HP': [150, 180],
# }
#
# my_table =pd.DataFrame(cars, index = ['2000', '2001'])
# print(my_table.loc['2000'])
###################################

# table = read_csv('data.csv',)
# pd.options.display.max_rows = 200
# # print(table.head(10))
# print(table.info())
# #
# print(table.loc[1])

#
# print(pd.options.display.max_rows)
###############################

# table = pd.read_json('data_js.js')
# print(table)
#######################

# my_table = pd.read_csv('data.csv')
# print(my_table.to_string())
# new_table = my_table.dropna()
# print(new_table.to_string())
####################################

# table = pd.read_csv('data.csv')
# table.dropna(inplace=True)
# print(table.to_string())
#################################

# table = pd.read_csv('data.csv')
# table.fillna(300, inplace=True)
# print(table.to_string())

#
# df = pd.read_csv('data.csv')
# df['Calories'].fillna(245, inplace=True)
# print(df.to_string())
####################################


#
# df = pd.read_csv('data.csv')
# df['Calories'].fillna(100, inplace=True)
# print(df.to_string())
#################################

# a = {1,2,3}
# b={3 ,4, 5}
# print(a - b)
#######################

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pd.DataFrame(mydataset)
# print(myvar)
#
#
# def make_table(my_data):
#     len_of_list = len(my_data['studenst'])
#     index_range = [x for x in range(1, len_of_list + 1)]
#     frame = pd.DataFrame(my_data, index=index_range)
#     return frame
#
#
# student_info = {
#     'studenst': ['Stan', 'Elly', 'Yoan', 'Teddy'],
#     'grades': [5.5, 6, 6, 6]
# }
# curent_table = make_table(student_info)
# print(curent_table)
# print()
#
# student_info2 = {
#     'studenst': ['Stan', 'Elly', 'Yoan', 'Teddy'],
#     'grades': [5, 5, 6, 6]
# }
# curent_table = make_table(student_info2)
# print(curent_table)
##############################
#
# df = pd.read_csv('data.csv')
# print(df.to_string())
# print(pd.options.display.max_rows)
#############################

#Pandas - Cleaning Data

# df = pd.read_csv('data.csv')
#
# df.dropna()
# print(df.to_string())
