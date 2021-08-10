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
# For this class, please create a folder named `BIOF440` on your computer where all the material will reside, and within that folder create a sub-folder named `data` where you will store data sets used in class. All your deliverables should be written in the `BIOF440` folder, so that your code will be consistent with mine in terms of reading data, and will make my life correcting your homework more reasonable. If I have to go through hoops to try and run your notebook to reproduce your homework, I will deduct **5 points** from the homework. To this end, **ensure that you're running the Jupyter notebook using the biof440 environment, so that we don't have issues with packages not being installed**.
#
# Each full question is **30 points**. You will get full credit if all the parts are done correctly. Extra credit problems will allow you to have a score of more than 100% for this homework.
#
# ## Question 1
#
# ### 1 (A)
#
# In the following code chunk, import the packages `numpy` and `pandas` using the usual aliases `np` and `pd` respectively.

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ### 1 (B)
#
# We spoke of the example data sets denoted table1, table2, table3, table4a, table4b and table5 (p. 63 of the pandas slides). All the files are available on Canvas and should be downloaded to the `data` folder described above. Read these 6 files into a dictionary (`dict`) object named `tbl_data`, with keys being the names listed earlier here, and the values being the actual data, using a `for-loop` and `pandas` functions. Show your code below.

# %%
tbl_data = {}
fnames = ["table1", "table2", "table3", "table4a", "table4b", "table5"]
for f in fnames:
    tbl_data[f] = pd.read_csv("data/" + f + ".csv")
tbl_data

# %% [markdown]
# ### 1 (C)
#
# Write why each of table1, table2, table3, (table4a + table4b) and table5 are or are not tidy, and, if not, how would you transform them to make them tidy.

# %% [markdown]
# table1 is tidy
#
# table2 is not tidy since the column `type` contains 2 kinds of data
#
# table3 is not tidy, since the `rate` column is a composite column with both cases and population, as a string
#
# tables 4a and 4b aren't tidy, since the year data are column headers
#
# table5 is nto tidy, since, like table3, the `rate` column is composite, and `century` and `year` can be combined into just year

# %% [markdown]
# ### 1 (extra credit, 5 points)
#
# Write the Python code below that would transform each of the data sets (or the pair `table4a + table4b`) to be tidy.

# %%
# Convert table2
pd.pivot_table(
    tbl_data["table2"], index=["country", "year"], columns="type", values="count"
).reset_index()

# %%
tbl_data["table3"]
var_split = tbl_data["table3"]["rate"].str.split("/", expand=True)
var_split.columns = ["cases", "population"]
var_split = var_split.astype(int)
pd.concat([tbl_data["table3"], var_split], axis=1).drop(["rate"], axis=1)

# %%
d1 = tbl_data["table4a"].melt(id_vars="country", var_name="year", value_name="cases")
d2 = tbl_data["table4b"].melt(
    id_vars="country", var_name="year", value_name="population"
)
pd.merge(d1, d2, left_on=["country", "year"], right_on=["country", "year"])

# %%
d = tbl_data["table5"].copy()
d["year"] = [str(x) + str(y).zfill(2) for x, y in zip(d["century"], d["year"])]
d1 = (
    d["rate"]
    .str.split("/", expand=True)
    .astype(int)
    .set_axis(["cases", "population"], axis=1)
)
d = pd.concat([d, d1], axis=1).drop(["century", "rate"], axis=1)
d

# %% [markdown]
# ## Question 2
#
# ### 2 (A)
#
# Read in to Python the gapminder dataset. Note from the slides how to read it in, since it is tab-delimited. Call it `gapm`

# %%
gapm = pd.read_csv("data/gapminder.tsv", sep="\t")

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
gapm2 = gapm[gapm.year == 2007].groupby("continent")["lifeExp"].mean().reset_index()
gapm2

# %% [markdown]
# ### 2 (C)
#
# Apply the function `sort_values` to the DataFrame created in 2(B) to re-arrange the rows in increasing order of life expectancy. Use the help features or Google to figure out how to use `sort_values`

# %%
gapm2 = gapm2.sort_values("lifeExp")
gapm2

# %% [markdown]
# ## Question 3
#
# ### 3 (A)
#
# Download the files BreastCancer_Clinical.xlsx and BreastCancer_Expression.xlsx from Canvas. Read both of these data into Python, calling them `brca_clin` and `brca_expr`, respectively.

# %%
brca_clin = pd.read_excel("data/BreastCancer_Clinical.xlsx")
brca_expr = pd.read_excel("data/BreastCancer_Expression.xlsx")

# %% [markdown]
# ### 3 (B)
#
# Identify the common subject identifier in the two datasets and merge `brca_clin` with `brca_expr` using a left join, calling the result `brca`. To check, this merged dataset should have 108 rows and 41 columns

# %%
brca = brca_clin.merge(
    brca_expr, left_on="Complete TCGA ID", right_on="TCGA_ID", how="left"
)
print(f"brca has {brca.shape[0]} rows and {brca.shape[1]} columns")
brca.head()

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
pd.merge(
    brca_clin, brca_expr, how="left", left_on="Complete TCGA ID", right_on="TCGA_ID"
)

# %% [markdown]
# ### 3 (C)
#
# Find the mean expression of the proteins NP_958782 & NP_958785 by ER status.

# %%
brca.groupby("ER Status")[["NP_958782", "NP_958785"]].mean()

# %% [markdown]
# ### 3 (Extra credit, 5 points)
#
# Create a new column `Status` in `brca` that equals "HR + " if either ER or PR are positive, "HER2" if HER2 Final Status is positive, and "Triple Neg" if all of ER, PR and HER2 status are negative, and 'Other' otherwise.

# %%
d = pd.Series("Other", brca.index)  # Initialize Series with same number of rows as brca
d[(brca["ER Status"] == "Positive") | (brca["PR Status"] == "Positive")] = "HR +"
d[brca["HER2 Final Status"] == "Positive"] = "HER2"
d[
    (brca["ER Status"] == "Negative")
    & (brca["PR Status"] == "Negative")
    & (brca["HER2 Final Status"] == "Negative")
] = "Triple Neg"
brca["Status"] = d
brca.head()

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
brca["new_col"] = np.where(
    ((brca["ER Status"] == "Positive") | (brca["ER Status"] == "Positive")), "HR+", 0
)
brca["new_col"] = np.where(
    (brca["HER2 Final Status"] == "Positive"), "HR2", brca["new_col"]
)
brca["new_col"] = np.where(
    (
        (brca["ER Status"] == "Negative")
        & (brca["ER Status"] == "Negative")
        & (brca["HER2 Final Status"] == "Negative")
    ),
    "Triple Neg",
    brca["new_col"],
)

brca["new_col"].value_counts()

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
brca["Status"].value_counts()

# %% [markdown]
# ## Extra credit (15 points)
#
# Download weather.csv into your `data` directory. Use a combination of Python data munging (transformation) tools to make this data tidy.

# %%
weather = pd.read_csv("data/weather.csv")
weather = weather.melt(
    id_vars=["id", "year", "month", "element"],
    var_name="variable",
    value_name="rainfall",
)
weather["day"] = weather["variable"].str.replace("d", "").astype(int)
weather.drop("variable", axis=1)
weather = weather.pivot_table(
    index=["id", "year", "month", "day"], columns="element", values="rainfall"
)
weather = weather.reset_index()
weather = weather.sort_values(["year", "month", "day"], axis=0)

weather.columns.name = None
weather

# %%
import os

os.system("jupyter nbconvert --to html BIOF440_HW2_Solution.ipynb")

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
weather = pd.read_csv("data/weather.csv")
weather_MX17004_2010_tmax = weather[weather["element"] == "tmax"]
weather_MX17004_2010_tmin = weather[weather["element"] == "tmin"]
# Drop columns summarized in DF name as they are invariant.
weather_MX17004_2010_tmax.drop(columns=["id", "year", "element"], inplace=True)
weather_MX17004_2010_tmin.drop(columns=["id", "year", "element"], inplace=True)
# Now transpose the data so imputation is within months.
weather_MX17004_2010_tmax_transposed = weather_MX17004_2010_tmax.T
weather_MX17004_2010_tmin_transposed = weather_MX17004_2010_tmin.T
#
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="median")
weather_MX17004_2010_tmax_transposed_imputed_array = imputer.fit_transform(
    weather_MX17004_2010_tmax_transposed
)
weather_MX17004_2010_tmin_transposed_imputed_array = imputer.fit_transform(
    weather_MX17004_2010_tmin_transposed
)
weather_MX17004_2010_tmin_transposed_imputed_df = pd.DataFrame(
    weather_MX17004_2010_tmin_transposed_imputed_array
)
weather_MX17004_2010_tmax_transposed_imputed_df = pd.DataFrame(
    weather_MX17004_2010_tmax_transposed_imputed_array
)

headers = weather_MX17004_2010_tmin_transposed_imputed_df.iloc[0]
tmin_df = pd.DataFrame(
    weather_MX17004_2010_tmin_transposed_imputed_df.values[1:], columns=headers
)
tmin_df.index.name = "day"

headers = weather_MX17004_2010_tmax_transposed_imputed_df.iloc[0]
tmax_df = pd.DataFrame(
    weather_MX17004_2010_tmax_transposed_imputed_df.values[1:], columns=headers
)
tmax_df.index.name = "day"


# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
tmax_df

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
from glob import glob

filenames = sorted(glob("data/table*.csv"))
tbl_data = dict(
    zip(
        [i.replace("data/", "").replace(".csv", "") for i in filenames],
        [pd.read_csv(f) for f in filenames],
    )
)

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
tbl_data


# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
def add_HR(row):
    if row["ER Status"] == "Positive":
        return "HR+"
    if row["PR Status"] == "Positive":
        return "HR+"
    if row["HER2 Final Status"] == "Positive":
        return "HER2"
    return "Triple Neg"


brca["HR"] = brca.apply(lambda row: add_HR(row), axis=1)

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
brca["HR"].value_counts()

# %% jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
