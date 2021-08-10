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
# ## Homework 4
#
# The COVID-19 pandemic has affected the entire world. Inspired by this page (Links to an external site.) in the Financial Times, we'll create some dynamic visualizations using the covid2021.csv data.
#
# 1. Death trajectories
#     
#     a. Compute the top 10 countries in terms of total deaths from COVID-19. 
#
#     b. Use Plotly to plot the trajectory of daily deaths over time for these countries
#     
#     c. Use Plotly to plot the trajectory of cumulative deaths over time for these countries
#
# 2. per-capita death trajectories
#     
#     a. Compute the top 10 countries in terms of per-capita deaths from COVID-19
#
#     b. Use Altair to plot the trajectory of the cumulative per-capita deaths over time for these countries
#
# 3. (Extra credit) Plot the trajectories of cumulative deaths over time for the top 30 countries in terms of total deaths. Add tooltips to show the country and the per-capita death rate at any time point, when the mouse is hovered over the point. 
#
# Each part is worth 5 points
#
# ------
#

# %%
import pandas as pd
import plotly.express as px
import altair



# %%
dat = pd.read_csv('covid2021.csv')
dat.head()

# %% [markdown]
# ### Question 1a

# %%
top10 = dat.groupby('country')['cases'].sum().nlargest(10)
top10

# %% [markdown]
# ### Question 1b

# %%
top10_data = dat[dat['country'].map(lambda x: x in top10.index)] # Keep data from top10 countries
top10_data.country.value_counts() # verify

# %%
fig = px.line(top10_data, x='date', y = 'cases', color = 'country', template='none', 
    category_orders={'country':top10.index},
    labels = {'cases':'Daily cases', 'date':'', 'country':'Country'})
fig.update_traces(opacity=0.3)
fig.write_html('covid1.html')
fig.show(renderer='notebook_connected')

# %%
# %%HTML
<iframe width='100%' height="350" src='covid1.html'></iframe>

# %% [markdown]
# Note the peaks and valleys. This is mainly because case counts aren't reported on the weekends, and the full weekend count is reported on Mondays

# %% [markdown]
# ### Question 1c

# %%
plotdat_cumsum = (top10_data
    .groupby(['country','date'])['cases'].sum()
    .groupby(level=0).cumsum().reset_index()
)
fig = px.line(plotdat_cumsum, x = 'date',y = 'cases', color = 'country',
    template = 'none', category_orders={'country': top10.index},
    labels = {'date':"", "cases": "COVID-19 cases", "country":"Country"})
fig.write_html('covid2.html')
fig.show()

# %%
# %%HTML
<iframe width="100%" height="350" src='covid2.html'></iframe>

# %% [markdown]
# ### Question 2a

# %%
popln = dat[['country','population']].drop_duplicates().set_index('country')
cases = dat.groupby('country')['cases'].sum().reset_index().set_index('country')
cases.head()
dat_percap = pd.merge(cases, popln, left_index=True, right_index=True)
dat_percap['percap'] = dat_percap.cases/dat_percap.population * 100000 # per 100K
top10_percap = dat_percap.nlargest(10, 'percap')
top10_percap

# %% [markdown]
# ### Question 2b

# %%
dat_percap = dat[dat['country'].apply(lambda x: x in top10_percap.index)]
plotdat_percap = (dat_percap
    .groupby(['country','date','population'])['cases'].sum()
    .groupby(level=0).cumsum().reset_index()
    .assign(percap = lambda d: d['cases']/d['population']*100000)
)


# %%
altair.Chart(plotdat_percap).mark_line().encode(
    altair.X('date:T',title=''),
    altair.Y('percap:Q',title='Deaths per capita'),
    color = altair.Color('country', sort = list(top10_percap.index))
)

# %% [markdown]
# ### Extra credit

# %%
top30_deaths = dat.groupby('country')['cases'].sum().nlargest(30)

top30_data = dat[dat['country'].map(lambda x: x in top30_deaths.index)]
plotdat_top30 = (top30_data
    .groupby(['country','date','population'])['cases'].sum()
    .groupby(level=0).cumsum().reset_index()
    .assign(percap = lambda d: d['cases']/d['population']*100000)
)
plotdat_top30.head()

fig = px.line(plotdat_top30, x = 'date', y = 'percap', color = 'country',
    template = 'none', category_orders={'country': top30_deaths.index},
    labels = {'percap': "Deaths per 100K", 'date':'', 'country': 'Country'})
fig.write_html('covid3.html')
fig.show()

# %%
# %%HTML
<iframe src="covid3.html" width="100%" height="350"></iframe>
