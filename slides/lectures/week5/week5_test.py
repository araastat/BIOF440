# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: title,-all
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

# %% [markdown]
# # Survival plots in Python
#
# ## Survival data
#
# Survival, or time-to-event, data is common data in biomedical research
#
# We follow subjects over time, and stop either when an event, like death, occurs, or when we stop the study or the subject leaves the study (censoring)
#
# So the response we record are 
#
# 1. The time to event or censoring, whichever is earlier
# 1. Whether we obseverd the event (1) or the subject was censored (0)
#
# For survival data, we need to install the _lifelines_ and _kaplanmeier_ packages
#
# > You can open the Anaconda console (Win) or a terminal (Mac) and type the following code
# > ```
# > conda activate biof440
# > conda install -c conda-forge lifelines
# > pip install kaplanmeier
# >```
#
# ## The Python setup

# %% Setup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import lifelines as lfl #<<
import kaplanmeier as km #<<
imgdir = 'img'

from IPython.display import IFrame
# %%

# ## Visualizing survival data
# 
# We will first look at the nature of survival data through a visualization. 
#
# We will use some sample data from the _kaplanmeier_ package
#
# %% Example km code

df = km.example_data()
time_event = df['time'] # Time to event
censoring = df['Died'] # Whether subject died (1) or was censored (2)
labx = df['group'] # a grouping variable

# %%

# ## Visualizing survival data
#
# We can plot the subjects' over time, indicating who died (red) and who were censored (blue)
#
# The _lifelines_ package in Python provides most tools for looking at survival data
#
# %%
ax = lfl.plotting.plot_lifetimes(time_event, censoring,
    event_observed_color='red', event_censored_color='blue',
    sort_by_duration=True)
ax.set_xlabel('Time')
ax.vlines(1000, 0,200,linestyles='--');
plt.show()
# %%

# ## Survival data
# 
# You could look at survival summaries based on this plot, to see how many people died by a certain time
#
# However, to look overall at the survival pattern for this group, we have to account for censoring
#
# The standard way of doing this is using a Kaplan-Meier curve
#
# ## Kaplan Meier curve in Python
#
# We can compute and plot the Kaplan Meier curve using either the _kaplanmeier_ package or the _lifelines_ package.
#
# ## Kaplan-Meier curve using _kaplanmeier_
#
# This plot includes a table that tells you how many subjects are at risk, how many are dead,
# and how many are censored at a select set of time points
# %% Plotting
out = km.fit(time_event, censoring, labx) # Direct grouped lines
km.plot(out)

# %% [markdown]
# # Kaplan-Meier curve using _lifelines_
#
# We can have greater control over the KM curve using the _lifelines_ package. This package follows the 
# coding style of packages like _scikit-learn_ in that we first start a fitting object, then we 
# fit the model to the data and then plot it
#
# This plotting uses a matplotlib backend
# %% lifelines

from lifelines import KaplanMeierFitter 

kmf = KaplanMeierFitter() # Kaplan Meier fitting object
kmf.fit(time_event, event_observed=censoring) # Fit model to data

kmf.plot(at_risk_counts=False) # No table at first
plt.title('Kaplan-Meier Curve')
plt.show();

# %% [markdown]
# # Kaplan-Meier curve using _lifelines_
#
# We can clean this curve up a bit.

# %% Kaplan-Meier via lifelines
ax = kmf.plot()
ax.set_xlabel('days')
ax.set_ylabel('Probability of survival')
ax.get_legend().remove()
ax.set_title('Kaplan-Meier estimates')
plt.show();

# %% [markdown]
#
# ## Kaplan-Meier curve using _lifelines
#
# We can also add the table of deaths below the curve.

# %% Adding tables

ax = kmf.plot( at_risk_counts=True, legend=False)
ax.set_label('days')
ax.set_ylabel('Probability of survival')
plt.show();

# %% [markdown]
#
# ## Kaplan-Meier curve using _lifelines
#
# We can also add the table of deaths below the curve, even in grouped data

# %% Grouped km using lifelines
from lifelines.plotting import add_at_risk_counts

T1 = df.query('group==1')['time']
T2 = df.query('group==2')['time']

C1 = df.query('group==1')['Died']
C2 = df.query('group==2')['Died']

fig, ax = plt.subplots()
kmf1 = KaplanMeierFitter()
kmf1.fit(T1, C1,label='Group 1',)
kmf2 = KaplanMeierFitter()
kmf2.fit(T2, C2,label = 'Group 2',)

ax = kmf1.plot_survival_function(ax = ax,  ci_show=False)
ax = kmf2.plot_survival_function(ax = ax, 
    label = 'Group 2', ci_show=False)
add_at_risk_counts(kmf1, kmf2, ax=ax)

plt.tight_layout();
# %% [markdown]
# ## Kaplan-Meier curve using _lifelines_
#
# We can also format the axes to show percentages rather than proportions. 
#
# We'll demo this with a single KM curve
# %%
import matplotlib.ticker as mtick

ax = kmf.plot()
ax.set_xlabel('days')
ax.set_ylabel('Probability of survival')
ax.get_legend().remove()
ax.set_title('Kaplan-Meier estimates')
fmt = "%0.0f%%"
ticks = mtick.PercentFormatter(xmax=1, 
    symbol='%', 
    decimals=None) # formats axis as percents
ax.yaxis.set_major_formatter(ticks)
ax.set_ylabel('Percent survived');

plt.tight_layout();


