## Geopandas

[Geopandas](https://geopandas.org/index.html) is a tidy way to store geographic location data within
a pandas DataFrame object, much like in the R tibble. It typically adds a "column" named _geometry_
to the DataFrame that holds geometry information about the geographic location structures, like points, 
areas and polygons. 

![](img/geodataframe.png)

This structure allows the easy(er) merging of geographic data with other data about the geography
using pandas merges, as we will see. For this class we will use the _geopandas_ structures operationally,
and not go too deeply into how to manipulate this data.

## Plotting with geopandas

Geopandas DataFrame objects have a `plot` method built in, so we can create basic maps and 
choropleths in short order. These use the **matplotlib** package.

First lets get some data.


```

import geopandas
import matplotlib.pyplot as plt

path_to_data = geopandas.datasets.get_path('nybb') # NYC boroughs
gdf = geopandas.read_file(path_to_data)

gdf
```

Note the structure of the last column `gdf['geometry']`. It is a _MULTIPOLYGON_ structure, which
is a way to specify the geometry of each boroughs as a set of disjoint polygons. 

We will compute the area of each borough using geopandas, for the plotting


```
gdf = gdf.set_index('BoroName')
gdf['area'] = gdf.area
```

## Plotting with geopandas



```
gdf.plot('area');
```


## Plotting with geopandas: layers



```
gdf['centroid'] = gdf.centroid

ax = gdf['geometry'].plot(color = 'lightblue') #<< draw the map in monochrome
gdf['centroid'].plot(ax=ax, color='red');
```


## Map projections

There are different ways of projecting the earth's surface onto a 2-D map, as we traditionally
view maps. You may have heard of Mercator projections, and others.

We can specify different map projections for the same geometry; geopandas takes care of the 
transformations from the provided geometry



```
gdf = gdf.set_geometry('geometry')
boroughs_4326 = gdf.to_crs('EPSG:4326')
ax = boroughs_4326.plot()
ax.set_xlabel('Longitude') #<< Using matplotlib functions
ax.set_ylabel('Latitude');
```

.footnote[Note that the axes text changed to the traditional longitude and latitude]


## Map projections

We can see the projection specification as well


```
boroughs_4326.crs
```


## Larger geographies



```
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

world.head()
```


```
world.plot()
```


```

fig, ax = plt.subplots()
world.plot(column='pop_est',
           ax=ax,
           legend=True,
           legend_kwds={'label': "Population by Country",
                        'orientation': "horizontal"});
```

## Layering maps

We will layer ciites on top of the world map. First make sure that the geometry data are using 
the same CRS (projection)


```
cities = cities.to_crs(world.crs) #<<

base = world.plot(color = 'white', edgecolor = 'black')
cities.plot(ax = base, marker = 'o', color = 'red', markersize = 5)
```

## Layering maps

You can also use matplotlib methods to layer maps as well


```
fig,ax = plt.subplots(1,1)
ax.set_aspect('equal') # makes sure things are on the same aspect
world.plot(ax=ax, color = 'white', edgecolor = 'black')
cities.plot(ax = ax, marker = 'o', color = 'red', markersize = 5)
plt.show()
```

## Layering maps

Note that the order in which you put layers will affect the final map, just like in matplotlib or plotly


```
ax = cities.plot(color = 'black')
world.plot(ax= ax);
```

## Layering maps

We can specify the order even if our code is out of order, with the `zorder` argument


```
ax = cities.plot(color = 'black', zorder=2)
world.plot(ax= ax);
```

## Creating geographic aggregates

If we have regular data, we can aggregate in pandas using `groupby`. 

Sometimes we need to aggregate the geographies. For example, we might have country data and want
to show just the continents

The key to this is the `dissolve` function

## Creating geographic aggregates


```
world1 = world[['continent','geometry']]
continents = world.dissolve(by = 'continent')
continents.plot(edgecolor = 'white')
```

## Creating geographic aggregates

If we also want to aggregate data to the same scale, we can add arguments to the `dissolve` function


```
world2 = world[['continent','pop_est', 'geometry']]
continent = world2.dissolve(by = 'continent', aggfunc = 'sum')
continent.plot(column = 'pop_est', cmap = 'YlOrRd')
```


```

```
