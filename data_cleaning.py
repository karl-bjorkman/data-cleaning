import numpy as np
import pandas as pd

watchlist = pd.read_csv('watchlist.csv')
print(watchlist.head(10))

# DATA WRANGLING
print(watchlist.shape)

# Preliminary Cleaning
watchlist = watchlist.drop_duplicates()

watchlist.columns = map(str.lower, watchlist.columns) # converts all column names to lowercase

watchlist.rename(columns = {'letterboxd uri': 'url'}, inplace = True)

#print(watchlist.dtypes)
#print(watchlist.nunique())

# Missing Data
#print(watchlist.isna().sum())

#print(watchlist.head(20))

#watchlist.year = watchlist.year.where(watchlist.year.isna(), np.nan)
print(watchlist.isna().sum())
print(watchlist[watchlist.year.isna()]) # reveals what rows/observations contain 'NaN' in the 'year' column

pd.crosstab(
    watchlist.name,
    watchlist.year.isna(),
    rownames = ['name'],
    colnames = ['year is na']
)

watchlist.url = watchlist.url.str.lstrip('https://') # remove prefixes with 'left strip'
#print(watchlist.head(10))

# Tidy Data
watchlist = watchlist.melt(

) # restructures columns and values