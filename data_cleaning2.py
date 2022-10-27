import pandas as pd
import glob

files = glob.glob('file*.csv')

df_list = []
for file in files:
    data = pd.read_csv(file)
    df_list.append(data)

people = pd.concat(df_list, ignore_index = True)

# print(people)
# print()
# print("This dataframe is {length} rows long.".format(length = len(people)))
# print()
# print(people.info())

df = pd.read_csv('file1.csv')

df = pd.melt(
    frame = df, # dataframe you want to melt
    id_vars = ['name', 'gender', 'age'], # column(s) of the old df you want to keep
    value_vars = ['old_column1', 'old_column2'], # column(s) of the old df you want to turn into variables
    value_name = 'new_value_column', # new column that stores values
    var_name = 'new_variable_column' # new column that stores what were previously variables
)
df.columns(['Column 1', 'Column 2', 'Column 3'])

# Dealing with Duplicates

duplicates = df.duplicated()
print(duplicates.value_counts())

df = df.drop_duplicates()
duplicates = df.duplicated()
print(duplicates.value_counts())

