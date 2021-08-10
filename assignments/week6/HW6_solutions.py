# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: 'Python 3.7.2 64-bit (''biof440_env'': venv)'
#     name: python3
# ---

# %% [markdown]
# # BIOF 440: Data visualization using Python
# ## Homework 6

# %%
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('seaborn-notebook')
mpl.rc('font', **{'family': 'serif', 'serif': 'Palatino'})

# %% [markdown]
# ## Question 1 (10 points)
#
# We’ll use the data set beaches to fit a linear regression of $\log_{10}$(enterococci) on other variables.
#
# Create a plot of the coefficients and 95% confidence intervals of this model, including a reference line at 0. State which variables and levels are statistically significant. Order the months in chronological order, with January being the reference month. Make the plot publication quality, in that the graph shouldn’t have raw variable names, and should have appropriate titles and axes labels and legends (in English).

# %%
dat = pd.read_csv('data/sydneybeaches3.csv')
dat.head()

# %%
tmp=dat[['month','month_name']].drop_duplicates()
dat['month_name'] = pd.Categorical(dat['month_name'], categories=tmp['month_name']) # This assures the months are in the right order in the table and graph


# %%
mod = smf.ols(formula = "np.log10(enterococci) ~ rainfall + temperature + month_name ", data=dat)
res = mod.fit()


# %%
coefs = res.summary2().tables[1].reset_index().rename(columns = {'index':'variables'})

coefs

# %%
coefs['variables'] = coefs['variables'].str.replace('month_name\[T.','').str.replace('\]', '') # fixes the format of the month coefficients
coefs.query('variables != "Intercept"', inplace=True) # Takes out the row with the intercept
coefs

# %%
import seaborn as sns

fig, ax = plt.subplots()

sns.scatterplot(data=coefs, x = "Coef.", y = "variables", ax = ax)
ax.hlines(
    y = coefs['variables'],
    xmin = coefs['[0.025'],
    xmax = coefs['0.975]']
)
ax.axvline(0, linestyle=':', color='green');
ax.set_title('Model for $\log_{10}$(enterococci): Coefficients & 95% CI');

    

# %% [markdown]
# ## Extra credit
#
# Color the plot according to which variables and levels are significant.

# %%
coefs['indic'] = pd.Categorical(np.where(coefs['P>|t|'] < 0.05, 'signif', 'non-signif'), categories=['non-signif','signif'])

fig, ax = plt.subplots()

sns.scatterplot(data=coefs, x = "Coef.", y = "variables", hue = "indic", ax = ax)
ax.hlines(
    y = coefs['variables'],
    xmin = coefs['[0.025'],
    xmax = coefs['0.975]'],
    colors = np.where(coefs['indic']=='signif', 'red','blue'),
)
ax.axvline(0, linestyle=':', color='green'); # vertical line
ax.set_ylabel("");
ax.set_xlabel('Change in $\log_{10}$(enterococci) per unit change in variable');
ax.set_title('Model for $\log_{10}$(enterococci): Coefficients & 95% CI');
ax.legend(title = "", loc='upper left');
fig.text(0, 0.0001, 'Reference month: January', ha='right'); # location with respect to figure, not axes


# %% [markdown]
# ## Question 2
#
# The file `accidents2019.csv` in the data folder contains aggregate data about the number of traffic accidents with fatalities in the US in 2019, along with the location (Rural/Urban) of the accident and whether drunk driving was involved. In the spirit of the heatmap here, create heatmaps of the percent of accidents occur in rural areas , and what percent of accidents involve drunk driving. Make the plot pretty with proper ordering, legends and titles.

# %%
accidents = pd.read_csv('data/accidents2019.csv')
accidents['Month'] = pd.Categorical(accidents['Month'], # This sets the right order of months
    categories=['January','February','March','April','May','June','July',
        'August','September','October','November', 'December'])
accidents['Drunk'] = accidents.Drunk/accidents.N * 100
accidents['Urban'] = accidents.Urban/accidents.N * 100
accidents.head()

# %%
plot_dat = accidents[['Month','Hour','Drunk']].pivot(index = 'Month',columns = 'Hour')
fig, ax = plt.subplots(figsize = (15, 5))
sns.heatmap(plot_dat, cmap='inferno', ax=ax,
    cbar_kws={'shrink':0.8, 'label': 'Percent'})
ax.set_xlabel('Hour of day');
ax.set_xticklabels(list(range(24)), rotation=0);
ax.set_title('Percent of accidents involving drunk driving', size=16);

# %%
plot_dat = accidents[['Month','Hour','Urban']].pivot(index='Month', columns = 'Hour')

fig, ax = plt.subplots(figsize = (15, 5))
sns.heatmap(plot_dat, cmap='inferno', ax=ax,
    cbar_kws={'shrink':0.8, 'label': 'Percent'})
ax.set_xlabel('Hour of day');
ax.set_xticklabels(list(range(24)), rotation=0);
ax.set_title('Percent of accidents in urban areas', size=16);
