# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
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
# # Using plotly for maps
#
# ## Using plotly with geopandas
#
# geopandas provides a nice way to keep data and geometries together. 
#
# plotly accepts the geometry column in a geopandas GeoDataFrame to draw maps like choropleths
#
# We'll use data provided by plotly on the 2013 Montreal mayoral election
#
# ## Using plotly with geopandas
# %%
import plotly.express as px
import plotly
import geopandas as gpd
from IPython.display import IFrame, display_html
def show_fig(fig, filename, width="100%", height=500):
    plotly.offline.plot(fig, filename=filename, auto_open=False, auto_play=False)
    display_html(IFrame(filename, height=height, width=width))

dat = px.data.election()
dat.head()
# %% [markdown]
# We will grab the geometry data as a GeoJSON object and merge it in
# %%
geom = px.data.election_geojson()
geo_df = gpd.GeoDataFrame.from_features(
    geom['features']
).merge(dat, on = 'district').set_index('district')
geo_df.head()
# %% [markdown]
# Note that we now have a `geometry` column in our data set
#
# ## Using plotly with geopandas
#

# %%
fig = px.choropleth(
    geo_df,
    geojson = geo_df['geometry'],
    locations = geo_df.index, #<< we put district names in the index of the dataframe
    color = 'Joly', # Votes that candidate Joly received
    projection = 'mercator'
)
fig.update_geos(fitbounds = 'locations', visible = False)
show_fig(fig, 'img/plt_nybb1.html')
# %% [markdown]
# ## Using built in geographies in plotly
#
# plotly comes with geometry data on US states and countries from the Natural Earth dataset.
#
# We'll create a choropleth using the gapminder data we've used before.
#
# ## Using built in geographies in plotly
#

# %%
gapm_2007 = px.data.gapminder().query('year == 2007')
fig = px.choropleth(
    gapm_2007,
    color = 'lifeExp',
    hover_name='country',
    locations = 'iso_alpha',
    color_continuous_scale=px.colors.sequential.Plasma 
)
show_fig(fig, 'img/plt_lifeexp.html')
# %% [markdown]
# ## Logarithmic scales for color
# We can plot colors on the logarithmic scale, but we need to do a bit of customizing on the colorbar
# to ensure that the ticks are shown on the original scale
# %%
import numpy as np
fig = px.choropleth(
    gapm_2007, color = np.log10(gapm_2007['pop']), hover_name='country',
    locations = 'iso_alpha', color_continuous_scale=px.colors.sequential.Plasma 
)
fig.update_layout(
    coloraxis_colorbar = dict(title='population',
    tickvals = [6,7,8,9], ticktext = ['1M','10M','100M','1B'],
))
show_fig(fig, 'img/plt_le_log.html')
# %% [markdown]
# ## Logarithmic scales for color
# We can also update the hover data to reflect the original scales
# %%
import numpy as np
import pandas as pd

gapm_2007['text'] = "Population: "+ pd.Series(np.round(gapm_2007['pop']/1e6,2)).astype(str)+" M"

fig = px.choropleth(
    gapm_2007, color = np.log10(gapm_2007['pop']), hover_name='country',
    hover_data = {'pop':':.2s', 'iso_alpha':False},
    locations = 'iso_alpha', color_continuous_scale=px.colors.sequential.Plasma,
)
fig.update_layout(
    coloraxis_colorbar = dict(title='population',
    tickvals = [6,7,8,9], ticktext = ['1M','10M','100M','1B'],
))

show_fig(fig, 'img/plt_le_hover.html')
# %% [markdown]
# ## US states using plotly
#
# You have to add the argument `location-mode="USA-states"` to display US states using the default map data
#

# %%
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
df['total exports'] = df['total exports'].astype(float)
fig = px.choropleth(
    df,
    color = 'total exports',
    hover_name = 'state',
    locations = 'code',
    locationmode='USA-states',
)
fig.update_layout(
    title_text = '2011 US Agriculture exports by state',
    geo_scope = 'usa',
    coloraxis_colorbar = {'title':'Millions (USD)'}
)
show_fig(fig, 'img/plt_ag.html')
# %% [markdown]
# ## Representing data as bubbles
#
# We can represent the life expectancy of each country as bubbles on a map

# %%
fig = px.scatter_geo(
    gapm_2007,
    locations="iso_alpha", 
    color="continent",
    hover_name="country", 
    size="gdpPercap",
    projection="natural earth"
    )
show_fig(fig, 'img/plt_bubble.html')
# %% [markdown]
# # Dropping down to plotly graphobjects
#
# ## plotly graphobjects
#
# plotly has a more granular API that can provide more flexibility in plotting
#
# We'll look at a more complex example with some flight data
#
# ## Flight paths
# %%
import plotly.graph_objects as go

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')

fig = go.Figure()
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = df_airports['long'], lat = df_airports['lat'],
    hoverinfo = 'text', text = df_airports['airport'],
    mode = 'markers',
    marker = dict(size = 2,color = 'rgb(255, 0, 0)',
        line = dict(width = 3,color = 'rgba(68, 68, 68, 0)')
    )))
plotly.offline.plot(fig, show_link=False, auto_open=False)
# %% [markdown]
# ## plotly graphobjects
#
# Now we put the flight paths on the map

# %%
flight_paths = []
for i in range(len(df_flight_paths)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
            lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
            mode = 'lines',
            line = dict(width = 1,color = 'red'),
            opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
        )
    )
    fig.update_layout(
    title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = dict(
        scope = 'north america', projection_type = 'azimuthal equal area',
        showland = True, landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

# %% [markdown]
# ## plotly graphobjects
#
# The final product
# %%
show_fig(fig, 'img/plt_flights.html')
# %%
