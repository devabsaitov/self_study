import pandas as pd


data = pd.read_excel('example1.xlsx')

for i in data.values:
    print(i)
