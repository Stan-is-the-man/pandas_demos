import pandas as pd

cars_models = {
    'cars': ["Subaru", "Seat", "Honda"],
    'models': ['Forester', 'Tarraco', 'Pilot']
}

my_data = pd.DataFrame(cars_models)

print(my_data)

print(f"Current version of PANDAS is {(pd.__version__)}")
###########################

a = [1, 7, 2, 5, 3, 4, 6, 8, 9]
myvar = pd.Series(a)
print(myvar)

#################

a = ['Stan', 'The', 'Man']
myvar = pd.Series(a)

b = ['Stan', 'The', 'Man']
myvar_b = pd.Series(a, index=['a', 'b', 'c'])


print(myvar)
print(myvar_b)
######################




