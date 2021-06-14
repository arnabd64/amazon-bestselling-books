# Amazon Top 50 best selling books - Exploratory Data Analysis

The dataset is obtained from [Kaggle](https://kaggle.com), to import the dataset onto your jupyter notebook or other environment, use the github link: https://raw.githubusercontent.com/arnabd64/amazon-bestselling-books/main/books.csv

### For importing in Python

```python
df = pandas.read_csv('https://raw.githubusercontent.com/arnabd64/amazon-bestselling-books/main/books.csv')
```

### For importing in R

```r
df <- read.csv('https://raw.githubusercontent.com/arnabd64/amazon-bestselling-books/main/books.csv')
```

## About

This dataset contains the Top 50 best-selling books from Amazon.com for every year from 2009 to 2019. Thus there are 550 entries. Fortunately there are __No missing data__ or __Duplicate entries__ in the dataset. There are 7 variables in total

| Variable    | Data Type | Description                                   |
|:----------- |:--------- | --------------------------------------------- |
| Name        | string    | Name of the Book                              |
| Author      | string    | Name of the Author                            |
| User Rating | float     | Average rating out of 5                       |
| Reviews     | integer   | Total number of reviews for the book          |
| Price       | integer   | Price of the book in USD                      |
| Year        | integer   | Year in which it was on Best Selling category |
| Genre       | string    | Genre of the Book (Fiction or Non-Fiction)    |

My objective is to perform __Exploratory Data Analysis__ using the basic packages available to us. In python, I used `pandas`, `matplotlib` and `seaborn` packages. All the work is done using Jupyter Notebook with python 3.9. The output file is a `.ipynb` which is easily viewable on Github.
