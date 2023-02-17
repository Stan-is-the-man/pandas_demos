import pandas as pd

cars_models = {
    'cars': ["Subaru", "Seat", "Honda"],
    'models': ['Forester', 'Tarraco', 'Pilot']
}

my_data = pd.DataFrame(cars_models)

print(my_data)

print(f"Current version of PANDAS is {(pd.__version__)}")

#####################

