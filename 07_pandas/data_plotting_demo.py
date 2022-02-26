import os
import pandas as pd
import matplotlib.pyplot as plt

current_file_path = os.path.dirname(__file__)
print(current_file_path)
dataframe = pd.read_csv(os.path.join(current_file_path, "data.csv"))
dataframe.corr()

# dataframe.plot()
# plt.show()

# dataframe.plot(kind='scatter',x = 'Duration', y = 'Calories')
# plt.show()

dataframe['Duration'].plot(kind='hist')
plt.show()
