'''
# Amazon top 50 bestselling books

Source : [Kaggle.io](https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019)

Dataset contains for each year from 2009 to 2019, the Top 50 best-selling books for that respective year. 
There are a total of 550 entries.

## Objective: Perform Exploratory Data Analysis

__Index__

1. Data Import and Initial Overview

'''

#%% Packages
import numpy
import pandas
from matplotlib import pyplot as plt
import seaborn

seaborn.set_style('darkgrid')

#%% 1. Data Import and Initial Overview

#%%% 1.1 Import
books = pandas.read_csv('books.csv')
books.head(10)

#%%% 1.2 Basic Overview
print(books.info())  # basic info

print("Missing Observations: \n", books.isnull().sum())

print("Duplicate Entries: \n", books.duplicated().sum())

print("Shape of DataFrame: ", books.shape)

print("Variable names: ", list(books.columns))

numerical_var = ['User Rating','Reviews','Price','Year']
text_var = ['Name','Author','Genre']

#%% 1.3 Overview of Variables
books.describe()

# distribution of Genre
table = books.loc[:, 'Genre'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(x = table, autopct = "%1.1f%%")
plt.legend(labels=table.index)
plt.title("Distribution of Genre")
plt.show()

# distrbution of Genre over time
table = books.groupby(['Year','Genre']).aggregate({'Year':'count'})
table.rename(columns={'Year':'Year','Genre':'Genre','Year':'Count'}, inplace = True)
table.head()

plt.figure(figsize = (15,6))
seaborn.relplot(data = table, x = 'Year', y = 'Count', hue = 'Genre', kind = 'line')
plt.title('Distribution of genre over time')
plt.show()

# distrbution of price

plt.figure(figsize = (8,6))
seaborn.displot(data = books, x = 'Price', hue = 'Year', kind = 'kde')
plt.show()

plt.figure(figsize = (8,6))
seaborn.displot(data = books, x = 'Price', hue = 'Genre', kind = 'kde')
plt.show()

plt.figure(figsize = (8,6))
seaborn.relplot(data = books, x = 'Year', y = 'Price', kind = 'line')
plt.show()

plt.figure(figsize = (8,6))
seaborn.relplot(data = books, x = 'Year', y = 'Price', hue = 'Genre', kind = 'line')
plt.show()

# Books and Authors

table = books['Name'].value_counts()
table = table.head(10)
table

plt.figure(figsize = (8,6))
plt.barh(y = table.index, width = table.values)
plt.xlabel('Number of Years book has been on Best-Selling list')
plt.show()

table = books['Author'].value_counts()
table = table.head(25)
table

plt.figure(figsize = (12,8))
plt.barh(y = table.index, width = table.values)
plt.xlabel('Number of times Auhor has been on Best-Selling list')
plt.show()