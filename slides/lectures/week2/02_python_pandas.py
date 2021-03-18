# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] toc=true
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Starting-pandas" data-toc-modified-id="Starting-pandas-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Starting pandas</a></span></li><li><span><a href="#Data-import-and-export" data-toc-modified-id="Data-import-and-export-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Data import and export</a></span></li><li><span><a href="#Exploring-a-data-set" data-toc-modified-id="Exploring-a-data-set-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Exploring a data set</a></span></li><li><span><a href="#Data-structures-and-types" data-toc-modified-id="Data-structures-and-types-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Data structures and types</a></span><ul class="toc-item"><li><span><a href="#pandas.Series" data-toc-modified-id="pandas.Series-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>pandas.Series</a></span></li><li><span><a href="#pandas.DataFrame" data-toc-modified-id="pandas.DataFrame-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>pandas.DataFrame</a></span><ul class="toc-item"><li><span><a href="#Creating-a-DataFrame" data-toc-modified-id="Creating-a-DataFrame-5.2.1"><span class="toc-item-num">5.2.1&nbsp;&nbsp;</span>Creating a DataFrame</a></span></li><li><span><a href="#Working-with-a-DataFrame" data-toc-modified-id="Working-with-a-DataFrame-5.2.2"><span class="toc-item-num">5.2.2&nbsp;&nbsp;</span>Working with a DataFrame</a></span></li><li><span><a href="#Extracting-rows-and-columns" data-toc-modified-id="Extracting-rows-and-columns-5.2.3"><span class="toc-item-num">5.2.3&nbsp;&nbsp;</span>Extracting rows and columns</a></span></li><li><span><a href="#Boolean-selection" data-toc-modified-id="Boolean-selection-5.2.4"><span class="toc-item-num">5.2.4&nbsp;&nbsp;</span>Boolean selection</a></span></li><li><span><a href="#query" data-toc-modified-id="query-5.2.5"><span class="toc-item-num">5.2.5&nbsp;&nbsp;</span><code>query</code></a></span></li><li><span><a href="#Replacing-values-in-a-DataFrame" data-toc-modified-id="Replacing-values-in-a-DataFrame-5.2.6"><span class="toc-item-num">5.2.6&nbsp;&nbsp;</span>Replacing values in a DataFrame</a></span></li></ul></li><li><span><a href="#Categorical-data" data-toc-modified-id="Categorical-data-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Categorical data</a></span><ul class="toc-item"><li><span><a href="#Re-organizing-categories" data-toc-modified-id="Re-organizing-categories-5.3.1"><span class="toc-item-num">5.3.1&nbsp;&nbsp;</span>Re-organizing categories</a></span></li></ul></li><li><span><a href="#Missing-data" data-toc-modified-id="Missing-data-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Missing data</a></span></li></ul></li><li><span><a href="#Data-transformation" data-toc-modified-id="Data-transformation-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Data transformation</a></span><ul class="toc-item"><li><span><a href="#Arithmetic-operations" data-toc-modified-id="Arithmetic-operations-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Arithmetic operations</a></span></li><li><span><a href="#Concatenation-of-data-sets" data-toc-modified-id="Concatenation-of-data-sets-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Concatenation of data sets</a></span><ul class="toc-item"><li><span><a href="#Adding-columns" data-toc-modified-id="Adding-columns-6.2.1"><span class="toc-item-num">6.2.1&nbsp;&nbsp;</span>Adding columns</a></span></li></ul></li><li><span><a href="#Merging-data-sets" data-toc-modified-id="Merging-data-sets-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Merging data sets</a></span></li><li><span><a href="#Tidy-data-principles-and-reshaping-datasets" data-toc-modified-id="Tidy-data-principles-and-reshaping-datasets-6.4"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Tidy data principles and reshaping datasets</a></span></li><li><span><a href="#Melting-(unpivoting)-data" data-toc-modified-id="Melting-(unpivoting)-data-6.5"><span class="toc-item-num">6.5&nbsp;&nbsp;</span>Melting (unpivoting) data</a></span></li><li><span><a href="#Separating-columns-containing-multiple-variables" data-toc-modified-id="Separating-columns-containing-multiple-variables-6.6"><span class="toc-item-num">6.6&nbsp;&nbsp;</span>Separating columns containing multiple variables</a></span></li><li><span><a href="#Pivot/spread-datasets" data-toc-modified-id="Pivot/spread-datasets-6.7"><span class="toc-item-num">6.7&nbsp;&nbsp;</span>Pivot/spread datasets</a></span></li></ul></li><li><span><a href="#Data-aggregation-and-split-apply-combine" data-toc-modified-id="Data-aggregation-and-split-apply-combine-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Data aggregation and split-apply-combine</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Transformation" data-toc-modified-id="Transformation-7.0.1"><span class="toc-item-num">7.0.1&nbsp;&nbsp;</span>Transformation</a></span></li><li><span><a href="#Filter" data-toc-modified-id="Filter-7.0.2"><span class="toc-item-num">7.0.2&nbsp;&nbsp;</span>Filter</a></span></li></ul></li></ul></li></ul></div>

# %% [markdown]
# # Pandas
#
# ## Introduction
#
# `pandas` is the Python Data Analysis package. It allows for data ingestion, transformation and cleaning, and creates objects that can then be passed on to analytic packages like `statsmodels` and `scikit-learn` for modeling and packages like `matplotlib`, `seaborn`, and `plotly` for visualization. 
#
# `pandas` is built on top of numpy, so many numpy functions are commonly used in manipulating `pandas` objects. 
#
# > `pandas` is a pretty extensive package, and we'll only be able to cover some of its features. For more details, there is free online documentation at [pandas.pydata.org](https://pandas.pydata.org). You can also look at the book ["Python for Data Analysis (2nd edition)"](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython-dp-1491957662/dp/1491957662/) by Wes McKinney, the original developer of the pandas package, for more details.
#
# ## Starting pandas
#
# As with any Python module, you have to "activate" `pandas` by using `import`. The "standard" alias for `pandas` is `pd`. We will also import `numpy`, since `pandas` uses some `numpy` functions in the workflows. 

# %% name="02-python-pandas-2"
import numpy as np
import pandas as pd
# %% [markdown]
# ## Data import and export
#
# Most data sets you will work with are set up in tables, so are rectangular in shape. Think Excel spreadsheets. In `pandas` the structure that will hold this kind of data is a `DataFrame`.  We can read external data into a `DataFrame` using one of many `read_*` functions. We can also write from a `DataFrame` to a variety of formats using `to_*` functions. The most common of these are listed below:
#
# | Format type | Description | reader       | writer     |
# | ----------- | ----------- | ------------ | ---------- |
# | text        | CSV         | read_csv     | to_csv     |
# |             | Excel       | read_excel   | to_excel   |
# | text        | JSON        | read_json    | to_json    |
# | binary      | Feather     | read_feather | to_feather |
# | binary      | SAS         | read_sas     |            |
# | SQL         | SQL         | read_sql     | to_sql     |
#
# We'll start by reading in the `mtcars` dataset stored as a CSV file

# %% name="02-python-pandas-3"
pd.read_csv('data/mtcars.csv')

# %% [markdown]
# This just prints out the data, but then it's lost. To use this data, we have to give it a name, so it's stored in Python's memory

# %% name="02-python-pandas-4"
mtcars = pd.read_csv('data/mtcars.csv')

# %% [markdown]
# > One of the big differences between a spreadsheet program and a programming language from the data science perspective is that you have to load data into the programming language. It's not "just there" like Excel. This is a good thing, since it allows the common functionality of the programming language to work across multiple data sets, and also keeps the original data set pristine. Excel users can run into problems and [corrupt their data](https://nature.berkeley.edu/garbelottoat/?p=1488) if they are not careful.
#
# If we wanted to write this data set back out into an Excel file, say, we could do

# %% name="02-python-pandas-5"
mtcars.to_excel('data/mtcars.xlsx')

# %% [markdown]
# > You may get an error if you don't have the `openpyxl` package installed. You can easily install it from the Anaconda prompt using `conda install openpyxl` and following the prompts. 
#

# %% [markdown]
# ## Exploring a data set
#
# We would like to get some idea about this data set. There are a bunch of functions linked to the `DataFrame` object that help us in this. First we will use `head` to see the first 8 rows of this data set

# %% name="02-python-pandas-6"
mtcars.head(8)
# %% [markdown]
# This is our first look into this data. We notice a few things. Each column has a name, and each row has an *index*, starting at 0. 
#
# > If you're interested in the last N rows, there is a corresponding `tail` function
#
# Let's look at the data types of each of the columns

# %% name="02-python-pandas-7"
mtcars.dtypes

# %% [markdown]
# This tells us that some of the variables, like `mpg` and `disp`, are floating point (decimal) numbers, several are integers, and `make` is an "object". The `dtypes` function borrows from `numpy`, where there isn't really a type for character or categorical variables. So most often, when you see "object" in the output of `dtypes`, you think it's a character or categorical variable. 
#
# We can also look at the data structure in a bit more detail.

# %% name="02-python-pandas-8"
mtcars.info()

# %% [markdown]
# This tells us that this is indeed a `DataFrame`, wth 12 columns, each with 32 valid observations. Each row has an index value ranging from 0 to 11. We also get the approximate size of this object in memory.
#
# You can also quickly find the number of rows and columns of a data set by using `shape`, which is borrowed from numpy.

# %% name="02-python-pandas-9"
mtcars.shape

# %% [markdown]
# More generally, we can get a summary of each variable using the `describe` function

# %% name="02-python-pandas-10"
mtcars.describe()
# %% [markdown]
# These are usually the first steps in exploring the data.

# %% [markdown]
# ## Data structures and types
#
# pandas has two main data types: `Series` and `DataFrame`. These are analogous to vectors and matrices, in that a `Series` is 1-dimensional while a `DataFrame` is 2-dimensional. 
#
# ### pandas.Series
#
# The `Series` object holds data from a single input variable, and is required, much like numpy arrays, to be homogeneous in type. You can create `Series` objects from lists or numpy arrays quite easily

# %% name="02-python-pandas-11"
s = pd.Series([1,3,5,np.nan, 9, 13])
s

# %% name="02-python-pandas-12"
s2 = pd.Series(np.arange(1,20))
s2
# %% [markdown]
# You can access elements of a `Series` much like a `dict`

# %% name="02-python-pandas-13"
s2[4]

# %% [markdown]
# There is no requirement that the index of a `Series` has to be numeric. It can be any kind of scalar object

# %% name="02-python-pandas-14"
s3 = pd.Series(np.random.normal(0,1, (5,)), index = ['a','b','c','d','e'])
s3

# %% name="02-python-pandas-15"
s3['d']

# %% name="02-python-pandas-16"
s3['a':'d']

# %% [markdown]
# Well, slicing worked, but it gave us something different than expected. It gave us both the start **and** end of the slice, which is unlike what we've encountered so far!! 
#
# It turns out that in `pandas`, slicing by index actually does this. It is a discrepancy from `numpy` and Python in general that we have to be careful about. 

# %% [markdown]
# You can extract the actual values into a numpy array

# %% name="02-python-pandas-17"
s3.to_numpy()

# %% [markdown]
# In fact, you'll see that much of `pandas`' structures are build on top of `numpy` arrays. This is a good thing, since you can take advantage of the powerful numpy functions that are built for fast, efficient scientific computing. 

# %% [markdown]
# Making the point about slicing again, 

# %% name="02-python-pandas-18"
s3.to_numpy()[0:3]

# %% [markdown]
# This is different from index-based slicing done earlier.

# %% [markdown]
# ### pandas.DataFrame
#
# The `DataFrame` object holds a rectangular data set. Each column of a `DataFrame` is a `Series` object. This means that each column of a `DataFrame` must be comprised of data of the same type, but different columns can hold data of different types. This structure is extremely useful in practical data science. The invention of this structure was, in my opinion, transformative in making Python an effective data science tool.

# %% [markdown]
# #### Creating a DataFrame
#
# The `DataFrame` can be created by importing data, as we saw in the previous section. It can also be created by a few methods within Python.
#
# First, it can be created from a 2-dimensional `numpy` array.

# %% name="02-python-pandas-19"
rng = np.random.RandomState(25)
d1 = pd.DataFrame(rng.normal(0,1, (4,5)))
d1

# %% [markdown]
# You will notice that it creates default column names, that are merely the column number, starting from 0. We can also create the column names and row index (similar to the `Series` index we saw earlier) directly during creation.

# %% name="02-python-pandas-20"
d2 = pd.DataFrame(rng.normal(0,1, (4, 5)), 
                  columns = ['A','B','C','D','E'], 
                  index = ['a','b','c','d'])
d2

# %% [markdown]
# > We could also create a `DataFrame` from a list of lists, as long as things line up, just as we showed for `numpy` arrays. However, to me, other ways, including the `dict` method below, make more sense.

# %% [markdown]
# We can change the column names (which can be extracted and replaced with the `columns` attribute) and the index values (using the `index` attribute).

# %% name="02-python-pandas-21"
d2.columns

# %% name="02-python-pandas-22"
d2.columns = pd.Index(['V'+str(i) for i in range(1,6)]) # Index creates the right objects for both column names and row names, which can be extracted and changed with the `index` attribute
d2

# %% [markdown]
# **Exercise:** Can you explain what I did in the list comprehension above? The key points are understanding `str` and how I constructed the `range`.

# %% name="02-python-pandas-23"
d2.index = ['o1','o2','o3','o4']
d2

# %% [markdown]
# You can also extract data from a homogeneous `DataFrame` to a `numpy` array

# %% name="02-python-pandas-24"
d1.to_numpy()

# %% [markdown]
# > It turns out that you can use `to_numpy` for a non-homogeneous `DataFrame` as well. `numpy` just makes it homogeneous by assigning each column the data type `object`. This also limits what you can do in `numpy` with the array and may require changing data types using the [`astype` function](https://numpy.org/devdocs/reference/generated/numpy.ndarray.astype.html). There is some more detail about the `object` data type in the Python Tools for Data Science ([notebook](01_python_tools_ds.ipynb#object), [PDF](01_python_tools_ds.pdf)) document.

# %% [markdown]
# The other easy way to create a `DataFrame` is from a `dict` object, where each component object is either a list or a numpy array, and is homogeneous in type. One exception is if a component is of size 1; then it is repeated to meet the needs of the `DataFrame`'s dimensions

# %% name="02-python-pandas-25"
df = pd.DataFrame({
    'A':3.,
    'B':rng.random_sample(5),
    'C': pd.Timestamp('20200512'),
    'D': np.array([6] * 5),
    'E': pd.Categorical(['yes','no','no','yes','no']),
    'F': 'NIH'})
df

# %% name="02-python-pandas-26"
df.info()

# %% [markdown]
# We note that C is a date object, E is a category object, and F is a text/string object. pandas has excellent time series capabilities (having origins in FinTech), and the `TimeStamp` function creates datetime objects which can be queried and manipulated in Python. We'll describe category data in the next section.

# %% [markdown]
# You can also create a `DataFrame` where each column is composed of composite objects, like lists and dicts, as well. This might have limited value in some settings, but may be useful in others. In particular, this allows capabilities like the [*list-column* construct in R tibbles](https://jennybc.github.io/purrr-tutorial/ls13_list-columns.html). For example, 

# %% name="02-python-pandas-27"
pd.DataFrame({'list' :[[1,2],[3,4],[5,6]],
             'tuple' : [('a','b'), ('c','d'), ('e','f')],
              'set' : [{'A','B','C'}, {'D','E'}, {'F'}], 
            'dicts' : [{'A': [1,2,3]}, {'B':[5,6,8]}, {'C': [3,9]}]})

# %% [markdown]
# #### Working with a DataFrame
#
# You can extract particular columns of a `DataFrame` by name

# %% name="02-python-pandas-28"
df['E']

# %% name="02-python-pandas-29"
df['B']

# %% [markdown]
# > There is also a shortcut for accessing single columns, using Python's dot (`.`) notation.

# %% name="02-python-pandas-30"
df.B

# %% [markdown]
# > This notation can be more convenient if we need to perform operations on a single column. If we want to extract multiple columns, this notation will not work. Also, if we want to create new columns or replace existing columns, we need to use the array notation with the column name in quotes. 

# %% [markdown]
# Let's look at slicing a `DataFrame`
#
# #### Extracting rows and columns
#
# There are two extractor functions in `pandas`:
#
# + `loc` extracts by label (index label, column label, slice of labels, etc.
# + `iloc` extracts by index (integers, slice objects, etc.
#

# %% name="02-python-pandas-31"
df2 = pd.DataFrame(rng.randint(0,10, (5,4)), 
                  index = ['a','b','c','d','e'],
                  columns = ['one','two','three','four'])
df2

# %% [markdown]
# First, let's see what naively slicing this `DataFrame` does.

# %% name="02-python-pandas-32"
df2['one']

# %% [markdown]
# Ok, that works. It grabs one column from the dataset. How about the dot notation?

# %% name="02-python-pandas-33"
df2.one

# %% [markdown]
# Let's see what this produces.

# %% name="02-python-pandas-34"
type(df2.one)

# %% [markdown]
# So this is a series, so we can potentially do slicing of this series.

# %% name="02-python-pandas-35"
df2.one['b']

# %% name="02-python-pandas-36"
df2.one['b':'d']

# %% name="02-python-pandas-37"
df2.one[:3]

# %% [markdown]
# Ok, so we have all the `Series` slicing available. The problem here is in semantics, in that we are grabbing one column and then slicing the rows. That doesn't quite work with our sense that a `DataFrame` is a rectangle with rows and columns, and we tend to think of rows, then columns. 
#
# Let's see if we can do column slicing with this. 

# %% name="02-python-pandas-38"
df2[:'two']

# %% [markdown]
# That's not what we want, of course. It's giving back the entire data frame. We'll come back to this.

# %% name="02-python-pandas-39"
df2[['one','three']]

# %% [markdown]
# That works correctly though. We can give a list of column names. Ok. 
#
# How about row slices?

# %% name="02-python-pandas-40"
#df2['a'] # Doesn't work
df2['a':'c'] 

# %% [markdown]
# Ok, that works. It slices rows, but includes the largest index, like a `Series` but unlike `numpy` arrays. 

# %% name="02-python-pandas-41"
df2[0:2]

# %% [markdown]
# Slices by location work too, but use the `numpy` slicing rules. 

# %% [markdown]
# This entire extraction method becomes confusing. Let's simplify things for this, and then move on to more consistent ways to extract elements of a `DataFrame`. Let's agree on two things. If we're going the direct extraction route, 
#
# 1. We will extract single columns of a `DataFrame` with `[]` or `.`, i.e., `df2['one']` or `df2.one`
# 1. We will extract slices of rows of a `DataFrame` using location only, i.e., `df2[:3]`. 
#
# For everything else, we'll use two functions, `loc` and `iloc`.
#
# + `loc` extracts elements like a matrix, using index and columns
# + `iloc` extracts elements like a matrix, using location

# %% name="02-python-pandas-42"
df2.loc[:,'one':'three']

# %% name="02-python-pandas-43"
df2.loc['a':'d',:]

# %% name="02-python-pandas-44"
df2.loc['b', 'three']

# %% [markdown]
# So `loc` works just like a matrix, but with `pandas` slicing rules (include largest index)

# %% name="02-python-pandas-45"
df2.iloc[:,1:4]

# %% name="02-python-pandas-46"
df2.iloc[1:3,:]

# %% name="02-python-pandas-47"
df2.iloc[1:3, 1:4]

# %% [markdown]
# `iloc` slices like a matrix, but uses `numpy` slicing conventions (does **not** include highest index)
#
# If we want to extract a single element from a dataset, there are two functions available, `iat` and `at`, with behavior corresponding to `iloc` and `loc`, respectively.

# %%
df2.iat[2,3]

# %%
df2.at['b','three']


# %% [markdown]
# #### Boolean selection
#
# We can also use tests to extract data from a `DataFrame`. For example, we can extract only rows where column labeled `one` is greater than 3. 

# %% name="02-python-pandas-48"
df2[df2.one > 3]

# %% [markdown]
# We can also do composite tests. Here we ask for rows where `one` is greater than 3 and `three` is less than 9

# %% name="02-python-pandas-49"
df2[(df2.one > 3) & (df2.three < 9)]

# %% [markdown]
# #### `query`
#
# `DataFrame`'s have a `query` method allowing selection using a Python expression

# %% name="02-python-pandas-50"
n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns = list('abc'))
df

# %% name="02-python-pandas-51"
df[(df.a < df.b) & (df.b < df.c)]

# %% [markdown]
# We can equivalently write this query as 

# %% name="02-python-pandas-52"
df.query('(a < b) & (b < c)')


# %% [markdown]
# #### Replacing values in a DataFrame
#
# We can replace values within a DataFrame either by position or using a query. 

# %%
df2

# %%
df2['one'] = [2,5,2,5,2]
df2

# %%
df2.iat[2,3] = -9 # missing value
df2

# %% [markdown]
# Let's now replace values using `replace` which is more flexible. 

# %%
df2.replace(0, -9) # replace 0 with -9

# %%
df2.replace({2: 2.5, 8: 6.5}) # multiple replacements

# %%
df2.replace({'one': {5: 500}, 'three': {0: -9, 8: 800}}) 
# different replacements in different columns

# %% [markdown]
# See more examples in the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html?highlight=replace#pandas.DataFrame.replace)

# %% [markdown]
# ### Categorical data
#
# `pandas` provides a `Categorical` function and a `category` object type to Python. This type is analogous to the `factor` data type in R. It is meant to address categorical or discrete variables, where we need to use them in analyses. Categorical variables typically take on a small number of unique values, like gender, blood type, country of origin, race, etc. 
#
# You can create categorical `Series` in a couple of ways:

# %% name="02-python-pandas-53"
s = pd.Series(['a','b','c'], dtype='category')

# %% name="02-python-pandas-54"
df = pd.DataFrame({
    'A':3.,
    'B':rng.random_sample(5),
    'C': pd.Timestamp('20200512'),
    'D': np.array([6] * 5),
    'E': pd.Categorical(['yes','no','no','yes','no']),
    'F': 'NIH'})
df['F'].astype('category')

# %% [markdown]
# You can also create `DataFrame`'s where each column is categorical

# %% name="02-python-pandas-55"
df = pd.DataFrame({'A': list('abcd'), 'B': list('bdca')})
df_cat = df.astype('category')
df_cat.dtypes

# %% [markdown]
# You can explore categorical data in a variety of ways

# %% name="02-python-pandas-56"
df_cat['A'].describe()

# %% name="02-python-pandas-57"
df['A'].value_counts()

# %% [markdown]
# One issue with categories is that, if a particular level of a category is not seen before, it can create an error. So you can pre-specify the categories you expect

# %% name="02-python-pandas-58"
df_cat['B'] = pd.Categorical(list('aabb'), categories = ['a','b','c','d'])
df_cat['B'].value_counts()

# %% [markdown]
# #### Re-organizing categories
#
# In categorical data, there is often the concept of a "first" or "reference" category, and an ordering of categories. This tends to be important in both visualization as well as in regression modeling. Both aspects of a category can be addressed using the `reorder_categories` function.
#
# In our earlier example, we can see that the `A` variable has 4 categories, with the "first" category being "a".

# %%
df_cat.A

# %% [markdown]
# Suppose we want to change this ordering to the reverse ordering, where
# "d" is the "first" category, and then it goes in reverse order. 

# %%
df_cat['A'] = df_cat.A.cat.reorder_categories(['d','c','b','a'])
df_cat.A

# %% [markdown]
# ### Missing data
#
# Both `numpy` and `pandas` allow for missing values, which are a reality in data science. The missing values are coded as `np.nan`. Let's create some data and force some missing values

# %% name="02-python-pandas-59"
df = pd.DataFrame(np.random.randn(5, 3), index = ['a','c','e', 'f','g'], columns = ['one','two','three']) # pre-specify index and column names
df['four'] = 20 # add a column named "four", which will all be 20
df['five'] = df['one'] > 0
df

# %% name="02-python-pandas-60"
df2 = df.reindex(['a','b','c','d','e','f','g'])
df2.style.applymap(lambda x: 'background-color:yellow', subset = pd.IndexSlice[['b','d'],:])

# %% [markdown]
# The code above is creating new blank rows based on the new index values, some of which are present in the existing data and some of which are missing.
#
# We can create *masks* of the data indicating where missing values reside in a data set.

# %% name="02-python-pandas-61"
df2.isna()

# %% name="02-python-pandas-62"
df2['one'].notna()

# %% [markdown]
# We can obtain complete data by dropping any row that has any missing value. This is called *complete case analysis*, and you should be very careful using it. It is *only* valid if we belive that the missingness is missing at random, and not related to some characteristic of the data or the data gathering process. 

# %% name="02-python-pandas-63"
df2.dropna(how='any')

# %% [markdown]
# You can also fill in, or *impute*, missing values. This can be done using a single value..

# %% name="02-python-pandas-64"
out1 = df2.fillna(value = 5)

out1.style.applymap(lambda x: 'background-color:yellow', subset = pd.IndexSlice[['b','d'],:])

# %% [markdown]
# or a computed value like a column mean

# %% name="02-python-pandas-65"
df3 = df2.copy()
df3 = df3.select_dtypes(exclude=[object])   # remove non-numeric columns
out2 = df3.fillna(df3.mean())  # df3.mean() computes column-wise means

out2.style.applymap(lambda x: 'background-color:yellow', subset = pd.IndexSlice[['b','d'],:])

# %% [markdown]
# You can also impute based on the principle of *last value carried forward* which is common in time series. This means that the missing value is imputed with the previous recorded value. 

# %% name="02-python-pandas-66"
out3 = df2.fillna(method = 'ffill') # Fill forward

out3.style.applymap(lambda x: 'background-color:yellow', subset = pd.IndexSlice[['b','d'],:])

# %% name="02-python-pandas-67"
out4 = df2.fillna(method = 'bfill') # Fill backward

out4.style.applymap(lambda x: 'background-color:yellow', subset = pd.IndexSlice[['b','d'],:])

# %% [markdown]
# ## Data transformation
#
# ### Arithmetic operations
#
# If you have a `Series` or `DataFrame` that is all numeric, you can add or multiply single numbers to all the elements together.

# %% name="02-python-pandas-68"
A = pd.DataFrame(np.random.randn(4,5))
print(A)

# %% name="02-python-pandas-69"
print(A + 6)

# %% name="02-python-pandas-70"
print(A * -10)

# %% [markdown]
# If you have two compatible (same dimension) numeric `DataFrame`s, you can add, subtract, multiply and divide elementwise

# %% name="02-python-pandas-71"
B = pd.DataFrame(np.random.randn(4,5) + 4)
print(A + B)

# %% name="02-python-pandas-72"
print(A * B)

# %% [markdown]
# If you have a `Series` with the same number of elements as the number of columns of a `DataFrame`, you can do arithmetic operations, with each element of the `Series` acting upon each column of the `DataFrame`

# %% name="02-python-pandas-73"
c = pd.Series([1,2,3,4,5])
print(A + c)

# %% name="02-python-pandas-74"
print(A * c)
# %% [markdown]
# This idea can be used to standardize a dataset, i.e. make each column have mean 0 and standard deviation 1.

# %% name="02-python-pandas-75"
means = A.mean(axis=0)
stds = A.std(axis = 0)

(A - means)/stds

# %% [markdown]
# ### Concatenation of data sets
#
# Let's create some example data sets

# %% name="02-python-pandas-76"
df1 = pd.DataFrame({'A': ['a'+str(i) for i in range(4)],
    'B': ['b'+str(i) for i in range(4)],
    'C': ['c'+str(i) for i in range(4)],
    'D': ['d'+str(i) for i in range(4)]})

df2 =  pd.DataFrame({'A': ['a'+str(i) for i in range(4,8)],
    'B': ['b'+str(i) for i in range(4,8)],
    'C': ['c'+str(i) for i in range(4,8)],
    'D': ['d'+str(i) for i in range(4,8)]})
df3 =  pd.DataFrame({'A': ['a'+str(i) for i in range(8,12)],
    'B': ['b'+str(i) for i in range(8,12)],
    'C': ['c'+str(i) for i in range(8,12)],
    'D': ['d'+str(i) for i in range(8,12)]})

# %% [markdown]
# We can concatenate these `DataFrame` objects by row

# %% name="02-python-pandas-77"
row_concatenate = pd.concat([df1, df2, df3])
print(row_concatenate)

# %% [markdown]
# This stacks the dataframes together. They are literally stacked, as is evidenced by the index values being repeated. 

# %% [markdown]
# This same exercise can be done by the `append` function

# %% name="02-python-pandas-78"
df1.append(df2).append(df3)

# %% [markdown]
# Suppose we want to append a new row to `df1`. Lets create a new row.

# %% name="02-python-pandas-79"
new_row = pd.Series(['n1','n2','n3','n4'])
pd.concat([df1, new_row])

# %% [markdown]
# That's a lot of missing values. The issue is that the we don't have column names in the `new_row`, and the indices are the same, so pandas tries to append it my making a new column. The solution is to make it a `DataFrame`.

# %% name="02-python-pandas-80"
new_row = pd.DataFrame([['n1','n2','n3','n4']], columns = ['A','B','C','D'])
print(new_row)

# %% name="02-python-pandas-81"
pd.concat([df1, new_row])

# %% [markdown]
# or

# %% name="02-python-pandas-82"
df1.append(new_row)

# %% [markdown]
# #### Adding columns

# %% name="02-python-pandas-83"
pd.concat([df1,df2,df3], axis = 1)

# %% [markdown]
# The option `axis=1` ensures that concatenation happens by columns. The default value `axis = 0` concatenates by rows.

# %% [markdown]
# Let's play a little game. Let's change the column names of `df2` and `df3` so they are not the same as `df1`.

# %% name="02-python-pandas-84"
df2.columns = ['E','F','G','H']
df3.columns = ['A','D','F','H']
pd.concat([df1,df2,df3])

# %% [markdown]
# Now pandas ensures that all column names are represented in the new data frame, but with missing values where the row indices and column indices are mismatched. Some of this can be avoided by only joining on common columns. This is done using the `join` option ir `concat`. The default value is 'outer`, which is what you see. above

# %% name="02-python-pandas-85"
pd.concat([df1, df3], join = 'inner')

# %% [markdown]
# You can do the same thing when joining by rows, using `axis = 0` and `join="inner"` to only join on rows with matching indices. Reminder that the indices are just labels and happen to be the row numbers by default. 

# %% [markdown]
# ### Merging data sets

# %% [markdown]
# For this section we'll use a set of data from a survey, also used by Daniel Chen in "Pandas for Everyone"

# %% name="02-python-pandas-86"
person = pd.read_csv('data/survey_person.csv')
site = pd.read_csv('data/survey_site.csv')
survey = pd.read_csv('data/survey_survey.csv')
visited = pd.read_csv('data/survey_visited.csv')

# %% name="02-python-pandas-87"
print(person)

# %% name="02-python-pandas-88"
print(site)

# %% name="02-python-pandas-89"
print(survey)

# %% name="02-python-pandas-90"
print(visited)

# %% [markdown]
# There are basically four kinds of joins:
#
# | pandas | R          | SQL         | Description                     |
# | ------ | ---------- | ----------- | ------------------------------- |
# | left   | left_join  | left outer  | keep all rows on left           |
# | right  | right_join | right outer | keep all rows on right          |
# | outer  | outer_join | full outer  | keep all rows from both         |
# | inner  | inner_join | inner       | keep only rows with common keys |

# %% [markdown]
# ![](graphs/joins.png)
#
# The terms `left` and `right` refer to which data set you call first and second respectively. 
#
# We start with an left join
#

# %% name="02-python-pandas-91"
s2v_merge = survey.merge(visited, left_on = 'taken',right_on = 'ident', how = 'left')

# %% name="02-python-pandas-92"
print(s2v_merge)

# %% [markdown]
# Here, the left dataset is `survey` and the right one is `visited`. Since we're doing a left join, we keed all the rows from `survey` and add columns from `visited`, matching on the common key, called "taken" in one dataset and "ident" in the other. Note that the rows of `visited` are repeated as needed to line up with all the rows with common "taken" values. 
#
# We can now add location information, where the common key is the site code

# %% name="02-python-pandas-93"
s2v2loc_merge = s2v_merge.merge(site, how = 'left', left_on = 'site', right_on = 'name')
print(s2v2loc_merge)

# %% [markdown]
# Lastly, we add the person information to this dataset.

# %% name="02-python-pandas-94"
merged = s2v2loc_merge.merge(person, how = 'left', left_on = 'person', right_on = 'ident')
print(merged.head())

# %% [markdown]
# You can merge based on multiple columns as long as they match up. 

# %% name="02-python-pandas-95"
ps = person.merge(survey, left_on = 'ident', right_on = 'person')
vs = visited.merge(survey, left_on = 'ident', right_on = 'taken')
print(ps)

# %% name="02-python-pandas-96"
print(vs)

# %% name="02-python-pandas-97"
ps_vs = ps.merge(vs, 
                left_on = ['ident','taken', 'quant','reading'],
                right_on = ['person','ident','quant','reading']) # The keys need to correspond
ps_vs.head()

# %% [markdown]
# Note that since there are common column names, the merge appends `_x` and `_y` to denote which column came from the left and right, respectively.
#

# %% [markdown]
# ### Tidy data principles and reshaping datasets
#
# The tidy data principle is a principle espoused by Dr. Hadley Wickham, one of the foremost R developers. [Tidy data](http://vita.had.co.nz/papers/tidy-data.pdf) is a structure for datasets to make them more easily analyzed on computers. The basic principles are
#
# + Each row is an observation
# + Each column is a variable
# + Each type of observational unit forms a table
#
# > Tidy data is tidy in one way. Untidy data can be untidy in many ways
#
# Let's look at some examples.

# %% name="02-python-pandas-98"
from glob import glob
filenames = sorted(glob('data/table*.csv')) # find files matching pattern. I know there are 6 of them
table1, table2, table3, table4a, table4b, table5 = [pd.read_csv(f) for f in filenames] # Use a list comprehension

# %% [markdown]
# This code imports data from 6 files matching a pattern. Python allows multiple assignments on the left of the `=`, and as each dataset is imported, it gets assigned in order to the variables on the left. In the second line I sort the file names so that they match the order in which I'm storing them in the 3rd line. The function `glob` does pattern-matching of file names. 
#
# The following tables refer to the number of TB cases and population in Afghanistan, Brazil and China in 1999 and 2000

# %% name="02-python-pandas-99"
print(table1)

# %% name="02-python-pandas-100"
print(table2)
# %% name="02-python-pandas-101"
print(table3)

# %% name="02-python-pandas-102"
print(table4a) # cases

# %% name="02-python-pandas-103"
print(table4b) # population

# %% name="02-python-pandas-104"
print(table5)

# %% [markdown]
# **Exercise:** Describe why and why not each of these datasets are tidy.

# %% [markdown]
# ### Melting (unpivoting) data
#
# Melting is the operation of collapsing multiple columns into 2 columns, where one column is formed by the old column names, and the other by the corresponding values. Some columns may be kept fixed and their data are repeated to maintain the interrelationships between the variables.
#
# We'll start with loading some data on income and religion in the US from the Pew Research Center.

# %% name="02-python-pandas-105"
pew = pd.read_csv('data/pew.csv')
print(pew.head())

# %% [markdown]
# This dataset is considered in "wide" format. There are several issues with it, including the fact that column headers have data. Those column headers are income groups, that should be a column by tidy principles. Our job is to turn this dataset into "long" format with a column for income group. 
#
# We will use the function `melt` to achieve this. This takes a few parameters:
#
# + **id_vars** is a list of variables that will remain as is
# + **value_vars** is a list of column nmaes that we will melt (or unpivot). By default, it will melt all columns not mentioned in id_vars
# + **var_name** is a string giving the name of the new column created by the headers (default: `variable`)
# + **value_name** is a string giving the name of the new column created by the values (default: `value`)
#

# %% name="02-python-pandas-106"
pew_long = pew.melt(id_vars = ['religion'], var_name = 'income_group', value_name = 'count')
print(pew_long.head())

# %% [markdown]
# ### Separating columns containing multiple variables
#
# We will use an Ebola dataset to illustrate this principle

# %% name="02-python-pandas-107"
ebola = pd.read_csv('data/country_timeseries.csv')
print(ebola.head())

# %% [markdown]
# Note that for each country we have two columns -- one for cases (number infected) and one for deaths. Ideally we want one column for country, one for cases and one for deaths. 
#
# The first step will be to melt this data sets so that the column headers in question from a column and the corresponding data forms a second column.

# %% name="02-python-pandas-108"
ebola_long = ebola.melt(id_vars = ['Date','Day'])
print(ebola_long.head())

# %% [markdown]
# We now need to split the data in the `variable` column to make two columns. One will contain the country name and the other either Cases or Deaths. We will use some string manipulation functions that we will see later to achieve this.

# %% name="02-python-pandas-109"
variable_split = ebola_long['variable'].str.split('_', expand=True) # split on the `_` character
print(variable_split[:5])

# %% [markdown]
# The `expand=True` option forces the creation of an `DataFrame` rather than a list

# %% name="02-python-pandas-110"
type(variable_split)

# %% [markdown]
# We can now concatenate this to the original data

# %% name="02-python-pandas-111"
variable_split.columns = ['status','country']

ebola_parsed = pd.concat([ebola_long, variable_split], axis = 1)

ebola_parsed.drop('variable', axis = 1, inplace=True) # Remove the column named "variable" and replace the old data with the new one in the same location

print(ebola_parsed.head())

# %% [markdown]
# ### Pivot/spread datasets
#
# If we wanted to, we could also make two columns based on cases and deaths, so for each country and date you could easily read off the cases and deaths. This is achieved using the `pivot_table` function.
#
# In the `pivot_table` syntax, `index` refers to the columns we don't want to change, `columns` refers to the column whose values will form the column names of the new columns, and `values` is the name of the column that will form the values in the pivoted dataset. 

# %% name="02-python-pandas-112"
ebola_parsed.pivot_table(index = ['Date','Day', 'country'], columns = 'status', values = 'value')

# %% [markdown]
# This creates something called `MultiIndex` in the `pandas` `DataFrame`. This is useful in some advanced cases, but here, we just want a normal `DataFrame` back. We can achieve that by using the `reset_index` function.

# %% name="02-python-pandas-113"
ebola_parsed.pivot_table(index = ['Date','Day','country'], columns = 'status', values = 'value').reset_index()

# %% [markdown]
# Pivoting is a 2-column to many-column operation, with the number of columns formed depending on the number of unique values present in the column of the original data that is entered into the `columns` argument of `pivot_table`

# %% [markdown]
# **Exercise:** Load the file `weather.csv` into Python and work on making it a tidy dataset. It requires melting and pivoting. The dataset comprises of the maximun and minimum temperatures recorded each day in 2010. There are lots of missing value. Ultimately we want columns for days of the month, maximum temperature and minimum tempearture along with the location ID, the year and the month.

# %% [markdown]
# ## Data aggregation and split-apply-combine
#
# We'll use the Gapminder dataset for this section

# %% name="02-python-pandas-114"
df = pd.read_csv('data/gapminder.tsv', sep = '\t') # data is tab-separated, so we use `\t` to specify that
# %% [markdown]
# The paradigm we will be exploring is often called *split-apply-combine* or MapReduce or grouped aggregation. The basic idea is that you split a data set up by some feature, apply a recipe to each piece, compute the result, and then put the results back together into a dataset. This can be described in teh following schematic.

# %% [markdown]
# ![](graphs/split-apply-combine.png)

# %% [markdown]
# `pandas` is set up for this. It features the `groupby` function that allows the "split" part of the operation. We can then apply a function to each part and put it back together. Let's see how.

# %% name="02-python-pandas-115"
df.head()

# %% name="02-python-pandas-116"
f"This dataset has {len(df['country'].unique())} countries in it"

# %% [markdown]
# One of the variables in this dataset is life expectancy at birth, `lifeExp`. Suppose we want to find the average life expectancy of each country over the period of study.

# %% name="02-python-pandas-117"
df.groupby('country')['lifeExp'].mean()

# %% [markdown]
# So what's going on here? First, we use the `groupby` function, telling `pandas` to split the dataset up by values of the column `country`.

# %% name="02-python-pandas-118"
df.groupby('country')

# %% [markdown]
# `pandas` won't show you the actual data, but will tell you that it is a grouped dataframe object. This means that each element of this object is a `DataFrame` with data from one country.

# %% name="02-python-pandas-119"
df.groupby('country').ngroups

# %% name="02-python-pandas-120"
df.groupby('country').get_group('United Kingdom')

# %% name="02-python-pandas-121"
type(df.groupby('country').get_group('United Kingdom'))

# %% name="02-python-pandas-122"
avg_lifeexp_country = df.groupby('country').lifeExp.mean()
avg_lifeexp_country['United Kingdom']

# %% name="02-python-pandas-123"
df.groupby('country').get_group('United Kingdom').lifeExp.mean()

# %% [markdown]
# Let's look at if life expectancy has gone up over time, by continent

# %% name="02-python-pandas-124"
df.groupby(['continent','year']).lifeExp.mean()

# %% name="02-python-pandas-125"
avg_lifeexp_continent_yr = df.groupby(['continent','year']).lifeExp.mean().reset_index()
avg_lifeexp_continent_yr

# %% name="02-python-pandas-126"
type(avg_lifeexp_continent_yr)

# %% [markdown]
# The aggregation function, in this case `mean`, does both the "apply" and "combine" parts of the process.

# %% [markdown]
# We can do quick aggregations with `pandas`

# %% name="02-python-pandas-127"
df.groupby('continent').lifeExp.describe()

# %% name="02-python-pandas-128"
df.groupby('continent').nth(10) # Tenth observation in each group

# %% [markdown]
# You can also use functions from other modules, or your own functions in this aggregation work.

# %% name="02-python-pandas-129"
df.groupby('continent').lifeExp.agg(np.mean)


# %% name="02-python-pandas-130"
def my_mean(values):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return(sum/n)

df.groupby('continent').lifeExp.agg(my_mean)

# %% [markdown]
# You can do many functions at once

# %% name="02-python-pandas-131"
df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])

# %% [markdown]
# You can also aggregate on different columns at the same time by passing a `dict` to the `agg` function

# %% name="02-python-pandas-132"
df.groupby('year').agg({'lifeExp': np.mean,'pop': np.median,'gdpPercap': np.median}).reset_index()


# %% [markdown]
# #### Transformation

# %% [markdown]
# You can do grouped transformations using this same method. We will compute the z-score for each year, i.e. we will substract the average life expectancy and divide by the standard deviation

# %% name="02-python-pandas-133"
def my_zscore(values):
    m = np.mean(values)
    s = np.std(values)
    return((values - m)/s)


# %% name="02-python-pandas-134"
df.groupby('year').lifeExp.transform(my_zscore)

# %% name="02-python-pandas-135"
df['lifeExp_z'] = df.groupby('year').lifeExp.transform(my_zscore)

# %% name="02-python-pandas-136"
df.groupby('year').lifeExp_z.mean()

# %% [markdown]
# #### Filter

# %% [markdown]
# We can split the dataset by values of one variable, and filter out those splits that fail some criterion. The following code only keeps countries with a population of at least 10 million at some point during the study period

# %% name="02-python-pandas-137"
df.groupby('country').filter(lambda d: d['pop'].max() > 10000000)
# %% [markdown]
#
#
#
#
#
#
#
