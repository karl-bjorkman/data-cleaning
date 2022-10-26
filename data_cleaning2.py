import pandas as pd
import glob

files = glob.glob('file*.csv')

df_list = []
for file in files:
    data = pd.read_csv(file)
    df_list.append(data)

people = pd.concat(df_list, ignore_index = True)

print(people)
print()
print("This dataframe is {length} rows long.".format(length = len(people)))
print()
print(people.info())