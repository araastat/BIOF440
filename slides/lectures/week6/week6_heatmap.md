## Python setup


```python
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
```

# Heatmaps

## Heatmaps

Heatmaps are a common 2-dimensional colored grid that is used for visualizing intensity or level of a variable across levels of two other variables.

It is commonly used in bioinformatics to display expression levels of genes across samples, often in conjunction with some cluster analysis to put
like genes/samples next to each other for visualization purposes

Heatmaps can be drawn using all the packages we have seen in this class. 


## Example data

We'll use average monthly temperatures in Washington, DC in 1971-2020, obtained from the National Weather Service ([link](https://w2.weather.gov/climate/xmacis.php?wfo=lwx)).

.footnote[This data was extracted using the R package `datapasta`]


```python
import pandas as pd

dc_weather = pd.read_csv('data/dc_weather.csv')
dc_weather.drop('Annual', axis=1, inplace=True) # Remove the 'Annual' column
dc_weather.set_index('Year', inplace=True)
dc_weather = dc_weather.T
dc_weather.index.name='Month'
```

## Weather data: Seaborn


```python
fig, ax = plt.subplots(figsize = (15,5))
sns.heatmap(dc_weather, cmap="inferno", cbar_kws={'shrink':0.8, 'label': 'Degrees (F)'}, ax=ax);

ax.set_yticklabels(ax.get_yticklabels(), rotation = 0, horizontalalignment='right');
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, horizontalalignment='right');
ax.set_title('Average monthly temperature in Washington DC (1971-2020)', loc='left');
fig.savefig('img/temp_sns.html')
show_fig2('img/temp_sns.html')


```


    
![svg](week6_heatmap_files/week6_heatmap_5_0.svg)
    


## Weather data: matplotlib


```python
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
```


    
![svg](week6_heatmap_files/week6_heatmap_7_0.svg)
    


## Weather data: Plotly express


```python
fig = px.imshow(dc_weather, labels = dict(color='Temperature (F)'))
show_fig(fig, 'img/temp_plotly.html')
```



## Weather data: altair


```python
D = dc_weather.reset_index().melt(id_vars='Month', value_name='Avg Temp')
D['Month'] = pd.Categorical(D['Month'], categories = dc_weather.index)
alt.Chart(D).mark_rect().encode(
    x = 'Year:N', # Make year nominal so it is treated as a discrete variable
    y = alt.Y('Month:N', bin=False, sort=None),
    color = alt.Color('Avg Temp:Q', scale = alt.Scale(scheme='inferno')),
    tooltip = ['Month','Year','Avg Temp']
).save('img/temp_alt.html')
show_fig2('img/temp_alt.html')
```





<div id="altair-viz-54d08ddbd8e74f9e975b83d97c15ac1b"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-54d08ddbd8e74f9e975b83d97c15ac1b") {
      outputDiv = document.getElementById("altair-viz-54d08ddbd8e74f9e975b83d97c15ac1b");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-093187107e3e3bedf01318c3c93c3189"}, "mark": "rect", "encoding": {"color": {"type": "quantitative", "field": "Avg Temp", "scale": {"scheme": "inferno"}}, "tooltip": [{"type": "nominal", "field": "Month"}, {"type": "quantitative", "field": "Year"}, {"type": "quantitative", "field": "Avg Temp"}], "x": {"type": "nominal", "field": "Year"}, "y": {"type": "nominal", "bin": false, "field": "Month", "sort": null}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-093187107e3e3bedf01318c3c93c3189": [{"Month": "Jan", "Year": 1971, "Avg Temp": 30.0}, {"Month": "Feb", "Year": 1971, "Avg Temp": 37.4}, {"Month": "Mar", "Year": 1971, "Avg Temp": 41.8}, {"Month": "Apr", "Year": 1971, "Avg Temp": 52.6}, {"Month": "May", "Year": 1971, "Avg Temp": 61.2}, {"Month": "Jun", "Year": 1971, "Avg Temp": 74.0}, {"Month": "Jul", "Year": 1971, "Avg Temp": 76.5}, {"Month": "Aug", "Year": 1971, "Avg Temp": 74.2}, {"Month": "Sep", "Year": 1971, "Avg Temp": 70.9}, {"Month": "Oct", "Year": 1971, "Avg Temp": 62.9}, {"Month": "Nov", "Year": 1971, "Avg Temp": 46.3}, {"Month": "Dec", "Year": 1971, "Avg Temp": 43.7}, {"Month": "Jan", "Year": 1972, "Avg Temp": 37.6}, {"Month": "Feb", "Year": 1972, "Avg Temp": 34.3}, {"Month": "Mar", "Year": 1972, "Avg Temp": 43.5}, {"Month": "Apr", "Year": 1972, "Avg Temp": 51.6}, {"Month": "May", "Year": 1972, "Avg Temp": 62.7}, {"Month": "Jun", "Year": 1972, "Avg Temp": 68.1}, {"Month": "Jul", "Year": 1972, "Avg Temp": 76.9}, {"Month": "Aug", "Year": 1972, "Avg Temp": 75.4}, {"Month": "Sep", "Year": 1972, "Avg Temp": 69.8}, {"Month": "Oct", "Year": 1972, "Avg Temp": 53.5}, {"Month": "Nov", "Year": 1972, "Avg Temp": 43.2}, {"Month": "Dec", "Year": 1972, "Avg Temp": 40.3}, {"Month": "Jan", "Year": 1973, "Avg Temp": 34.6}, {"Month": "Feb", "Year": 1973, "Avg Temp": 34.3}, {"Month": "Mar", "Year": 1973, "Avg Temp": 48.2}, {"Month": "Apr", "Year": 1973, "Avg Temp": 53.0}, {"Month": "May", "Year": 1973, "Avg Temp": 59.5}, {"Month": "Jun", "Year": 1973, "Avg Temp": 73.5}, {"Month": "Jul", "Year": 1973, "Avg Temp": 75.9}, {"Month": "Aug", "Year": 1973, "Avg Temp": 76.9}, {"Month": "Sep", "Year": 1973, "Avg Temp": 69.7}, {"Month": "Oct", "Year": 1973, "Avg Temp": 58.2}, {"Month": "Nov", "Year": 1973, "Avg Temp": 47.3}, {"Month": "Dec", "Year": 1973, "Avg Temp": 37.3}, {"Month": "Jan", "Year": 1974, "Avg Temp": 37.9}, {"Month": "Feb", "Year": 1974, "Avg Temp": 33.8}, {"Month": "Mar", "Year": 1974, "Avg Temp": 45.2}, {"Month": "Apr", "Year": 1974, "Avg Temp": 55.3}, {"Month": "May", "Year": 1974, "Avg Temp": 61.9}, {"Month": "Jun", "Year": 1974, "Avg Temp": 68.5}, {"Month": "Jul", "Year": 1974, "Avg Temp": 76.5}, {"Month": "Aug", "Year": 1974, "Avg Temp": 75.0}, {"Month": "Sep", "Year": 1974, "Avg Temp": 67.5}, {"Month": "Oct", "Year": 1974, "Avg Temp": 55.3}, {"Month": "Nov", "Year": 1974, "Avg Temp": 48.2}, {"Month": "Dec", "Year": 1974, "Avg Temp": 40.3}, {"Month": "Jan", "Year": 1975, "Avg Temp": 38.5}, {"Month": "Feb", "Year": 1975, "Avg Temp": 39.0}, {"Month": "Mar", "Year": 1975, "Avg Temp": 42.1}, {"Month": "Apr", "Year": 1975, "Avg Temp": 50.4}, {"Month": "May", "Year": 1975, "Avg Temp": 66.3}, {"Month": "Jun", "Year": 1975, "Avg Temp": 73.0}, {"Month": "Jul", "Year": 1975, "Avg Temp": 76.0}, {"Month": "Aug", "Year": 1975, "Avg Temp": 77.8}, {"Month": "Sep", "Year": 1975, "Avg Temp": 66.0}, {"Month": "Oct", "Year": 1975, "Avg Temp": 60.6}, {"Month": "Nov", "Year": 1975, "Avg Temp": 51.9}, {"Month": "Dec", "Year": 1975, "Avg Temp": 37.2}, {"Month": "Jan", "Year": 1976, "Avg Temp": 30.8}, {"Month": "Feb", "Year": 1976, "Avg Temp": 44.0}, {"Month": "Mar", "Year": 1976, "Avg Temp": 48.0}, {"Month": "Apr", "Year": 1976, "Avg Temp": 56.9}, {"Month": "May", "Year": 1976, "Avg Temp": 62.1}, {"Month": "Jun", "Year": 1976, "Avg Temp": 74.8}, {"Month": "Jul", "Year": 1976, "Avg Temp": 75.0}, {"Month": "Aug", "Year": 1976, "Avg Temp": 73.9}, {"Month": "Sep", "Year": 1976, "Avg Temp": 67.5}, {"Month": "Oct", "Year": 1976, "Avg Temp": 52.9}, {"Month": "Nov", "Year": 1976, "Avg Temp": 40.9}, {"Month": "Dec", "Year": 1976, "Avg Temp": 32.6}, {"Month": "Jan", "Year": 1977, "Avg Temp": 22.9}, {"Month": "Feb", "Year": 1977, "Avg Temp": 36.5}, {"Month": "Mar", "Year": 1977, "Avg Temp": 49.9}, {"Month": "Apr", "Year": 1977, "Avg Temp": 57.9}, {"Month": "May", "Year": 1977, "Avg Temp": 66.7}, {"Month": "Jun", "Year": 1977, "Avg Temp": 71.4}, {"Month": "Jul", "Year": 1977, "Avg Temp": 79.0}, {"Month": "Aug", "Year": 1977, "Avg Temp": 77.7}, {"Month": "Sep", "Year": 1977, "Avg Temp": 72.1}, {"Month": "Oct", "Year": 1977, "Avg Temp": 56.0}, {"Month": "Nov", "Year": 1977, "Avg Temp": 49.2}, {"Month": "Dec", "Year": 1977, "Avg Temp": 35.6}, {"Month": "Jan", "Year": 1978, "Avg Temp": 29.2}, {"Month": "Feb", "Year": 1978, "Avg Temp": 27.3}, {"Month": "Mar", "Year": 1978, "Avg Temp": 41.7}, {"Month": "Apr", "Year": 1978, "Avg Temp": 54.2}, {"Month": "May", "Year": 1978, "Avg Temp": 62.3}, {"Month": "Jun", "Year": 1978, "Avg Temp": 73.1}, {"Month": "Jul", "Year": 1978, "Avg Temp": 75.8}, {"Month": "Aug", "Year": 1978, "Avg Temp": 78.1}, {"Month": "Sep", "Year": 1978, "Avg Temp": 69.7}, {"Month": "Oct", "Year": 1978, "Avg Temp": 56.1}, {"Month": "Nov", "Year": 1978, "Avg Temp": 48.7}, {"Month": "Dec", "Year": 1978, "Avg Temp": 40.1}, {"Month": "Jan", "Year": 1979, "Avg Temp": 33.1}, {"Month": "Feb", "Year": 1979, "Avg Temp": 25.5}, {"Month": "Mar", "Year": 1979, "Avg Temp": 48.4}, {"Month": "Apr", "Year": 1979, "Avg Temp": 53.1}, {"Month": "May", "Year": 1979, "Avg Temp": 64.6}, {"Month": "Jun", "Year": 1979, "Avg Temp": 70.7}, {"Month": "Jul", "Year": 1979, "Avg Temp": 75.9}, {"Month": "Aug", "Year": 1979, "Avg Temp": 75.6}, {"Month": "Sep", "Year": 1979, "Avg Temp": 68.8}, {"Month": "Oct", "Year": 1979, "Avg Temp": 55.6}, {"Month": "Nov", "Year": 1979, "Avg Temp": 50.6}, {"Month": "Dec", "Year": 1979, "Avg Temp": 40.3}, {"Month": "Jan", "Year": 1980, "Avg Temp": 33.8}, {"Month": "Feb", "Year": 1980, "Avg Temp": 31.4}, {"Month": "Mar", "Year": 1980, "Avg Temp": 41.4}, {"Month": "Apr", "Year": 1980, "Avg Temp": 55.7}, {"Month": "May", "Year": 1980, "Avg Temp": 65.5}, {"Month": "Jun", "Year": 1980, "Avg Temp": 71.3}, {"Month": "Jul", "Year": 1980, "Avg Temp": 78.2}, {"Month": "Aug", "Year": 1980, "Avg Temp": 78.7}, {"Month": "Sep", "Year": 1980, "Avg Temp": 72.2}, {"Month": "Oct", "Year": 1980, "Avg Temp": 55.3}, {"Month": "Nov", "Year": 1980, "Avg Temp": 44.2}, {"Month": "Dec", "Year": 1980, "Avg Temp": 35.5}, {"Month": "Jan", "Year": 1981, "Avg Temp": 27.9}, {"Month": "Feb", "Year": 1981, "Avg Temp": 38.8}, {"Month": "Mar", "Year": 1981, "Avg Temp": 41.9}, {"Month": "Apr", "Year": 1981, "Avg Temp": 57.0}, {"Month": "May", "Year": 1981, "Avg Temp": 62.2}, {"Month": "Jun", "Year": 1981, "Avg Temp": 74.3}, {"Month": "Jul", "Year": 1981, "Avg Temp": 77.3}, {"Month": "Aug", "Year": 1981, "Avg Temp": 74.4}, {"Month": "Sep", "Year": 1981, "Avg Temp": 67.7}, {"Month": "Oct", "Year": 1981, "Avg Temp": 53.2}, {"Month": "Nov", "Year": 1981, "Avg Temp": 46.2}, {"Month": "Dec", "Year": 1981, "Avg Temp": 34.5}, {"Month": "Jan", "Year": 1982, "Avg Temp": 25.5}, {"Month": "Feb", "Year": 1982, "Avg Temp": 35.8}, {"Month": "Mar", "Year": 1982, "Avg Temp": 42.9}, {"Month": "Apr", "Year": 1982, "Avg Temp": 50.7}, {"Month": "May", "Year": 1982, "Avg Temp": 66.1}, {"Month": "Jun", "Year": 1982, "Avg Temp": 69.4}, {"Month": "Jul", "Year": 1982, "Avg Temp": 77.1}, {"Month": "Aug", "Year": 1982, "Avg Temp": 73.0}, {"Month": "Sep", "Year": 1982, "Avg Temp": 67.3}, {"Month": "Oct", "Year": 1982, "Avg Temp": 56.3}, {"Month": "Nov", "Year": 1982, "Avg Temp": 48.4}, {"Month": "Dec", "Year": 1982, "Avg Temp": 42.0}, {"Month": "Jan", "Year": 1983, "Avg Temp": 34.6}, {"Month": "Feb", "Year": 1983, "Avg Temp": 34.7}, {"Month": "Mar", "Year": 1983, "Avg Temp": 45.3}, {"Month": "Apr", "Year": 1983, "Avg Temp": 51.7}, {"Month": "May", "Year": 1983, "Avg Temp": 61.5}, {"Month": "Jun", "Year": 1983, "Avg Temp": 72.1}, {"Month": "Jul", "Year": 1983, "Avg Temp": 78.7}, {"Month": "Aug", "Year": 1983, "Avg Temp": 78.0}, {"Month": "Sep", "Year": 1983, "Avg Temp": 69.5}, {"Month": "Oct", "Year": 1983, "Avg Temp": 57.2}, {"Month": "Nov", "Year": 1983, "Avg Temp": 47.0}, {"Month": "Dec", "Year": 1983, "Avg Temp": 33.2}, {"Month": "Jan", "Year": 1984, "Avg Temp": 28.5}, {"Month": "Feb", "Year": 1984, "Avg Temp": 41.7}, {"Month": "Mar", "Year": 1984, "Avg Temp": 38.2}, {"Month": "Apr", "Year": 1984, "Avg Temp": 51.5}, {"Month": "May", "Year": 1984, "Avg Temp": 61.3}, {"Month": "Jun", "Year": 1984, "Avg Temp": 73.4}, {"Month": "Jul", "Year": 1984, "Avg Temp": 73.9}, {"Month": "Aug", "Year": 1984, "Avg Temp": 75.0}, {"Month": "Sep", "Year": 1984, "Avg Temp": 64.8}, {"Month": "Oct", "Year": 1984, "Avg Temp": 62.1}, {"Month": "Nov", "Year": 1984, "Avg Temp": 43.9}, {"Month": "Dec", "Year": 1984, "Avg Temp": 44.1}, {"Month": "Jan", "Year": 1985, "Avg Temp": 29.2}, {"Month": "Feb", "Year": 1985, "Avg Temp": 38.7}, {"Month": "Mar", "Year": 1985, "Avg Temp": 46.0}, {"Month": "Apr", "Year": 1985, "Avg Temp": 57.8}, {"Month": "May", "Year": 1985, "Avg Temp": 65.1}, {"Month": "Jun", "Year": 1985, "Avg Temp": 70.4}, {"Month": "Jul", "Year": 1985, "Avg Temp": 76.4}, {"Month": "Aug", "Year": 1985, "Avg Temp": 74.4}, {"Month": "Sep", "Year": 1985, "Avg Temp": 69.4}, {"Month": "Oct", "Year": 1985, "Avg Temp": 58.8}, {"Month": "Nov", "Year": 1985, "Avg Temp": 52.4}, {"Month": "Dec", "Year": 1985, "Avg Temp": 33.7}, {"Month": "Jan", "Year": 1986, "Avg Temp": 33.1}, {"Month": "Feb", "Year": 1986, "Avg Temp": 32.9}, {"Month": "Mar", "Year": 1986, "Avg Temp": 45.0}, {"Month": "Apr", "Year": 1986, "Avg Temp": 53.5}, {"Month": "May", "Year": 1986, "Avg Temp": 66.6}, {"Month": "Jun", "Year": 1986, "Avg Temp": 74.4}, {"Month": "Jul", "Year": 1986, "Avg Temp": 79.3}, {"Month": "Aug", "Year": 1986, "Avg Temp": 73.1}, {"Month": "Sep", "Year": 1986, "Avg Temp": 68.9}, {"Month": "Oct", "Year": 1986, "Avg Temp": 58.9}, {"Month": "Nov", "Year": 1986, "Avg Temp": 44.8}, {"Month": "Dec", "Year": 1986, "Avg Temp": 38.1}, {"Month": "Jan", "Year": 1987, "Avg Temp": 32.4}, {"Month": "Feb", "Year": 1987, "Avg Temp": 34.3}, {"Month": "Mar", "Year": 1987, "Avg Temp": 46.2}, {"Month": "Apr", "Year": 1987, "Avg Temp": 53.1}, {"Month": "May", "Year": 1987, "Avg Temp": 65.0}, {"Month": "Jun", "Year": 1987, "Avg Temp": 74.4}, {"Month": "Jul", "Year": 1987, "Avg Temp": 80.0}, {"Month": "Aug", "Year": 1987, "Avg Temp": 76.1}, {"Month": "Sep", "Year": 1987, "Avg Temp": 69.3}, {"Month": "Oct", "Year": 1987, "Avg Temp": 51.5}, {"Month": "Nov", "Year": 1987, "Avg Temp": 47.8}, {"Month": "Dec", "Year": 1987, "Avg Temp": 39.8}, {"Month": "Jan", "Year": 1988, "Avg Temp": 28.6}, {"Month": "Feb", "Year": 1988, "Avg Temp": 35.8}, {"Month": "Mar", "Year": 1988, "Avg Temp": 45.0}, {"Month": "Apr", "Year": 1988, "Avg Temp": 52.0}, {"Month": "May", "Year": 1988, "Avg Temp": 64.0}, {"Month": "Jun", "Year": 1988, "Avg Temp": 73.0}, {"Month": "Jul", "Year": 1988, "Avg Temp": 80.3}, {"Month": "Aug", "Year": 1988, "Avg Temp": 78.5}, {"Month": "Sep", "Year": 1988, "Avg Temp": 66.8}, {"Month": "Oct", "Year": 1988, "Avg Temp": 51.3}, {"Month": "Nov", "Year": 1988, "Avg Temp": 48.1}, {"Month": "Dec", "Year": 1988, "Avg Temp": 36.3}, {"Month": "Jan", "Year": 1989, "Avg Temp": 37.9}, {"Month": "Feb", "Year": 1989, "Avg Temp": 36.4}, {"Month": "Mar", "Year": 1989, "Avg Temp": 43.8}, {"Month": "Apr", "Year": 1989, "Avg Temp": 52.5}, {"Month": "May", "Year": 1989, "Avg Temp": 62.0}, {"Month": "Jun", "Year": 1989, "Avg Temp": 73.9}, {"Month": "Jul", "Year": 1989, "Avg Temp": 76.0}, {"Month": "Aug", "Year": 1989, "Avg Temp": 74.4}, {"Month": "Sep", "Year": 1989, "Avg Temp": 68.9}, {"Month": "Oct", "Year": 1989, "Avg Temp": 58.2}, {"Month": "Nov", "Year": 1989, "Avg Temp": 44.8}, {"Month": "Dec", "Year": 1989, "Avg Temp": 25.3}, {"Month": "Jan", "Year": 1990, "Avg Temp": 42.0}, {"Month": "Feb", "Year": 1990, "Avg Temp": 42.2}, {"Month": "Mar", "Year": 1990, "Avg Temp": 47.6}, {"Month": "Apr", "Year": 1990, "Avg Temp": 54.8}, {"Month": "May", "Year": 1990, "Avg Temp": 62.3}, {"Month": "Jun", "Year": 1990, "Avg Temp": 73.3}, {"Month": "Jul", "Year": 1990, "Avg Temp": 78.4}, {"Month": "Aug", "Year": 1990, "Avg Temp": 74.5}, {"Month": "Sep", "Year": 1990, "Avg Temp": 67.3}, {"Month": "Oct", "Year": 1990, "Avg Temp": 60.7}, {"Month": "Nov", "Year": 1990, "Avg Temp": 49.6}, {"Month": "Dec", "Year": 1990, "Avg Temp": 42.2}, {"Month": "Jan", "Year": 1991, "Avg Temp": 35.5}, {"Month": "Feb", "Year": 1991, "Avg Temp": 40.7}, {"Month": "Mar", "Year": 1991, "Avg Temp": 46.6}, {"Month": "Apr", "Year": 1991, "Avg Temp": 55.9}, {"Month": "May", "Year": 1991, "Avg Temp": 70.5}, {"Month": "Jun", "Year": 1991, "Avg Temp": 74.6}, {"Month": "Jul", "Year": 1991, "Avg Temp": 79.5}, {"Month": "Aug", "Year": 1991, "Avg Temp": 77.7}, {"Month": "Sep", "Year": 1991, "Avg Temp": 69.0}, {"Month": "Oct", "Year": 1991, "Avg Temp": 57.8}, {"Month": "Nov", "Year": 1991, "Avg Temp": 45.8}, {"Month": "Dec", "Year": 1991, "Avg Temp": 38.7}, {"Month": "Jan", "Year": 1992, "Avg Temp": 34.5}, {"Month": "Feb", "Year": 1992, "Avg Temp": 37.1}, {"Month": "Mar", "Year": 1992, "Avg Temp": 41.3}, {"Month": "Apr", "Year": 1992, "Avg Temp": 52.0}, {"Month": "May", "Year": 1992, "Avg Temp": 60.8}, {"Month": "Jun", "Year": 1992, "Avg Temp": 70.1}, {"Month": "Jul", "Year": 1992, "Avg Temp": 77.4}, {"Month": "Aug", "Year": 1992, "Avg Temp": 72.3}, {"Month": "Sep", "Year": 1992, "Avg Temp": 67.7}, {"Month": "Oct", "Year": 1992, "Avg Temp": 54.3}, {"Month": "Nov", "Year": 1992, "Avg Temp": 47.2}, {"Month": "Dec", "Year": 1992, "Avg Temp": 38.9}, {"Month": "Jan", "Year": 1993, "Avg Temp": 37.9}, {"Month": "Feb", "Year": 1993, "Avg Temp": 31.4}, {"Month": "Mar", "Year": 1993, "Avg Temp": 39.4}, {"Month": "Apr", "Year": 1993, "Avg Temp": 52.5}, {"Month": "May", "Year": 1993, "Avg Temp": 65.0}, {"Month": "Jun", "Year": 1993, "Avg Temp": 72.2}, {"Month": "Jul", "Year": 1993, "Avg Temp": 80.1}, {"Month": "Aug", "Year": 1993, "Avg Temp": 76.6}, {"Month": "Sep", "Year": 1993, "Avg Temp": 68.8}, {"Month": "Oct", "Year": 1993, "Avg Temp": 55.5}, {"Month": "Nov", "Year": 1993, "Avg Temp": 46.4}, {"Month": "Dec", "Year": 1993, "Avg Temp": 36.2}, {"Month": "Jan", "Year": 1994, "Avg Temp": 27.0}, {"Month": "Feb", "Year": 1994, "Avg Temp": 34.0}, {"Month": "Mar", "Year": 1994, "Avg Temp": 42.9}, {"Month": "Apr", "Year": 1994, "Avg Temp": 59.6}, {"Month": "May", "Year": 1994, "Avg Temp": 60.6}, {"Month": "Jun", "Year": 1994, "Avg Temp": 77.2}, {"Month": "Jul", "Year": 1994, "Avg Temp": 80.1}, {"Month": "Aug", "Year": 1994, "Avg Temp": 74.1}, {"Month": "Sep", "Year": 1994, "Avg Temp": 68.1}, {"Month": "Oct", "Year": 1994, "Avg Temp": 56.8}, {"Month": "Nov", "Year": 1994, "Avg Temp": 51.9}, {"Month": "Dec", "Year": 1994, "Avg Temp": 42.6}, {"Month": "Jan", "Year": 1995, "Avg Temp": 39.0}, {"Month": "Feb", "Year": 1995, "Avg Temp": 33.1}, {"Month": "Mar", "Year": 1995, "Avg Temp": 47.8}, {"Month": "Apr", "Year": 1995, "Avg Temp": 55.2}, {"Month": "May", "Year": 1995, "Avg Temp": 64.5}, {"Month": "Jun", "Year": 1995, "Avg Temp": 74.6}, {"Month": "Jul", "Year": 1995, "Avg Temp": 81.5}, {"Month": "Aug", "Year": 1995, "Avg Temp": 80.1}, {"Month": "Sep", "Year": 1995, "Avg Temp": 70.4}, {"Month": "Oct", "Year": 1995, "Avg Temp": 61.0}, {"Month": "Nov", "Year": 1995, "Avg Temp": 42.6}, {"Month": "Dec", "Year": 1995, "Avg Temp": 33.9}, {"Month": "Jan", "Year": 1996, "Avg Temp": 31.7}, {"Month": "Feb", "Year": 1996, "Avg Temp": 35.7}, {"Month": "Mar", "Year": 1996, "Avg Temp": 39.9}, {"Month": "Apr", "Year": 1996, "Avg Temp": 54.0}, {"Month": "May", "Year": 1996, "Avg Temp": 60.6}, {"Month": "Jun", "Year": 1996, "Avg Temp": 73.3}, {"Month": "Jul", "Year": 1996, "Avg Temp": 74.3}, {"Month": "Aug", "Year": 1996, "Avg Temp": 73.1}, {"Month": "Sep", "Year": 1996, "Avg Temp": 67.8}, {"Month": "Oct", "Year": 1996, "Avg Temp": 55.6}, {"Month": "Nov", "Year": 1996, "Avg Temp": 40.2}, {"Month": "Dec", "Year": 1996, "Avg Temp": 39.6}, {"Month": "Jan", "Year": 1997, "Avg Temp": 32.7}, {"Month": "Feb", "Year": 1997, "Avg Temp": 40.9}, {"Month": "Mar", "Year": 1997, "Avg Temp": 45.5}, {"Month": "Apr", "Year": 1997, "Avg Temp": 51.6}, {"Month": "May", "Year": 1997, "Avg Temp": 59.5}, {"Month": "Jun", "Year": 1997, "Avg Temp": 70.1}, {"Month": "Jul", "Year": 1997, "Avg Temp": 77.2}, {"Month": "Aug", "Year": 1997, "Avg Temp": 74.0}, {"Month": "Sep", "Year": 1997, "Avg Temp": 67.3}, {"Month": "Oct", "Year": 1997, "Avg Temp": 56.5}, {"Month": "Nov", "Year": 1997, "Avg Temp": 43.7}, {"Month": "Dec", "Year": 1997, "Avg Temp": 38.4}, {"Month": "Jan", "Year": 1998, "Avg Temp": 40.9}, {"Month": "Feb", "Year": 1998, "Avg Temp": 41.7}, {"Month": "Mar", "Year": 1998, "Avg Temp": 45.8}, {"Month": "Apr", "Year": 1998, "Avg Temp": 55.2}, {"Month": "May", "Year": 1998, "Avg Temp": 66.5}, {"Month": "Jun", "Year": 1998, "Avg Temp": 71.7}, {"Month": "Jul", "Year": 1998, "Avg Temp": 76.6}, {"Month": "Aug", "Year": 1998, "Avg Temp": 75.7}, {"Month": "Sep", "Year": 1998, "Avg Temp": 71.7}, {"Month": "Oct", "Year": 1998, "Avg Temp": 56.2}, {"Month": "Nov", "Year": 1998, "Avg Temp": 46.1}, {"Month": "Dec", "Year": 1998, "Avg Temp": 41.0}, {"Month": "Jan", "Year": 1999, "Avg Temp": 35.1}, {"Month": "Feb", "Year": 1999, "Avg Temp": 37.6}, {"Month": "Mar", "Year": 1999, "Avg Temp": 41.8}, {"Month": "Apr", "Year": 1999, "Avg Temp": 53.1}, {"Month": "May", "Year": 1999, "Avg Temp": 64.2}, {"Month": "Jun", "Year": 1999, "Avg Temp": 71.5}, {"Month": "Jul", "Year": 1999, "Avg Temp": 80.0}, {"Month": "Aug", "Year": 1999, "Avg Temp": 75.7}, {"Month": "Sep", "Year": 1999, "Avg Temp": 68.1}, {"Month": "Oct", "Year": 1999, "Avg Temp": 53.9}, {"Month": "Nov", "Year": 1999, "Avg Temp": 49.9}, {"Month": "Dec", "Year": 1999, "Avg Temp": 39.1}, {"Month": "Jan", "Year": 2000, "Avg Temp": 32.5}, {"Month": "Feb", "Year": 2000, "Avg Temp": 38.0}, {"Month": "Mar", "Year": 2000, "Avg Temp": 48.5}, {"Month": "Apr", "Year": 2000, "Avg Temp": 52.9}, {"Month": "May", "Year": 2000, "Avg Temp": 64.7}, {"Month": "Jun", "Year": 2000, "Avg Temp": 72.8}, {"Month": "Jul", "Year": 2000, "Avg Temp": 72.7}, {"Month": "Aug", "Year": 2000, "Avg Temp": 73.4}, {"Month": "Sep", "Year": 2000, "Avg Temp": 65.3}, {"Month": "Oct", "Year": 2000, "Avg Temp": 57.1}, {"Month": "Nov", "Year": 2000, "Avg Temp": 44.2}, {"Month": "Dec", "Year": 2000, "Avg Temp": 30.0}, {"Month": "Jan", "Year": 2001, "Avg Temp": 33.0}, {"Month": "Feb", "Year": 2001, "Avg Temp": 38.5}, {"Month": "Mar", "Year": 2001, "Avg Temp": 41.7}, {"Month": "Apr", "Year": 2001, "Avg Temp": 55.4}, {"Month": "May", "Year": 2001, "Avg Temp": 63.4}, {"Month": "Jun", "Year": 2001, "Avg Temp": 74.0}, {"Month": "Jul", "Year": 2001, "Avg Temp": 72.8}, {"Month": "Aug", "Year": 2001, "Avg Temp": 77.0}, {"Month": "Sep", "Year": 2001, "Avg Temp": 65.2}, {"Month": "Oct", "Year": 2001, "Avg Temp": 55.9}, {"Month": "Nov", "Year": 2001, "Avg Temp": 50.7}, {"Month": "Dec", "Year": 2001, "Avg Temp": 42.1}, {"Month": "Jan", "Year": 2002, "Avg Temp": 39.1}, {"Month": "Feb", "Year": 2002, "Avg Temp": 39.3}, {"Month": "Mar", "Year": 2002, "Avg Temp": 45.0}, {"Month": "Apr", "Year": 2002, "Avg Temp": 56.7}, {"Month": "May", "Year": 2002, "Avg Temp": 62.2}, {"Month": "Jun", "Year": 2002, "Avg Temp": 73.8}, {"Month": "Jul", "Year": 2002, "Avg Temp": 78.6}, {"Month": "Aug", "Year": 2002, "Avg Temp": 78.4}, {"Month": "Sep", "Year": 2002, "Avg Temp": 69.5}, {"Month": "Oct", "Year": 2002, "Avg Temp": 56.0}, {"Month": "Nov", "Year": 2002, "Avg Temp": 44.4}, {"Month": "Dec", "Year": 2002, "Avg Temp": 34.3}, {"Month": "Jan", "Year": 2003, "Avg Temp": 28.3}, {"Month": "Feb", "Year": 2003, "Avg Temp": 30.2}, {"Month": "Mar", "Year": 2003, "Avg Temp": 43.9}, {"Month": "Apr", "Year": 2003, "Avg Temp": 52.7}, {"Month": "May", "Year": 2003, "Avg Temp": 59.3}, {"Month": "Jun", "Year": 2003, "Avg Temp": 69.8}, {"Month": "Jul", "Year": 2003, "Avg Temp": 75.6}, {"Month": "Aug", "Year": 2003, "Avg Temp": 76.3}, {"Month": "Sep", "Year": 2003, "Avg Temp": 68.0}, {"Month": "Oct", "Year": 2003, "Avg Temp": 55.1}, {"Month": "Nov", "Year": 2003, "Avg Temp": 50.6}, {"Month": "Dec", "Year": 2003, "Avg Temp": 36.4}, {"Month": "Jan", "Year": 2004, "Avg Temp": 27.6}, {"Month": "Feb", "Year": 2004, "Avg Temp": 34.8}, {"Month": "Mar", "Year": 2004, "Avg Temp": 45.6}, {"Month": "Apr", "Year": 2004, "Avg Temp": 54.7}, {"Month": "May", "Year": 2004, "Avg Temp": 69.8}, {"Month": "Jun", "Year": 2004, "Avg Temp": 70.9}, {"Month": "Jul", "Year": 2004, "Avg Temp": 76.2}, {"Month": "Aug", "Year": 2004, "Avg Temp": 74.2}, {"Month": "Sep", "Year": 2004, "Avg Temp": 69.4}, {"Month": "Oct", "Year": 2004, "Avg Temp": 55.4}, {"Month": "Nov", "Year": 2004, "Avg Temp": 48.5}, {"Month": "Dec", "Year": 2004, "Avg Temp": 37.5}, {"Month": "Jan", "Year": 2005, "Avg Temp": 34.1}, {"Month": "Feb", "Year": 2005, "Avg Temp": 36.7}, {"Month": "Mar", "Year": 2005, "Avg Temp": 40.6}, {"Month": "Apr", "Year": 2005, "Avg Temp": 55.2}, {"Month": "May", "Year": 2005, "Avg Temp": 59.2}, {"Month": "Jun", "Year": 2005, "Avg Temp": 73.6}, {"Month": "Jul", "Year": 2005, "Avg Temp": 77.9}, {"Month": "Aug", "Year": 2005, "Avg Temp": 77.6}, {"Month": "Sep", "Year": 2005, "Avg Temp": 72.0}, {"Month": "Oct", "Year": 2005, "Avg Temp": 57.8}, {"Month": "Nov", "Year": 2005, "Avg Temp": 48.1}, {"Month": "Dec", "Year": 2005, "Avg Temp": 34.0}, {"Month": "Jan", "Year": 2006, "Avg Temp": 41.5}, {"Month": "Feb", "Year": 2006, "Avg Temp": 36.1}, {"Month": "Mar", "Year": 2006, "Avg Temp": 45.6}, {"Month": "Apr", "Year": 2006, "Avg Temp": 57.4}, {"Month": "May", "Year": 2006, "Avg Temp": 63.3}, {"Month": "Jun", "Year": 2006, "Avg Temp": 73.1}, {"Month": "Jul", "Year": 2006, "Avg Temp": 79.8}, {"Month": "Aug", "Year": 2006, "Avg Temp": 78.4}, {"Month": "Sep", "Year": 2006, "Avg Temp": 65.5}, {"Month": "Oct", "Year": 2006, "Avg Temp": 55.1}, {"Month": "Nov", "Year": 2006, "Avg Temp": 49.6}, {"Month": "Dec", "Year": 2006, "Avg Temp": 42.4}, {"Month": "Jan", "Year": 2007, "Avg Temp": 38.7}, {"Month": "Feb", "Year": 2007, "Avg Temp": 29.1}, {"Month": "Mar", "Year": 2007, "Avg Temp": 45.1}, {"Month": "Apr", "Year": 2007, "Avg Temp": 51.4}, {"Month": "May", "Year": 2007, "Avg Temp": 65.5}, {"Month": "Jun", "Year": 2007, "Avg Temp": 73.7}, {"Month": "Jul", "Year": 2007, "Avg Temp": 76.9}, {"Month": "Aug", "Year": 2007, "Avg Temp": 77.5}, {"Month": "Sep", "Year": 2007, "Avg Temp": 70.6}, {"Month": "Oct", "Year": 2007, "Avg Temp": 63.4}, {"Month": "Nov", "Year": 2007, "Avg Temp": 46.2}, {"Month": "Dec", "Year": 2007, "Avg Temp": 37.8}, {"Month": "Jan", "Year": 2008, "Avg Temp": 35.4}, {"Month": "Feb", "Year": 2008, "Avg Temp": 37.1}, {"Month": "Mar", "Year": 2008, "Avg Temp": 45.0}, {"Month": "Apr", "Year": 2008, "Avg Temp": 55.8}, {"Month": "May", "Year": 2008, "Avg Temp": 60.5}, {"Month": "Jun", "Year": 2008, "Avg Temp": 75.3}, {"Month": "Jul", "Year": 2008, "Avg Temp": 77.5}, {"Month": "Aug", "Year": 2008, "Avg Temp": 73.6}, {"Month": "Sep", "Year": 2008, "Avg Temp": 69.4}, {"Month": "Oct", "Year": 2008, "Avg Temp": 55.5}, {"Month": "Nov", "Year": 2008, "Avg Temp": 45.4}, {"Month": "Dec", "Year": 2008, "Avg Temp": 38.5}, {"Month": "Jan", "Year": 2009, "Avg Temp": 29.3}, {"Month": "Feb", "Year": 2009, "Avg Temp": 37.4}, {"Month": "Mar", "Year": 2009, "Avg Temp": 43.1}, {"Month": "Apr", "Year": 2009, "Avg Temp": 54.9}, {"Month": "May", "Year": 2009, "Avg Temp": 63.7}, {"Month": "Jun", "Year": 2009, "Avg Temp": 71.4}, {"Month": "Jul", "Year": 2009, "Avg Temp": 74.6}, {"Month": "Aug", "Year": 2009, "Avg Temp": 76.6}, {"Month": "Sep", "Year": 2009, "Avg Temp": 66.6}, {"Month": "Oct", "Year": 2009, "Avg Temp": 55.3}, {"Month": "Nov", "Year": 2009, "Avg Temp": 49.7}, {"Month": "Dec", "Year": 2009, "Avg Temp": 34.8}, {"Month": "Jan", "Year": 2010, "Avg Temp": 32.7}, {"Month": "Feb", "Year": 2010, "Avg Temp": 30.9}, {"Month": "Mar", "Year": 2010, "Avg Temp": 48.5}, {"Month": "Apr", "Year": 2010, "Avg Temp": 57.1}, {"Month": "May", "Year": 2010, "Avg Temp": 67.3}, {"Month": "Jun", "Year": 2010, "Avg Temp": 78.8}, {"Month": "Jul", "Year": 2010, "Avg Temp": 81.5}, {"Month": "Aug", "Year": 2010, "Avg Temp": 77.4}, {"Month": "Sep", "Year": 2010, "Avg Temp": 71.0}, {"Month": "Oct", "Year": 2010, "Avg Temp": 57.6}, {"Month": "Nov", "Year": 2010, "Avg Temp": 47.2}, {"Month": "Dec", "Year": 2010, "Avg Temp": 32.4}, {"Month": "Jan", "Year": 2011, "Avg Temp": 30.2}, {"Month": "Feb", "Year": 2011, "Avg Temp": 38.5}, {"Month": "Mar", "Year": 2011, "Avg Temp": 44.3}, {"Month": "Apr", "Year": 2011, "Avg Temp": 57.7}, {"Month": "May", "Year": 2011, "Avg Temp": 67.2}, {"Month": "Jun", "Year": 2011, "Avg Temp": 75.7}, {"Month": "Jul", "Year": 2011, "Avg Temp": 81.7}, {"Month": "Aug", "Year": 2011, "Avg Temp": 75.9}, {"Month": "Sep", "Year": 2011, "Avg Temp": 69.3}, {"Month": "Oct", "Year": 2011, "Avg Temp": 56.6}, {"Month": "Nov", "Year": 2011, "Avg Temp": 50.5}, {"Month": "Dec", "Year": 2011, "Avg Temp": 42.2}, {"Month": "Jan", "Year": 2012, "Avg Temp": 38.3}, {"Month": "Feb", "Year": 2012, "Avg Temp": 41.6}, {"Month": "Mar", "Year": 2012, "Avg Temp": 53.7}, {"Month": "Apr", "Year": 2012, "Avg Temp": 55.3}, {"Month": "May", "Year": 2012, "Avg Temp": 69.0}, {"Month": "Jun", "Year": 2012, "Avg Temp": 73.6}, {"Month": "Jul", "Year": 2012, "Avg Temp": 81.4}, {"Month": "Aug", "Year": 2012, "Avg Temp": 77.3}, {"Month": "Sep", "Year": 2012, "Avg Temp": 69.5}, {"Month": "Oct", "Year": 2012, "Avg Temp": 58.3}, {"Month": "Nov", "Year": 2012, "Avg Temp": 42.9}, {"Month": "Dec", "Year": 2012, "Avg Temp": 42.7}, {"Month": "Jan", "Year": 2013, "Avg Temp": 36.9}, {"Month": "Feb", "Year": 2013, "Avg Temp": 35.0}, {"Month": "Mar", "Year": 2013, "Avg Temp": 40.6}, {"Month": "Apr", "Year": 2013, "Avg Temp": 55.3}, {"Month": "May", "Year": 2013, "Avg Temp": 63.7}, {"Month": "Jun", "Year": 2013, "Avg Temp": 73.9}, {"Month": "Jul", "Year": 2013, "Avg Temp": 79.0}, {"Month": "Aug", "Year": 2013, "Avg Temp": 74.2}, {"Month": "Sep", "Year": 2013, "Avg Temp": 67.7}, {"Month": "Oct", "Year": 2013, "Avg Temp": 58.8}, {"Month": "Nov", "Year": 2013, "Avg Temp": 43.6}, {"Month": "Dec", "Year": 2013, "Avg Temp": 39.6}, {"Month": "Jan", "Year": 2014, "Avg Temp": 27.4}, {"Month": "Feb", "Year": 2014, "Avg Temp": 32.9}, {"Month": "Mar", "Year": 2014, "Avg Temp": 38.5}, {"Month": "Apr", "Year": 2014, "Avg Temp": 53.0}, {"Month": "May", "Year": 2014, "Avg Temp": 64.9}, {"Month": "Jun", "Year": 2014, "Avg Temp": 73.2}, {"Month": "Jul", "Year": 2014, "Avg Temp": 75.6}, {"Month": "Aug", "Year": 2014, "Avg Temp": 72.5}, {"Month": "Sep", "Year": 2014, "Avg Temp": 68.7}, {"Month": "Oct", "Year": 2014, "Avg Temp": 58.2}, {"Month": "Nov", "Year": 2014, "Avg Temp": 43.4}, {"Month": "Dec", "Year": 2014, "Avg Temp": 39.9}, {"Month": "Jan", "Year": 2015, "Avg Temp": 30.8}, {"Month": "Feb", "Year": 2015, "Avg Temp": 25.3}, {"Month": "Mar", "Year": 2015, "Avg Temp": 39.7}, {"Month": "Apr", "Year": 2015, "Avg Temp": 54.6}, {"Month": "May", "Year": 2015, "Avg Temp": 69.1}, {"Month": "Jun", "Year": 2015, "Avg Temp": 74.1}, {"Month": "Jul", "Year": 2015, "Avg Temp": 77.0}, {"Month": "Aug", "Year": 2015, "Avg Temp": 75.1}, {"Month": "Sep", "Year": 2015, "Avg Temp": 71.9}, {"Month": "Oct", "Year": 2015, "Avg Temp": 55.3}, {"Month": "Nov", "Year": 2015, "Avg Temp": 50.9}, {"Month": "Dec", "Year": 2015, "Avg Temp": 49.0}, {"Month": "Jan", "Year": 2016, "Avg Temp": 31.9}, {"Month": "Feb", "Year": 2016, "Avg Temp": 37.4}, {"Month": "Mar", "Year": 2016, "Avg Temp": 50.0}, {"Month": "Apr", "Year": 2016, "Avg Temp": 54.0}, {"Month": "May", "Year": 2016, "Avg Temp": 61.5}, {"Month": "Jun", "Year": 2016, "Avg Temp": 73.0}, {"Month": "Jul", "Year": 2016, "Avg Temp": 79.7}, {"Month": "Aug", "Year": 2016, "Avg Temp": 79.1}, {"Month": "Sep", "Year": 2016, "Avg Temp": 72.3}, {"Month": "Oct", "Year": 2016, "Avg Temp": 59.6}, {"Month": "Nov", "Year": 2016, "Avg Temp": 48.6}, {"Month": "Dec", "Year": 2016, "Avg Temp": 38.3}, {"Month": "Jan", "Year": 2017, "Avg Temp": 39.0}, {"Month": "Feb", "Year": 2017, "Avg Temp": 44.2}, {"Month": "Mar", "Year": 2017, "Avg Temp": 43.9}, {"Month": "Apr", "Year": 2017, "Avg Temp": 60.3}, {"Month": "May", "Year": 2017, "Avg Temp": 62.3}, {"Month": "Jun", "Year": 2017, "Avg Temp": 73.7}, {"Month": "Jul", "Year": 2017, "Avg Temp": 78.7}, {"Month": "Aug", "Year": 2017, "Avg Temp": 73.5}, {"Month": "Sep", "Year": 2017, "Avg Temp": 69.1}, {"Month": "Oct", "Year": 2017, "Avg Temp": 61.6}, {"Month": "Nov", "Year": 2017, "Avg Temp": 46.2}, {"Month": "Dec", "Year": 2017, "Avg Temp": 35.5}, {"Month": "Jan", "Year": 2018, "Avg Temp": 32.0}, {"Month": "Feb", "Year": 2018, "Avg Temp": 41.8}, {"Month": "Mar", "Year": 2018, "Avg Temp": 40.2}, {"Month": "Apr", "Year": 2018, "Avg Temp": 52.1}, {"Month": "May", "Year": 2018, "Avg Temp": 69.6}, {"Month": "Jun", "Year": 2018, "Avg Temp": 72.6}, {"Month": "Jul", "Year": 2018, "Avg Temp": 77.8}, {"Month": "Aug", "Year": 2018, "Avg Temp": 78.4}, {"Month": "Sep", "Year": 2018, "Avg Temp": 73.0}, {"Month": "Oct", "Year": 2018, "Avg Temp": 59.3}, {"Month": "Nov", "Year": 2018, "Avg Temp": 43.6}, {"Month": "Dec", "Year": 2018, "Avg Temp": 39.7}, {"Month": "Jan", "Year": 2019, "Avg Temp": 33.5}, {"Month": "Feb", "Year": 2019, "Avg Temp": 37.8}, {"Month": "Mar", "Year": 2019, "Avg Temp": 43.0}, {"Month": "Apr", "Year": 2019, "Avg Temp": 59.5}, {"Month": "May", "Year": 2019, "Avg Temp": 68.3}, {"Month": "Jun", "Year": 2019, "Avg Temp": 75.3}, {"Month": "Jul", "Year": 2019, "Avg Temp": 80.8}, {"Month": "Aug", "Year": 2019, "Avg Temp": 77.9}, {"Month": "Sep", "Year": 2019, "Avg Temp": 73.8}, {"Month": "Oct", "Year": 2019, "Avg Temp": 62.2}, {"Month": "Nov", "Year": 2019, "Avg Temp": 44.3}, {"Month": "Dec", "Year": 2019, "Avg Temp": 39.9}, {"Month": "Jan", "Year": 2020, "Avg Temp": 40.2}, {"Month": "Feb", "Year": 2020, "Avg Temp": 42.0}, {"Month": "Mar", "Year": 2020, "Avg Temp": 50.9}, {"Month": "Apr", "Year": 2020, "Avg Temp": 53.0}, {"Month": "May", "Year": 2020, "Avg Temp": 62.1}, {"Month": "Jun", "Year": 2020, "Avg Temp": 75.1}, {"Month": "Jul", "Year": 2020, "Avg Temp": 82.6}, {"Month": "Aug", "Year": 2020, "Avg Temp": 78.7}, {"Month": "Sep", "Year": 2020, "Avg Temp": 68.8}, {"Month": "Oct", "Year": 2020, "Avg Temp": 59.7}, {"Month": "Nov", "Year": 2020, "Avg Temp": 52.4}, {"Month": "Dec", "Year": 2020, "Avg Temp": 39.4}]}}, {"mode": "vega-lite"});
</script>



# Adding clustering

## Re-ordering rows and columns

In many contexts, especially bioinformatics, heatmaps are used to display similarities between units, using cluster analysis. Typically hierarchical clustering is used.

We will use a breast cancer data set, and look to see if there are individuals who have similar profiles across the variables recorded, and if that might be related to outcome.



```python
from sklearn.datasets import load_breast_cancer
bc_data = load_breast_cancer()
data = pd.DataFrame(bc_data.data, columns = bc_data.feature_names)
data.head()
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
      <th>mean radius</th>
      <th>mean texture</th>
      <th>mean perimeter</th>
      <th>mean area</th>
      <th>mean smoothness</th>
      <th>mean compactness</th>
      <th>mean concavity</th>
      <th>mean concave points</th>
      <th>mean symmetry</th>
      <th>mean fractal dimension</th>
      <th>radius error</th>
      <th>texture error</th>
      <th>perimeter error</th>
      <th>area error</th>
      <th>smoothness error</th>
      <th>compactness error</th>
      <th>concavity error</th>
      <th>concave points error</th>
      <th>symmetry error</th>
      <th>fractal dimension error</th>
      <th>worst radius</th>
      <th>worst texture</th>
      <th>worst perimeter</th>
      <th>worst area</th>
      <th>worst smoothness</th>
      <th>worst compactness</th>
      <th>worst concavity</th>
      <th>worst concave points</th>
      <th>worst symmetry</th>
      <th>worst fractal dimension</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17.99</td>
      <td>10.38</td>
      <td>122.80</td>
      <td>1001.0</td>
      <td>0.11840</td>
      <td>0.27760</td>
      <td>0.3001</td>
      <td>0.14710</td>
      <td>0.2419</td>
      <td>0.07871</td>
      <td>1.0950</td>
      <td>0.9053</td>
      <td>8.589</td>
      <td>153.40</td>
      <td>0.006399</td>
      <td>0.04904</td>
      <td>0.05373</td>
      <td>0.01587</td>
      <td>0.03003</td>
      <td>0.006193</td>
      <td>25.38</td>
      <td>17.33</td>
      <td>184.60</td>
      <td>2019.0</td>
      <td>0.1622</td>
      <td>0.6656</td>
      <td>0.7119</td>
      <td>0.2654</td>
      <td>0.4601</td>
      <td>0.11890</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20.57</td>
      <td>17.77</td>
      <td>132.90</td>
      <td>1326.0</td>
      <td>0.08474</td>
      <td>0.07864</td>
      <td>0.0869</td>
      <td>0.07017</td>
      <td>0.1812</td>
      <td>0.05667</td>
      <td>0.5435</td>
      <td>0.7339</td>
      <td>3.398</td>
      <td>74.08</td>
      <td>0.005225</td>
      <td>0.01308</td>
      <td>0.01860</td>
      <td>0.01340</td>
      <td>0.01389</td>
      <td>0.003532</td>
      <td>24.99</td>
      <td>23.41</td>
      <td>158.80</td>
      <td>1956.0</td>
      <td>0.1238</td>
      <td>0.1866</td>
      <td>0.2416</td>
      <td>0.1860</td>
      <td>0.2750</td>
      <td>0.08902</td>
    </tr>
    <tr>
      <th>2</th>
      <td>19.69</td>
      <td>21.25</td>
      <td>130.00</td>
      <td>1203.0</td>
      <td>0.10960</td>
      <td>0.15990</td>
      <td>0.1974</td>
      <td>0.12790</td>
      <td>0.2069</td>
      <td>0.05999</td>
      <td>0.7456</td>
      <td>0.7869</td>
      <td>4.585</td>
      <td>94.03</td>
      <td>0.006150</td>
      <td>0.04006</td>
      <td>0.03832</td>
      <td>0.02058</td>
      <td>0.02250</td>
      <td>0.004571</td>
      <td>23.57</td>
      <td>25.53</td>
      <td>152.50</td>
      <td>1709.0</td>
      <td>0.1444</td>
      <td>0.4245</td>
      <td>0.4504</td>
      <td>0.2430</td>
      <td>0.3613</td>
      <td>0.08758</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.42</td>
      <td>20.38</td>
      <td>77.58</td>
      <td>386.1</td>
      <td>0.14250</td>
      <td>0.28390</td>
      <td>0.2414</td>
      <td>0.10520</td>
      <td>0.2597</td>
      <td>0.09744</td>
      <td>0.4956</td>
      <td>1.1560</td>
      <td>3.445</td>
      <td>27.23</td>
      <td>0.009110</td>
      <td>0.07458</td>
      <td>0.05661</td>
      <td>0.01867</td>
      <td>0.05963</td>
      <td>0.009208</td>
      <td>14.91</td>
      <td>26.50</td>
      <td>98.87</td>
      <td>567.7</td>
      <td>0.2098</td>
      <td>0.8663</td>
      <td>0.6869</td>
      <td>0.2575</td>
      <td>0.6638</td>
      <td>0.17300</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20.29</td>
      <td>14.34</td>
      <td>135.10</td>
      <td>1297.0</td>
      <td>0.10030</td>
      <td>0.13280</td>
      <td>0.1980</td>
      <td>0.10430</td>
      <td>0.1809</td>
      <td>0.05883</td>
      <td>0.7572</td>
      <td>0.7813</td>
      <td>5.438</td>
      <td>94.44</td>
      <td>0.011490</td>
      <td>0.02461</td>
      <td>0.05688</td>
      <td>0.01885</td>
      <td>0.01756</td>
      <td>0.005115</td>
      <td>22.54</td>
      <td>16.67</td>
      <td>152.20</td>
      <td>1575.0</td>
      <td>0.1374</td>
      <td>0.2050</td>
      <td>0.4000</td>
      <td>0.1625</td>
      <td>0.2364</td>
      <td>0.07678</td>
    </tr>
  </tbody>
</table>
</div>



## breast cancer: creating the heatmap

In **seaborn**, the `clustermap` function takes care of the clustering for us. Note that we are scaling the rows so that they have mean 0 and variance 1, to enable a better view of the differences in patterns. We are also using the correlation metric (1 - correlation) to cluster rows and columns.


```python
fig = sns.clustermap(data, standard_scale=1, metric='correlation', method='average',cmap='RdBu',);
fig.savefig('img/heatmap_cluster1.png')
show_fig2('img/heatmap_cluster1.png')
```

    /Users/abhijit/opt/anaconda3/envs/biof440/lib/python3.8/site-packages/seaborn/matrix.py:649: UserWarning:
    
    Clustering large matrix with scipy. Installing `fastcluster` may give better performance.
    




<iframe
    width="100%"
    height="500"
    src="img/heatmap_cluster1.png"
    frameborder="0"
    allowfullscreen
></iframe>




    
![svg](week6_heatmap_files/week6_heatmap_15_2.svg)
    


## breast cancer: adding to the heatmap

We will add a column to the heatmap that color-codes the outcomes, so we can see if the clustering aligns with the outcomes.


```python
color_dict = dict(zip(np.unique(bc_data.target), np.array(['g','skyblue'])))
target_df = pd.DataFrame({'target': bc_data.target})
row_colors = target_df.target.map(color_dict)
```

## breast cancer: adding to the heatmap


```python
sns.clustermap(data, standard_scale=1, metric='correlation', method='average', cmap = 'RdBu',row_colors=row_colors);
```




    <seaborn.matrix.ClusterGrid at 0x7fd1cb74f910>




    
![svg](week6_heatmap_files/week6_heatmap_19_1.svg)
    


# Embellishing the heatmap

## Adding marginal histograms and annotation

We will use a data set of measles cases in the US from 1930 to 2000 to demonstrate how to create marginal histograms around a heatmap. 

We can first read in the data and do a bit of data munging.


```python
measles = pd.read_csv('data/measles.csv')
measles['state'] = measles['state'].str.title().str.replace('.', ' ')
measles = measles.set_index('state')
measles.head()
```

    <ipython-input-389-12b6c101491b>:2: FutureWarning:
    
    The default value of regex will change from True to False in a future version. In addition, single character regular expressions will*not* be treated as literal strings when regex=True.
    





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
      <th>1930</th>
      <th>1931</th>
      <th>1932</th>
      <th>1933</th>
      <th>1934</th>
      <th>1935</th>
      <th>1936</th>
      <th>1937</th>
      <th>1938</th>
      <th>1939</th>
      <th>1940</th>
      <th>1941</th>
      <th>1942</th>
      <th>1943</th>
      <th>1944</th>
      <th>1945</th>
      <th>1946</th>
      <th>1947</th>
      <th>1948</th>
      <th>1949</th>
      <th>1950</th>
      <th>1951</th>
      <th>1952</th>
      <th>1953</th>
      <th>1954</th>
      <th>1955</th>
      <th>1956</th>
      <th>1957</th>
      <th>1958</th>
      <th>1959</th>
      <th>1960</th>
      <th>1961</th>
      <th>1962</th>
      <th>1963</th>
      <th>1964</th>
      <th>1965</th>
      <th>1966</th>
      <th>1967</th>
      <th>1968</th>
      <th>1969</th>
      <th>1970</th>
      <th>1971</th>
      <th>1972</th>
      <th>1973</th>
      <th>1974</th>
      <th>1975</th>
      <th>1976</th>
      <th>1977</th>
      <th>1978</th>
      <th>1979</th>
      <th>1980</th>
      <th>1981</th>
      <th>1982</th>
      <th>1983</th>
      <th>1984</th>
      <th>1985</th>
      <th>1986</th>
      <th>1987</th>
      <th>1988</th>
      <th>1989</th>
      <th>1990</th>
      <th>1991</th>
      <th>1992</th>
      <th>1993</th>
      <th>1994</th>
      <th>1995</th>
      <th>1996</th>
      <th>1997</th>
      <th>1998</th>
      <th>1999</th>
      <th>2000</th>
      <th>2001</th>
    </tr>
    <tr>
      <th>state</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>Alabama</th>
      <td>4389</td>
      <td>8934</td>
      <td>270</td>
      <td>1735</td>
      <td>15849</td>
      <td>7214</td>
      <td>572</td>
      <td>620</td>
      <td>13511</td>
      <td>4381</td>
      <td>3052</td>
      <td>8696</td>
      <td>3564</td>
      <td>3865</td>
      <td>7199</td>
      <td>339</td>
      <td>3986</td>
      <td>3693</td>
      <td>2058</td>
      <td>11066</td>
      <td>1503</td>
      <td>3144</td>
      <td>11878</td>
      <td>2799</td>
      <td>8451</td>
      <td>2061</td>
      <td>7117</td>
      <td>9264</td>
      <td>7664</td>
      <td>3467</td>
      <td>2075</td>
      <td>2588</td>
      <td>2379</td>
      <td>1165</td>
      <td>18140</td>
      <td>2346</td>
      <td>1813</td>
      <td>1345</td>
      <td>158</td>
      <td>12</td>
      <td>486</td>
      <td>2086</td>
      <td>142</td>
      <td>19</td>
      <td>21</td>
      <td>5</td>
      <td>0</td>
      <td>79</td>
      <td>60</td>
      <td>94</td>
      <td>22</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>14</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1487</td>
      <td>536</td>
      <td>2511</td>
      <td>958</td>
      <td>1259</td>
      <td>1829</td>
      <td>1456</td>
      <td>1002</td>
      <td>1406</td>
      <td>1849</td>
      <td>1169</td>
      <td>215</td>
      <td>641</td>
      <td>148</td>
      <td>4</td>
      <td>22</td>
      <td>73</td>
      <td>40</td>
      <td>7</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>11</td>
      <td>49</td>
      <td>2</td>
      <td>18</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>American Samoa</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>2107</td>
      <td>2135</td>
      <td>86</td>
      <td>1261</td>
      <td>1022</td>
      <td>586</td>
      <td>2378</td>
      <td>3793</td>
      <td>604</td>
      <td>479</td>
      <td>2078</td>
      <td>2929</td>
      <td>3813</td>
      <td>1002</td>
      <td>4641</td>
      <td>332</td>
      <td>3274</td>
      <td>1464</td>
      <td>4303</td>
      <td>3795</td>
      <td>2389</td>
      <td>10454</td>
      <td>2515</td>
      <td>4934</td>
      <td>4959</td>
      <td>10086</td>
      <td>6785</td>
      <td>7659</td>
      <td>9845</td>
      <td>9067</td>
      <td>4305</td>
      <td>7868</td>
      <td>6350</td>
      <td>8878</td>
      <td>6328</td>
      <td>1593</td>
      <td>5536</td>
      <td>1022</td>
      <td>243</td>
      <td>561</td>
      <td>1006</td>
      <td>515</td>
      <td>868</td>
      <td>11</td>
      <td>21</td>
      <td>83</td>
      <td>233</td>
      <td>242</td>
      <td>58</td>
      <td>84</td>
      <td>327</td>
      <td>7</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>38</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>61</td>
      <td>52</td>
      <td>0</td>
      <td>3</td>
      <td>9</td>
      <td>12</td>
      <td>8</td>
      <td>9</td>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>996</td>
      <td>849</td>
      <td>99</td>
      <td>5438</td>
      <td>7222</td>
      <td>1518</td>
      <td>107</td>
      <td>322</td>
      <td>6690</td>
      <td>1724</td>
      <td>1096</td>
      <td>5474</td>
      <td>4542</td>
      <td>2867</td>
      <td>3780</td>
      <td>1098</td>
      <td>3266</td>
      <td>2414</td>
      <td>3824</td>
      <td>12313</td>
      <td>1739</td>
      <td>7625</td>
      <td>2910</td>
      <td>13079</td>
      <td>2619</td>
      <td>2983</td>
      <td>8637</td>
      <td>1358</td>
      <td>3002</td>
      <td>816</td>
      <td>1596</td>
      <td>1684</td>
      <td>1438</td>
      <td>1453</td>
      <td>1108</td>
      <td>1195</td>
      <td>1379</td>
      <td>1269</td>
      <td>3</td>
      <td>3</td>
      <td>33</td>
      <td>447</td>
      <td>13</td>
      <td>37</td>
      <td>14</td>
      <td>2</td>
      <td>20</td>
      <td>8</td>
      <td>18</td>
      <td>10</td>
      <td>9</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>244</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
measles2 = measles.reset_index().melt(id_vars = 'state',var_name='Year', value_name='count') # Tidying the data
bl = measles2.groupby('state')['count'].sum()
ind = bl.argsort() # Find index order that makes the states ordered by total case
```


```python
# Creating marginal frequency distributions
d1 = measles2.groupby('Year').sum().reset_index()
d2 = measles2.groupby('state').sum().reset_index().sort_values(by='count', ascending=False)
```

## measles: seaborn


```python
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
```


    
![svg](week6_heatmap_files/week6_heatmap_25_0.svg)
    



```python
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
```



<iframe
    width="100%"
    height="500"
    src="img/measles_plotly.html"
    frameborder="0"
    allowfullscreen
></iframe>



## measles: seaborn


```python
show_fig2('img/measles_sns.png')
```



<iframe
    width="100%"
    height="500"
    src="img/measles_sns.png"
    frameborder="0"
    allowfullscreen
></iframe>



## measles: altair


```python
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

```

## measles: altair


```python
show_fig2('img/measles_alt.html')
```



<iframe
    width="100%"
    height="500"
    src="img/measles_alt.html"
    frameborder="0"
    allowfullscreen
></iframe>


