import pandas as pd

raw_data = pd.read_csv("Menu.csv")
print(raw_data)
print(raw_data.info())
numberOfItems = len(raw_data)
sorted_data = raw_data.sort_values("Menu",ascending=True)
print(f'#1 -> Count:{numberOfItems}')
print(f'#2 {sorted_data}')