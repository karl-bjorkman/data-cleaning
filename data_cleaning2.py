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

# Restructuring untidy table

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

# Split by index (e.g. splits 'birthdate' into 'month', 'day', and 'year')

df['column1'] = df.old_col.str[0:2]
df['column2'] = df.old_col.str[2:4]
df['column3'] = df.old_col.str[4:]

# Split by character (e.g. splits 'full_name' into 'first_name' and 'last_name')

str_split = df.column.str.split('_')
df['column1'] = str_split.str.get(0)
df['column2'] = str_split.str.get(1)

# String parsing using Regex

df.column = df.column.replace('[\$]', '', regex = True) # Removes dollar signs from price column
df.column = pd.to_numeric(df.column) # ...then converts price strings to ints or floats

df.column = df.column.str.split('(\d+)', expand = True)[1] # Extract numbers from a string using Regex
df.column = pd.to_numeric(df.column) # ...then convert to ints or floats in order to use them for operations

# Missing values

#1: Drop all rows with missing value
df = df.dropna()
df = df.dropna(subset = ['column1'])

#2: Fill missing values with the mean of the column, or with some aggregate value
df = df.fillna(value = {'col1': df.col1.mean(), 'col2': df.col2.mean()})

# Data deletion

df.dropna(inplace = True) # listwise deletion
df.dropna(subset = ['col1', 'col2'], inplace = True, how = 'any') # pairwise deletion