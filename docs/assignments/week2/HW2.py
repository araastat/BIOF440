# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # BIOF 440 Homework: Week 2
#
# ## Instructions
#
# This homework must be done on a Jupyter notebook, either through JupyterLab or Notebook. The submission will consist of **2 files**; both files are required for complete submission.
#
# 1. The homework will be provided as a `ipynb` file, to be opened in JupyterLab or Jupyter Notebook. This file must be edited to include required code, run within the _biof440_ environment to produce outputs for code, and submitted.
# 1. The final `ipynb` file, after all your work is done, must be converted to a HTML file using `File > Export Notebook As...` in JupyterLab or `File > Download as..` in Jupyter Notebook. Check that this HTML file contains all the outputs required from the assignment. This file needs to be submitted as well.
# 1. Please submit both files using the naming convention `BIOF440_HW2_Lastname.ipynb` and `BIOF440_HW2_Lastname.html`, replacing "Lastname" with your last name/surname/family name.
#
# -----

# %% [markdown]
# For this class, please create a folder named `BIOF440` on your computer where all the material will reside, and within that folder create a sub-folder named `data` where you will store data sets used in class.
#
# All your deliverables should be written in the `BIOF440` folder, so that your code will be consistent with mine in terms of reading data, and will make my life correcting your homework more reasonable. If I have to go through hoops to try and run your notebook to reproduce your homework, I will deduct **5 points** from the homework. To this end, **ensure that you're running the Jupyter notebook using the biof440 environment, so that we don't have issues with packages not being installed**. Reach out on Slack if you have questions.
#
# Each full question is **30 points**. You will get full credit if all the parts are done correctly. Extra credit problems will allow you to have a score of more than 100% for this homework.
#
# ## Question 1
#
# ### 1 (A)
#
# In the following code chunk, import the packages `numpy` and `pandas` using the usual aliases `np` and `pd` respectively.

# %%

# %% [markdown]
# ### 1 (B)
#
# We spoke of the example data sets denoted table1, table2, table3, table4a, table4b and table5 (p. 63 of the pandas slides). All the files are available on Canvas and should be downloaded to the `data` folder described above. Read these 6 files into a dictionary (`dict`) object named `tbl_data`, with keys being the names listed earlier here, and the values being the actual data, using a `for-loop` and `pandas` functions. Show your code below.

# %%

# %% [markdown]
# ### 1 (C)
#
# Write why each of table1, table2, table3, (table4a + table4b) and table5 are or are not tidy, and, if not, how would you transform them to make them tidy.

# %%

# %% [markdown]
# ### 1 (extra credit, 5 points)
#
# Write the Python code below that would transform each of the data sets (or the pair `table4a + table4b`) to be tidy.

# %%

# %% [markdown]
# ## Question 2
#
# ### 2 (A)
#
# Read in to Python the gapminder dataset. Note from the slides how to read it in, since it is tab-delimited. Call it `gapm`

# %%

# %% [markdown]
# ### 2 (B)
#
# We want to create the following plot:
#
# ![](bar1.png)
#
# To create this we need to get our data in shape!
#
# First, find the average life expectancy by continent in 2007. Make sure your result is a `DataFrame` and not a `Series` by appropriate use of `reset_index`.

# %%

# %% [markdown]
# ### 2 (C)
#
# Apply the function `sort_values` to the DataFrame created in 2(B) to re-arrange the rows in increasing order of life expectancy. Use the help features or Google to figure out how to use `sort_values`

# %%

# %% [markdown]
# ## Question 3
#
# ### 3 (A)
#
# Download the files BreastCancer_Clinical.xlsx and BreastCancer_Expression.xlsx from Canvas. Read both of these data into Python, calling them `brca_clin` and `brca_expr`, respectively.

# %%

# %% [markdown]
# ### 3 (B)
#
# Identify the common subject identifier in the two datasets and merge `brca_clin` with `brca_expr` using a left join, calling the result `brca`. To check, this merged dataset should have 108 rows and 41 columns

# %%

# %% [markdown]
# ### 3 (C)
#
# Find the mean expression of the proteins NP_958782 & NP_958785 by ER status.

# %%

# %% [markdown]
# ### 3 (Extra credit, 5 points)
#
# Create a new column in `brca` that equals "HR + " if either ER or PR are positive, "HER2" if HER2 Final Status is positive, and "Triple Neg" if all of ER, PR and HER2 status are negative.

# %%

# %% [markdown]
# ## Extra credit (15 points)
#
# Download weather.csv into your `data` directory. Use a combination of Python data munging (transformation) tools to make this data tidy.

# %%

# %%
# Convert to HTML
import os

os.system("jupyter nbconvert --to html BIOF440_HW2.ipynb")
