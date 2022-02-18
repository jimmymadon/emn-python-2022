import pandas as pd

cars_list = ["Mercedes", "BMW", "Audi"]
print("Printings cars_list")
print(cars_list)
print()

# Creating a Pandas Series using 1 simple python list
cars_series = pd.Series(cars_list)
print("Printing cars_series:")
print(cars_series)
print()
print("Third car in the cars_series is:", cars_series[2])

cars_models = ["C Class", "4 Series", "Q5"]
# Creating a Pandas Series using 2 python lists: First list for values, second list for index/labels
cars_series_with_labels = pd.Series(cars_list, cars_models)
print("Printing cars_series_with_labels:")
print(cars_series_with_labels)
print()
print("Third car in the cars_series_with_labels is:", cars_series_with_labels["Q5"])
