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
# ## Homework 5
#
# 1. Using the dataset clinical_data_breast_cancer_modified.xlsx available in the data folder, create graphs showing Kaplan-Meier curves of Overall Survival (OS) stratified by (a) ER status, and (b) Node status. Add tables of at-risk individuals and deaths at different times, as in the lecture. Ensure that legends and axes are properly labelled (10 + 10 points)
# 2. The USArrests.csv file in the data folder provides data on murder, assault and rapes per 100,000 people, as well as the percent of the population in a state who live in urban areas. Using the plotly package, create choropleth maps of the USA, where each state is colored based on the data in the 4 columns of this data set. You should create 4 maps, one per column. Ensure that each visualization is properly labeled. (4 x 10 points)
# 3. Extra credit (15 points)
# Choose one of the columns in the USArrests.csv data, and create a choropleth using Folium, including tooltips that will provide information about the data on hovering over a state with the mouse.
#
# ------

# %%
# %%HTML
<script src="require.js"></script>


# %% [markdown]
# ## Question 1a

# %%
import pandas as pd
import lifelines
import kaplanmeier as km

dat = pd.read_csv("data/clinical_data_breast_cancer_modified.csv")
dat.head()

# %%
grp = dat['ER Status']
os_time = dat["OS Time"]
os_cens = dat['OS event']

out = km.fit(os_time, os_cens, grp)
km.plot(out,cii_lines=None, title='Survival function', cmap='Set2')

# %% [markdown]
# Alternatively, we can use other packages for this
#
# #### scikit-survival

# %%
# #!conda install -c sebp scikit-survival
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-notebook')
mpl.rc('font', **{'family': 'serif', 'serif': 'Palatino'})

from sksurv.nonparametric import kaplan_meier_estimator

os_event = dat['OS event'].map(lambda x: bool(x))
for status in dat['ER Status'].unique():
    mask = dat['ER Status']== status
    time_status, surv_prob_status = kaplan_meier_estimator(os_event[mask],
        dat['OS Time'][mask])
    plt.step(time_status, surv_prob_status, where='post',
        label = "%s (n = %d)" % (status, mask.sum()))

plt.ylabel('Estimated probability of survival $\hat{S}(t)$')
plt.xlabel('Time $t$')
plt.legend(loc='best');


# %% [markdown]
# #### lifelines

# %%
from lifelines import KaplanMeierFitter
from lifelines.plotting import add_at_risk_counts

ax = plt.subplot(111)
kmfs = []
for status in dat['ER Status'].unique():
    mask = dat['ER Status']==status
    kmf = KaplanMeierFitter()
    kmf.fit(dat["OS Time"][mask], event_observed = dat['OS event'][mask], label = status)
    ax = kmf.plot_survival_function(ax=ax,ci_show=False)
    kmfs.append(kmf)

add_at_risk_counts(*kmfs, ax=ax) # *kmfs expands to the elements of kmfs
plt.tight_layout()

# %% [markdown]
# Note that `lifelines` and `scikit-survival` leverage `matplotlib` and so the layers are having to be drawn as part of a for loop. This is typical `matplotlib` behavior.
#
# The `kaplanmeier` function basically packages up the `lifeline` Kaplan-Meier curve and makes some choices for you while creating the graph.

# %% [markdown]
# ## Question 1b

# %%
ax = plt.subplot(111)
kmfs = []
for status in sorted(dat['Node'].unique()):
    mask = dat['Node']==status
    kmf = KaplanMeierFitter()
    kmf.fit(dat["OS Time"][mask], event_observed = dat['OS event'][mask], label = status)
    ax = kmf.plot_survival_function(ax=ax,ci_show=False)
    kmfs.append(kmf)

ax.set_ylabel('Probability of survival ($\hat{S}(t)$)')
ax.set_xlabel('Time ($t$)')
ax.set_title('Kaplan-Meier curve stratified by Node status')

add_at_risk_counts(*kmfs, ax=ax, rows_to_show=['At risk','Events']); # *kmfs expands to the elements of kmfs
#plt.tight_layout()

# %% [markdown]
# ## Question 2

# %%
import plotly.express as px
import plotly.io as pio
pio.renderers.default='notebook'

arrests = pd.read_csv('data/USArrests.csv')
arrests.head()

# %%
fig = px.choropleth(arrests, locations =  'code', color ='Murder', 
    locationmode='USA-states', scope='usa', title="Murders per capita")


fig.show(renderer='notebook_connected') # This option is needed since I'm working in VS Codeb

# %%
fig = px.choropleth(arrests, locations =  'code', color ='Assault', 
    locationmode='USA-states', scope='usa', title="Assaults per capita")


fig.show(renderer='notebook_connected') # This option is needed since I'm working in VS Code

# %%
fig = px.choropleth(arrests, locations =  'code', color ='Rape', 
    locationmode='USA-states', scope='usa', title="Rapes per capita")


fig.show(renderer='notebook_connected') # This option is needed since I'm working in VS Code

# %%
fig = px.choropleth(arrests, locations =  'code', color ='UrbanPop', 
    locationmode='USA-states', scope='usa', title="Percent urban", hover_name='State')

fig.show(renderer='notebook_connected') # This option is needed since I'm working in VS Code

# %%
arrests2 = arrests.melt(id_vars = ['code','State'], var_name = 'Statistics', value_name = 'values')
arrests2.head()

# %%
fig = px.choropleth(arrests2, locations='code', color = 'values', locationmode='USA-states', scope='usa', facet_col='Statistics',
    facet_col_wrap=2, hover_name='State')

fig.show(renderer='notebook_connected')

# %%
import numpy as np
arrests3 = (arrests
    .apply(lambda x: x/np.max(x) if x.name in ['Murder','Assault','UrbanPop','Rape'] else x)
    .melt(id_vars = ['code','State'], var_name='Statistics', value_name = 'Percent of maximum'))

fig = px.choropleth(arrests3, locations='code',hover_name='State', color='Percent of maximum',
    locationmode='USA-states', scope='usa', facet_col='Statistics', facet_col_wrap=2)
fig.update_layout(coloraxis_colorbar_tickformat='.0%')


fig.show(renderer='notebook_connected')
fig.write_html("map_facet2.html")

# %% [markdown]
# ## Extra credit

# %%
import folium
url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"

m = folium.Map(location = [48, -102], zoom_start=3)

folium.Choropleth(
    geo_data = state_geo,
    data = arrests,
    columns = ['code','Murder'],
    legend_name = 'Murder rate',
    key_on='feature.id',
    fill_color = 'PuRd'
).add_to(m)

folium.LayerControl().add_to(m)

m

