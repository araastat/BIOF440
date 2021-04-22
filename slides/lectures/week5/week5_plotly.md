# Using plotly for maps

## Using plotly with geopandas

geopandas provides a nice way to keep data and geometries together. 

plotly accepts the geometry column in a geopandas GeoDataFrame to draw maps like choropleths

We'll use data provided by plotly on the 2013 Montreal mayoral election

## Using plotly with geopandas


```python
import plotly.express as px
import plotly
import geopandas as gpd
from IPython.display import IFrame, display_html
def show_fig(fig, filename, width="100%", height=500):
    plotly.offline.plot(fig, filename=filename, auto_open=False, auto_play=False)
    display_html(IFrame(filename, height=height, width=width))

dat = px.data.election()
dat.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>district</th>
      <th>Coderre</th>
      <th>Bergeron</th>
      <th>Joly</th>
      <th>total</th>
      <th>winner</th>
      <th>result</th>
      <th>district_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101-Bois-de-Liesse</td>
      <td>2481</td>
      <td>1829</td>
      <td>3024</td>
      <td>7334</td>
      <td>Joly</td>
      <td>plurality</td>
      <td>101</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102-Cap-Saint-Jacques</td>
      <td>2525</td>
      <td>1163</td>
      <td>2675</td>
      <td>6363</td>
      <td>Joly</td>
      <td>plurality</td>
      <td>102</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11-Sault-au-Récollet</td>
      <td>3348</td>
      <td>2770</td>
      <td>2532</td>
      <td>8650</td>
      <td>Coderre</td>
      <td>plurality</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>111-Mile-End</td>
      <td>1734</td>
      <td>4782</td>
      <td>2514</td>
      <td>9030</td>
      <td>Bergeron</td>
      <td>majority</td>
      <td>111</td>
    </tr>
    <tr>
      <th>4</th>
      <td>112-DeLorimier</td>
      <td>1770</td>
      <td>5933</td>
      <td>3044</td>
      <td>10747</td>
      <td>Bergeron</td>
      <td>majority</td>
      <td>112</td>
    </tr>
  </tbody>
</table>
</div>



We will grab the geometry data as a GeoJSON object and merge it in


```python
geom = px.data.election_geojson()
geo_df = gpd.GeoDataFrame.from_features(
    geom['features']
).merge(dat, on = 'district').set_index('district')
geo_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geometry</th>
      <th>Coderre</th>
      <th>Bergeron</th>
      <th>Joly</th>
      <th>total</th>
      <th>winner</th>
      <th>result</th>
      <th>district_id</th>
    </tr>
    <tr>
      <th>district</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11-Sault-au-Récollet</th>
      <td>MULTIPOLYGON (((-73.63632 45.57592, -73.63628 ...</td>
      <td>3348</td>
      <td>2770</td>
      <td>2532</td>
      <td>8650</td>
      <td>Coderre</td>
      <td>plurality</td>
      <td>11</td>
    </tr>
    <tr>
      <th>12-Saint-Sulpice</th>
      <td>POLYGON ((-73.62175 45.55448, -73.62350 45.553...</td>
      <td>3252</td>
      <td>2521</td>
      <td>2543</td>
      <td>8316</td>
      <td>Coderre</td>
      <td>plurality</td>
      <td>12</td>
    </tr>
    <tr>
      <th>13-Ahuntsic</th>
      <td>POLYGON ((-73.65132 45.55457, -73.65687 45.545...</td>
      <td>2979</td>
      <td>3430</td>
      <td>2873</td>
      <td>9282</td>
      <td>Bergeron</td>
      <td>plurality</td>
      <td>13</td>
    </tr>
    <tr>
      <th>14-Bordeaux-Cartierville</th>
      <td>POLYGON ((-73.70430 45.54419, -73.70421 45.543...</td>
      <td>3612</td>
      <td>1554</td>
      <td>2081</td>
      <td>7247</td>
      <td>Coderre</td>
      <td>plurality</td>
      <td>14</td>
    </tr>
    <tr>
      <th>21-Ouest</th>
      <td>POLYGON ((-73.55769 45.59322, -73.56942 45.597...</td>
      <td>2184</td>
      <td>691</td>
      <td>1076</td>
      <td>3951</td>
      <td>Coderre</td>
      <td>majority</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



Note that we now have a `geometry` column in our data set

## Using plotly with geopandas



```python
fig = px.choropleth(
    geo_df,
    geojson = geo_df['geometry'],
    locations = geo_df.index, #<< we put district names in the index of the dataframe
    color = 'Joly', # Votes that candidate Joly received
    projection = 'mercator'
)
fig.update_geos(fitbounds = 'locations', visible = False)
show_fig(fig, 'img/plt_nybb1.html')
```



<iframe
    width="100%"
    height="500"
    src="img/plt_nybb1.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Using built in geographies in plotly

plotly comes with geometry data on US states and countries from the Natural Earth dataset.

We'll create a choropleth using the gapminder data we've used before.

## Using built in geographies in plotly



```python
gapm_2007 = px.data.gapminder().query('year == 2007')
fig = px.choropleth(
    gapm_2007,
    color = 'lifeExp',
    hover_name='country',
    locations = 'iso_alpha',
    color_continuous_scale=px.colors.sequential.Plasma 
)
show_fig(fig, 'img/plt_lifeexp.html')
```



<iframe
    width="100%"
    height="500"
    src="img/plt_lifeexp.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Logarithmic scales for color
We can plot colors on the logarithmic scale, but we need to do a bit of customizing on the colorbar
to ensure that the ticks are shown on the original scale


```python
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
```



<iframe
    width="100%"
    height="500"
    src="img/plt_le_log.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Logarithmic scales for color
We can also update the hover data to reflect the original scales


```python
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
```



<iframe
    width="100%"
    height="500"
    src="img/plt_le_hover.html"
    frameborder="0"
    allowfullscreen
></iframe>



## US states using plotly

You have to add the argument `location-mode="USA-states"` to display US states using the default map data



```python
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
```



<iframe
    width="100%"
    height="500"
    src="img/plt_ag.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Representing data as bubbles

We can represent the life expectancy of each country as bubbles on a map


```python
fig = px.scatter_geo(
    gapm_2007,
    locations="iso_alpha", 
    color="continent",
    hover_name="country", 
    size="gdpPercap",
    projection="natural earth"
    )
show_fig(fig, 'img/plt_bubble.html')
```



<iframe
    width="100%"
    height="500"
    src="img/plt_bubble.html"
    frameborder="0"
    allowfullscreen
></iframe>



# Dropping down to plotly graphobjects

## plotly graphobjects

plotly has a more granular API that can provide more flexibility in plotting

We'll look at a more complex example with some flight data

## Flight paths


```python
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
```




    'temp-plot.html'



## plotly graphobjects

Now we put the flight paths on the map


```python
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
```

## plotly graphobjects

The final product


```python
show_fig(fig, 'img/plt_flights.html')
```



<iframe
    width="100%"
    height="500"
    src="img/plt_flights.html"
    frameborder="0"
    allowfullscreen
></iframe>




```python

```
