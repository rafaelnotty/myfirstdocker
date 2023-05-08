import numpy as np
import pandas as pd

print("Hello, Pandas and NumPy!")

a = np.array([1, 2, 3, 4])
print("NumPy array:", a)

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("Pandas DataFrame:")
print(df.head())
