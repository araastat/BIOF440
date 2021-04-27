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
#     display_name: 'Python 3.8.8 64-bit (''biof440'': conda)'
#     name: python388jvsc74a57bd0b8a008180da9e18ef20641f3ac8286a501f34fc11767b3b3fb216c86c1ec99bf
# ---

# %% [markdown]
# ## Python setup

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly
import plotly.express as px
import os

if not os.path.exists('img'):
    os.makedirs('img')

from IPython.display import IFrame, display_html
def show_fig(fig, filename, width="100%", height=500):
    plotly.offline.plot(fig, filename=filename, auto_open=False, auto_play=False)
    display_html(IFrame(filename, height=height, width=width))

def show_fig2(filename, width="100%", height=500):
    display_html(IFrame(filename, width=width, height=height))


# %% [markdown]
# # Heatmaps
#
# ## Heatmaps
#
# Heatmaps are a common 2-dimensional colored grid that is used for visualizing intensity or level of a variable across levels of two other variables.
#
# It is commonly used in bioinformatics to display expression levels of genes across samples, often in conjunction with some cluster analysis to put
# like genes/samples next to each other for visualization purposes
#
# Heatmaps can be drawn using all the packages we have seen in this class. 
#
#
# ## Example data
#
# We'll use average monthly temperatures in Washington, DC in 1971-2020, obtained from the National Weather Service ([link](https://w2.weather.gov/climate/xmacis.php?wfo=lwx)).
#
# .footnote[This data was extracted using the R package `datapasta`]

# %%
import pandas as pd

dc_weather = pd.read_csv('data/dc_weather.csv')
dc_weather.drop('Annual', axis=1, inplace=True) # Remove the 'Annual' column
dc_weather.set_index('Year', inplace=True)
dc_weather = dc_weather.T
dc_weather.index.name='Month'

# %% [markdown]
# ## Weather data: Seaborn

# %%
fig, ax = plt.subplots(figsize = (15,5))
sns.heatmap(dc_weather, cmap="inferno", cbar_kws={'shrink':0.8, 'label': 'Degrees (F)'}, ax=ax);

ax.set_yticklabels(ax.get_yticklabels(), rotation = 0, horizontalalignment='right');
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, horizontalalignment='right');
ax.set_title('Average monthly temperature in Washington DC (1971-2020)', loc='left');
fig.savefig('img/temp_sns.html')
show_fig2('img/temp_sns.html')



# %% [markdown]
# ## Weather data: matplotlib

# %%
fig, ax = plt.subplots(figsize=(15,5))
im= ax.imshow(dc_weather.values, cmap='inferno')
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Degrees (F)', rotation=90, va='bottom');
ax.set_xticks(np.arange(dc_weather.shape[1]))
ax.set_yticks(np.arange(dc_weather.shape[0]))
ax.set_xticklabels(dc_weather.columns.values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(dc_weather.index.values);
ax.set_title('Average monthly temperature in Washington DC (1971-2020)', loc='left');
fig.savefig('img/temp_mpl.html')
show_fig2('img/temp_mpl.html')

# %% [markdown]
# ## Weather data: Plotly express

# %%
fig = px.imshow(dc_weather, labels = dict(color='Temperature (F)'))
show_fig(fig, 'img/temp_plotly.html')

# %% [markdown]
# ## Weather data: altair

# %%
D = dc_weather.reset_index().melt(id_vars='Month', value_name='Avg Temp')
D['Month'] = pd.Categorical(D['Month'], categories = dc_weather.index)
alt.Chart(D).mark_rect().encode(
    x = 'Year:N', # Make year nominal so it is treated as a discrete variable
    y = alt.Y('Month:N', bin=False, sort=None),
    color = alt.Color('Avg Temp:Q', scale = alt.Scale(scheme='inferno')),
    tooltip = ['Month','Year','Avg Temp']
).save('img/temp_alt.html')
show_fig2('img/temp_alt.html')

# %% [markdown]
# # Adding clustering
#
# ## Re-ordering rows and columns
#
# In many contexts, especially bioinformatics, heatmaps are used to display similarities between units, using cluster analysis. Typically hierarchical clustering is used.
#
# We will use a breast cancer data set, and look to see if there are individuals who have similar profiles across the variables recorded, and if that might be related to outcome.
#

# %%
from sklearn.datasets import load_breast_cancer
bc_data = load_breast_cancer()
data = pd.DataFrame(bc_data.data, columns = bc_data.feature_names)
data.head()

# %% [markdown]
# ## breast cancer: creating the heatmap
#
# In **seaborn**, the `clustermap` function takes care of the clustering for us. Note that we are scaling the rows so that they have mean 0 and variance 1, to enable a better view of the differences in patterns. We are also using the correlation metric (1 - correlation) to cluster rows and columns.

# %%
fig = sns.clustermap(data, standard_scale=1, metric='correlation', method='average',cmap='RdBu',);
fig.savefig('img/heatmap_cluster1.png')
show_fig2('img/heatmap_cluster1.png')

# %% [markdown]
# ## breast cancer: adding to the heatmap
#
# We will add a column to the heatmap that color-codes the outcomes, so we can see if the clustering aligns with the outcomes.

# %%
color_dict = dict(zip(np.unique(bc_data.target), np.array(['g','skyblue'])))
target_df = pd.DataFrame({'target': bc_data.target})
row_colors = target_df.target.map(color_dict)

# %% [markdown]
# ## breast cancer: adding to the heatmap

# %%
sns.clustermap(data, standard_scale=1, metric='correlation', method='average', cmap = 'RdBu',row_colors=row_colors);

# %% [markdown]
# # Embellishing the heatmap
#
# ## Adding marginal histograms and annotation
#
# We will use a data set of measles cases in the US from 1930 to 2000 to demonstrate how to create marginal histograms around a heatmap. 
#
# We can first read in the data and do a bit of data munging.

# %%
measles = pd.read_csv('data/measles.csv')
measles['state'] = measles['state'].str.title().str.replace('.', ' ')
measles = measles.set_index('state')
measles.head()

# %%
measles2 = measles.reset_index().melt(id_vars = 'state',var_name='Year', value_name='count') # Tidying the data
bl = measles2.groupby('state')['count'].sum()
ind = bl.argsort() # Find index order that makes the states ordered by total case

# %%
# Creating marginal frequency distributions
d1 = measles2.groupby('Year').sum().reset_index()
d2 = measles2.groupby('state').sum().reset_index().sort_values(by='count', ascending=False)

# %% [markdown]
# ## measles: seaborn

# %%
g = sns.JointGrid(ratio=8, height=10)
sns.heatmap(measles.iloc[ind[::-1],:], cmap='YlOrRd', linewidth=0.1,ax=g.ax_joint, cbar=False)
sns.barplot(x='count', y ='state', data=d2, color = 'yellow', ax = g.ax_marg_y)
sns.barplot(y='count', x = 'Year', data=d1, color='yellow', ax = g.ax_marg_x)
g.ax_joint.axvline(np.where(measles.columns=='1961'), linestyle='--')
g.ax_joint.set_xticks(np.arange(0,80,10))
g.ax_joint.set_xticklabels(np.arange(1930, 2005,10),rotation=45);
g.ax_joint.set_ylabel('');
g.ax_marg_x.text(31,100,'Vaccine introduced', horizontalalignment='center', fontsize='x-large');
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Measles cases in the US, 1930-2001", fontsize='xx-large');   
g.fig.savefig('img/measles_sns.png')

# %%
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig1 = make_subplots(rows=2, cols=2, column_widths=[0.8, 0.2], row_heights=[0.2,0.8], horizontal_spacing=0.05, vertical_spacing=0.05)
fig1.add_trace(
    go.Heatmap(z = measles_px.values, x = measles_px.columns, y = measles_px.index, colorscale='ylorrd', showscale=False),
    row=2, col=1
)
fig1.add_trace(
    go.Bar(x = d1.Year, y = d1['count'].values, marker_color='orange')
)
fig1.add_trace(
    go.Bar(x = d2['count'].values, y = d2.state, orientation='h', marker_color='orange'),
    row=2,col=2,
)
fig1.add_shape(go.layout.Shape(type='line', x0=31, x1=31, y0 = -1, y1=56, line=dict(color='green', width=3, dash='dash')),row=2, col = 1, )
fig1.add_annotation(xref='x domain', yref='y domain', x = 0.45, y = 0.05, text = 'Vaccine available', showarrow=False, row=2, col=1,)
fig1.update_xaxes(showticklabels=False, row=1, col=1)
fig1.update_yaxes(showticklabels=False, row=2, col=2)
fig1.update_yaxes(row=2, col=1, autorange='reversed')
fig1.update_yaxes(row=2, col=2, autorange='reversed')
fig1.update_layout(showlegend=False, template = 'simple_white')
show_fig(fig1, 'img/measles_plotly.html')

# %% [markdown]
# ## measles: seaborn

# %%
show_fig2('img/measles_sns.png')

# %% [markdown]
# ## measles: altair

# %%
top_bar = alt.Chart(d1).mark_bar().encode(
    x = alt.X('Year', axis = alt.Axis(labels=False, title=None)),
    y = alt.Y('count', axis = alt.Axis(title=None, format='s')),
    tooltip = ['Year', alt.Tooltip('count', title="N", format='.3s')],
).properties(width=600, height=200).interactive()
side_bar = alt.Chart(d2).mark_bar().encode(
    y = alt.Y('state', sort=d2.state.values, axis = alt.Axis(labels=False, title=None)),
    x = alt.X('count', axis = alt.Axis(title=None, format='s')),
    tooltip = ['state',alt.Tooltip('count', title="N",format='.3s')],
).properties(width=200, height=600).interactive()

heatmap = alt.Chart(measles2).mark_rect().encode(
    x = 'Year', 
    y = alt.Y('state', sort = d2.state.values),
    color = alt.Color('count', scale=alt.Scale( scheme='yelloworangered')), 
    tooltip = [alt.Tooltip('state', title='State'),
            alt.Tooltip('Year', title='Year'),
            alt.Tooltip('count', title='N', format='.3s')],
).properties(width=600, height=600).interactive()
(top_bar & (heatmap | side_bar)).save('img/measles_alt.html')


# %% [markdown]
# ## measles: altair

# %%
show_fig2('img/measles_alt.html')
