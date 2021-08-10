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
# # Homework 3
#
# This homework is about visualizing data. You will have to fill in the blanks for some of the homework. All code must run and produce the visualizations in each section. This will be checked by running `Kernel > Restart Kernel and Run All Cells` in JupyterLab. To ensure that there aren't issues with packages, make sure your JupyterLab instance is running in the `biof440` environment.
#
# As before, after you finish the homework, export the notebook as a HTML file using `File > Export Notebook As ... > HTML`. You will submit both the ipynb file and the html file.
#
# -----

# %% [markdown]
# ## Visualizing the gapminder data
#
# Load the gapminder data from Canvas and store as `gapm`

# %% [markdown]
# ### Question 1 (25 points)
#
# #### 1 (a)
#
# Plot the life expectancy of Sudan over time using **pandas** plotting using a line plot. The x-axis will be time, and the y-axis will be the life expectancy. Fill in the blanks.

# %%
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline
plt.style.use("seaborn-white")

# %%
gapm = pd.read_csv("data/gapminder.tsv", sep="\t")

gapm[gapm["country"] == ________].plot(
    x=____,
    y=_____,
    kind=_____,
    legend=False,
    xlabel="",
    ylabel="Life expectancy (years)",
    title="Country: Sudan",
)

# %% [markdown]
# #### 1(b)
#
# Now we want to compare the experience in Sudan with the experience of other African countries on the same plot. We will encode the country information as color. We will look at two approaches. In this part, we will try to use **pandas** plotting to achieve this.
#
# The idea will be to create a `DataFrame` with year as the index, and each country's life expectancy as a separate column (call this `africa2`), and then use **pandas** to plot it.

# %%
africa = gapm.query("continent == 'Africa'")
africa.head()

# %%
africa2 = africa[["country", "year", "lifeExp"]].pivot_table(
    index=_____, columns=_______, values=________
)
africa2.head()

# %%
africa2._____(kind=_______, legend=False)

# %% [markdown]
# #### 1 (c)
#
# Now we will do the same plot using **seaborn**. The **seaborn** package works with tidy (long) data and can encode unique values of a variable to colors, shapes, and sizes. So we do not need to reshape the data.

# %%
sns.relplot(
    data=africa, x="year", y="lifeExp", ____=________, kind="line", legend=False
)

# %% [markdown]
# #### 1 (d)
#
# Well, we did it for one continent. Let's do a grid of plots (facets), one for each continent.
#
# We want to have a grid of plots in 2 columns. Each plot will represent one continent. That plot will have the pattern of life expectancy over time with one colored line for each country in the continent.

# %%
sns.relplot(
    data=gapm,
    x="year",
    y="lifeExp",
    kind="line",
    _____=_______,
    _______=________,
    ______=________,
    legend=False,
)

# %% [markdown]
# #### 1 (e)
#
# Let's do a small amount of customization. We will change the x-axis labels to blank, and the y-axis labels to describe what is being encoded there, in English. It cannot be the variable name.
#
# To do this, we first have to save the plot to a variable name (say, `g`), and then manipulate the plot using some available functions

# %%
g = sns.relplot(
    data=gapm,
    x="year",
    y="lifeExp",
    kind="line",
    hue="country",
    col="continent",
    col_wrap=2,
    legend=False,
)
# From (d)
g.set_xlabels(_______)
g.set_ylabels(_______)

# %% [markdown]
# #### 1 Extra credit (10 points)
#
# Customize the graph to reproduce the following visualization. You can use information available [here](https://towardsdatascience.com/texts-fonts-and-annotations-with-pythons-matplotlib-dfbdea19fc57) and [here](https://stackoverflow.com/questions/43920341/python-seaborn-facetgrid-change-titles) and [here](https://stackoverflow.com/questions/29813694/how-to-add-a-title-to-seaborn-facet-plot).

# %%

# %% [markdown] tags=[]
# ### Question 2 (15 points)
#
# This question will use the `diamonds` data that you can load via **seaborn**. You can learn about the dataset [here](https://www.rdocumentation.org/packages/ggplot2/versions/3.3.3/topics/diamonds).
#
# For this question you can use **pandas** plotting, **seaborn** and/or **matplotlib** to create the visualizations.

# %%
diamonds = sns.load_dataset("diamonds")
diamonds.head()

# %% [markdown]
# #### 2 (a)
#
# Construct a frequency bar graph for the variable _clarity_, with bars in order of frequency, from lowest to highest frequency.

# %%

# %% [markdown]
# #### 2(b)
#
# Plot the frequency bar graph with bars in order from best clarity to worst clarity (see documentation in link above to know what that order is)

# %%

# %% [markdown]
# #### 2(c)
#
# Visualize the distribution of the size of diamonds in carats over different cuts using boxplots

# %%

# %% [markdown]
# #### 2 extra credit (5 points)
#
# Use the example [here](https://seaborn.pydata.org/examples/kde_ridgeplot.html) to recreate the following plot that uses the diamonds dataset. The density plot is of _carat_ and the groups are _cut_. It's not an exact copy of the linked example, so figure out what pieces you need and what needs to be adjusted. Use the documentation to understand each option.

# %%

# %%
