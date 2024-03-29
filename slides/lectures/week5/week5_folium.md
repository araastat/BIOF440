```python
from IPython.display import IFrame, display_html
```

# Folium

---

## Folium

Folium is a Python program that allows the creation of geographic maps using 
leaflet.js, the same javascript package behind R's _leaflet_ package

## Folium

We'll first start by making a map and adding a marker to it, based on position


```python
import folium

m = folium.Map(location = [39.001757066565695, -77.10466742137453], zoom_start = 14) # NIH

folium.Marker([39.001757066565695, -77.10466742137453], 
    popup = "<b>NIH Main Campus</b>", 
    tooltip='Click Me!').add_to(m)

m.save('img/nih_map1.html')
display_html(IFrame('img/nih_map1.html', width='100%', height=450))
```



<iframe
    width="100%"
    height="450"
    src="img/nih_map1.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Folium

We can also add circles to a map to show a region


```python
m = folium.Map(location = [39.001757066565695, -77.10466742137453], zoom_start = 11) # NIH
folium.Circle(radius = 1000, # in meters
     location = [39.001757066565695, -77.10466742137453], # center
     tooltip = 'NIH Campus',
     fill = True,
     fill_color = 'blue',
     color = 'blue').add_to(m)
m.save('img/folium_circle.html')
display_html(IFrame('img/folium_circle.html', width="100%", height=450))
```



<iframe
    width="100%"
    height="450"
    src="img/folium_circle.html"
    frameborder="0"
    allowfullscreen
></iframe>



We can also create choropleth maps using Folium. 

- Link geographic data (GeoJSON/TopoJSON formats) with pandas DataFrame
- These data are merged internally
    - specify key in geography data in JSON variable format
    - the first column of the pandas DataFrame is assumed to be the key to merge with. This cannot be
      specified


```python

import pandas as pd

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)

bins = list(state_data["Unemployment"]
    .quantile([0, 0.25, 0.5, 0.75, 1])) #<< Bins for different colors

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"], #<< first column is merging key
    key_on="feature.id", #<< key in geography data
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
    bins = bins, #<<
).add_to(m)

folium.LayerControl().add_to(m)

m.save('img/unemployment.html')
display_html(IFrame('img/unemployment.html', width="100%", height=450))
```



<iframe
    width="100%"
    height="450"
    src="img/unemployment.html"
    frameborder="0"
    allowfullscreen
></iframe>




# Folium with geopandas

We can also use folium with geopandas.com

Here we will use the gapminder dataset and draw a choropleth of life expectancy in 2007 around the world in



## Folium with geopandas


```python
import plotly.express as px
import folium
import geopandas as gpd

gapm_2007 = px.data.gapminder().query('year == 2007')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# Replace United States of America to United States to fit the naming in the table
world = world.replace('United States of America', 'United States')

tab = world.merge(gapm_2007, how="left", left_on=['name'], right_on=['country'])
tab = tab.dropna(subset = ['lifeExp'])

m = folium.Map()
folium.Choropleth(
    geo_data=tab,
    name='choropleth',
    data=tab,
    columns=['country', 'lifeExp'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Life expectancy in 2007',
).add_to(m)
m.save('img/folium_lifeexp.html')
display_html(IFrame('img/folium_lifeexp.html', width='100%', height=450))
```



<iframe
    width="100%"
    height="450"
    src="img/folium_lifeexp.html"
    frameborder="0"
    allowfullscreen
></iframe>




## Folium with geopandas

We'll add some interactivity by adding a layer to the map using folium's GeoJSON capabilities


```python
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}

le = folium.features.GeoJson(
    tab,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['name','lifeExp','pop'],
        aliases=['Country','Life expectancy: ','Population: '],
     )
)
m.add_child(le)
m.keep_in_front(le)
folium.LayerControl().add_to(m)
m.save('img/folium_lifeexp2.html')
```

## Folium with geopandas



```python
display_html(IFrame('img/folium_lifeexp2.html', width='100%', height=450))
```



<iframe
    width="100%"
    height="450"
    src="img/folium_lifeexp2.html"
    frameborder="0"
    allowfullscreen
></iframe>


