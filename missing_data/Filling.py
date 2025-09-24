from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [3, 6.5, 3.],
                     [4, 7.5, 7.],
                     [5, 2.5, 3.],
                     [NA, NA, NA]
                     ])
print(data)
print("-"*10)
cleaned=data.fillna(data.mean()) #dung trung vi thi median
print(cleaned)

