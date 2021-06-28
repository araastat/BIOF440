---
title: "Statistical data visualizations (static)"
author: "Abhijit Dasgupta"
subtitle: "BIOF 440"
---
# Data visualization

## Visualization for analysis

- Tool for understanding datasets
- You ask questions and quickly answer them
- Iterate to develop insights.

## Context is important

A data visualization should be self-contained and be able to express the **context** of the data. 

This makes the visualization **informative**.

![](img/hr.png)

This chart is not novel or fancy, but the annotations make it relevant and contextual

## Improve readability

Data visualizations should be readable. It should be obvious what the chart is about and how to interpret it.

![](img/bad1.png)

![](img/good1.png)


## Some ideas

- Your visualization depends on your audience
    + If the audience is your lab group (has a similar contextual background), then you may not have to provide as much context in your visualization
    + If you audience is a conference or a journal reader, you probably need to have more detail and context within the visualization

- Your visualization needs to reflect the character of the data
    + Continuous <--> categorical <--> binary
    + Dates and times
    + Spatial data (may be related to objects other than maps, like cell structure or organisms)
    + Networked or co-related data

> Design is choice. The theory of the visual display of quantitative information consists of principles that generate design options and that guide choices among options. The principles should not be applied rigidly or in a peevish spirit; they are not logically or mathematically certain; and it is better to violate any principle than to place graceless or inelegant marks on paper. Most principles of design should be greeted with some skepticism, for word authority can dominate our vision, and we may come to see only through the lenses of word authority rather than with our own eyes.
>
> -- <cite>Edward Tufte, The Visual Display of Quantitative Data

## Tufte's Principles of Graphical Integrity

1. Show data variation, not design variation
1. Do not use graphics to quote data out of context
1. Use clear, detailed, thorough labelling.
1. Representation of numbers should be directly proportional to numerical quantities
1. Don't use more dimensions than the data require

## Tufte's Principles of Graphical Integrity

1. Show data variation, not design variation
   - Don't get fancy, let the data speak
1. Do not use graphics to quote data out of context
   - Maintain accuracy
1. Use clear, detailed, thorough labelling.
   - Use annotations to make your point
1. Representation of numbers should be directly proportional to numerical quantities
   - This is essential for fair representation
1. Don't use more dimensions than the data require
   - Be appropriate in use of 3D graphics, for example

## Tufte's Fundamental Principles of Design

   1. Show comparisons
   1. Show causality
   1. Use multivariate data
   1. Completely integrate modes (like text, images, numbers)
   1. Establish credibility
   1. Focus on content

## Nathan Yau's Seven Basic Rules for Making Charts and Graphs

   1. Check the data
   1. Explain encodings
   1. Label axes
   1. Include units
   1. Keep your geometry in check
   1. Include your sources
   1. Consider your audience

### 1) Check the data

<img src="https://flowingdata.com/wp-content/uploads/2010/07/1-check-the-data.jpg">

* This should be obvious
* If your data is weak, your chart is weak
* Start with simple graphs to see if there are any outliers

### 2) Explain encodings

<img src="https://flowingdata.com/wp-content/uploads/2010/07/2-explain-encodings.jpg">

* Don't assume the reader knows what everything means
* Provide a legend
* Label shapes
* Explain color scales

### 3) Label axes

<img src="https://flowingdata.com/wp-content/uploads/2010/07/3-labels-axes.jpg">

* Axes without labels or explanation are just decorationS
* Describe the scale (incremental, exponential, logarithmic?)
* Have axes values start at zero

### 4) Include units

<img src="https://flowingdata.com/wp-content/uploads/2010/07/4-include-units.jpg">

* Numbers without units are meaningless
* Remove the guesswork

### 5) Keep your geometry in check

<img src="https://flowingdata.com/wp-content/uploads/2010/07/5-keep-geometry-in-check.jpg">

* This is something that is immediately noticeable
* Don't use area to compare two units unless they are an area. An increase in a unit squares the area.
* Tip: size circles and other 2D shapes by area, unless it's a bar chart

### 6) Include your sources

<img src="https://flowingdata.com/wp-content/uploads/2010/07/6-sources.jpg">

* This is another obvious one
* Always include the source of your data
* Makes your graphic more reputable
* Allows for others to dig deeper

### 7) Consider your audience

<img src="https://flowingdata.com/wp-content/uploads/2010/07/7-audience.jpg">

* What purpose do your charts have and who are they for?
* Avoid quirky fonts
* Make good design choices

# Data to graphics

## Visual encoding

The basic question in data visualization is how we transform data values into blobs of ink on paper, or more recently, pixels on a screen. 

> All data visualizations map data values into quantifiable features of the resulting graphic. We refer to these as *aesthetics*
>
> -- <cite>Fundamentals of Data Visualization by Claus O. Wilke</cite>

We can also refer to these as **visual encoding**, i.e., how we encode aspects of data visually

## Common aesthetics/encodings

![:scale 50](img/aesthetics.png)



## Common aesthetics/encodings

The choice of aesthetics often will be guided by the kind of data you're trying to visualize, as we said earlier

- Quantitative / continuous
- Categorical ordered
- Categorical unordered
- Time (dates, times, years)

## Common aesthetics/encodings

Type      | Encodings   | Notes
----------|-------------|------
Continuous|x, y, size, color, line width | sequential and divergent color scales|
Ordered categorical | x, y, size, shape, color, line type, line width | sequential and divergent color scales|
Unordered categorical | x, y, shape, color, line type | qualitative color scales |
Time | x, y | |

> Can you think of examples where we can encode data types with different kinds of visualizations?

# Statistical Data Visualization

## Statistical data visualization

In this class we will mainly be dealing with statistical data visualizations, rather than visualizing functions and fixed patterns.

The package **seaborn** will be our main high-level Python tool to enable us to do this.

## seaborn, pandas and matplotlib

- pandas is the main tool to prepare data for visualization. It also has some plotting capabilities
- seaborn is the main tool for statistical visualizations as a high-level tool
- matplotlib is the primary tool for static data visualization in Python
    - Create customizable plots
    - Very granular; can control almost all aspects of a graph

![:scale 75%](img/mpl.png)

## seaborn, pandas and matplotlib

- Both **pandas** plotting and **seaborn** are built on top of **matplotlib**
- Both **pandas** plotting and **seaborn** allow the creation of data visualizations with simpler code
- You can use the capabilities of **matplotlib** to 
    - set up visualizations
    - customize visualizations
    - save visualizations

# Let's get started

## Setting up

We'll use this set of packages almost always for creating static visualizations meant for a paper, poster, or website


```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

%matplotlib inline
plt.style.use("seaborn-whitegrid") # this is a built-in style
mpl.rcParams['figure.figsize'] = (8,6) # Sets default size of graphics in inches
from IPython.display import Image # import images into Jupyter notebooks
```

This will be the usual setup for the material this week

## Starting with basic pandas plots

With **pandas**, we can do quite a bit of basic statistical plotting.

It also allows us to see the direct relationship between the data and visualizations

We can plot from both `Series` and `DataFrame` objects

**pandas** was originally built to work with time series, so a tacit assumption underlying **pandas** plotting is that the index of the `DataFrame` or `Series` is a series of dates or times, and each column is data collected at each of these time points for a particular variable. So a `DataFrame` was assumed to be a set of time series, and the plotting tools were designed accordingly. However, we won't follow that assumption here, since a `DataFrame` is used much more richly in data science.

## Starting with basic pandas plots

Let's start by importing the _cars2018.csv_ into our session


```python
cars = pd.read_csv("data/cars2018.csv")
cars.head()
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
      <th>Model</th>
      <th>Model Index</th>
      <th>Displacement</th>
      <th>Cylinders</th>
      <th>Gears</th>
      <th>Transmission</th>
      <th>MPG</th>
      <th>Aspiration</th>
      <th>Lockup Torque Converter</th>
      <th>Drive</th>
      <th>Max Ethanol</th>
      <th>Recommended Fuel</th>
      <th>Intake Valves Per Cyl</th>
      <th>Exhaust Valves Per Cyl</th>
      <th>Fuel injection</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura NSX</td>
      <td>57</td>
      <td>3.5</td>
      <td>6</td>
      <td>9</td>
      <td>Manual</td>
      <td>21</td>
      <td>Turbocharged/Supercharged</td>
      <td>Y</td>
      <td>All Wheel Drive</td>
      <td>10</td>
      <td>Premium Unleaded Required</td>
      <td>2</td>
      <td>2</td>
      <td>Direct ignition</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ALFA ROMEO 4C</td>
      <td>410</td>
      <td>1.8</td>
      <td>4</td>
      <td>6</td>
      <td>Manual</td>
      <td>28</td>
      <td>Turbocharged/Supercharged</td>
      <td>Y</td>
      <td>2-Wheel Drive, Rear</td>
      <td>10</td>
      <td>Premium Unleaded Required</td>
      <td>2</td>
      <td>2</td>
      <td>Direct ignition</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Audi R8 AWD</td>
      <td>65</td>
      <td>5.2</td>
      <td>10</td>
      <td>7</td>
      <td>Manual</td>
      <td>17</td>
      <td>Naturally Aspirated</td>
      <td>Y</td>
      <td>All Wheel Drive</td>
      <td>15</td>
      <td>Premium Unleaded Recommended</td>
      <td>2</td>
      <td>2</td>
      <td>Direct ignition</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Audi R8 RWD</td>
      <td>71</td>
      <td>5.2</td>
      <td>10</td>
      <td>7</td>
      <td>Manual</td>
      <td>18</td>
      <td>Naturally Aspirated</td>
      <td>Y</td>
      <td>2-Wheel Drive, Rear</td>
      <td>15</td>
      <td>Premium Unleaded Recommended</td>
      <td>2</td>
      <td>2</td>
      <td>Direct ignition</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Audi R8 Spyder AWD</td>
      <td>66</td>
      <td>5.2</td>
      <td>10</td>
      <td>7</td>
      <td>Manual</td>
      <td>17</td>
      <td>Naturally Aspirated</td>
      <td>Y</td>
      <td>All Wheel Drive</td>
      <td>15</td>
      <td>Premium Unleaded Recommended</td>
      <td>2</td>
      <td>2</td>
      <td>Direct ignition</td>
    </tr>
  </tbody>
</table>
</div>



# Visualizing one variable (Continuous)

## Histogram


```python
cars["MPG"].plot(kind="hist");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_41_0.png)
    


> **Note:** Notice the semi-colon after the command. This is to ensure that there is no textual meta-data about the plot that is printed. This is an inheritance from Matlab that has remained. 

## Density plot


```python
cars["MPG"].plot(kind="kde");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_44_0.png)
    


## Box plot


```python
cars["MPG"].plot(kind="box");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_46_0.png)
    


# Visualizing one variable (categorical)

## Frequency barplot

For a frequency barplot, you need to do a bit of data summarization using **pandas**


```python
cars["Cylinders"].value_counts()
```




    4     502
    6     392
    8     195
    12     23
    3      21
    10      8
    5       2
    16      1
    Name: Cylinders, dtype: int64



## Frequency barplot


```python
cars["Cylinders"].value_counts().plot(kind="bar");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_51_0.png)
    


## Frequency barplot

To order the bars by their natural order, we can modify how `value_counts` is computed


```python
cars["Cylinders"].value_counts(sort=False).plot(kind="bar");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_53_0.png)
    


# Visualizing bivariate relationships

## Scatter plot (2 continuous variables)


```python
cars.plot(x="Displacement", y="MPG", kind="scatter");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_56_0.png)
    


## Scatterplot matrix

You can look at inter-relationships between all the continuous variables in a dataset using a scatterplot matrix. We'll use the _penguins_ data, which we can load through the **seaborn** package.


```python
penguins = sns.load_dataset("penguins")
pd.plotting.scatter_matrix(penguins);
```

    /Users/abhijit/opt/anaconda3/envs/biof440/lib/python3.8/site-packages/pandas/plotting/_matplotlib/tools.py:400: MatplotlibDeprecationWarning: 
    The is_first_col function was deprecated in Matplotlib 3.4 and will be removed two minor releases later. Use ax.get_subplotspec().is_first_col() instead.
      if ax.is_first_col():



    
![png](03_01_data_visualization_files/03_01_data_visualization_58_1.png)
    



## Box plots (continuous x categorical)


```python
cars.boxplot(column="MPG", by="Cylinders");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_60_0.png)
    


# An aside about pandas plotting

## Plotting several columns in a DataFrame

Because **pandas** was created to deal with sets of time series, the plotting rules were set up to encode each column into a separate visualization

For example, if you want to look at univariate characteristics of all continuous variables in a DataFrame:


```python
penguins.plot(kind="kde");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_63_0.png)
    


## Plotting several columns in a DataFrame

We'd do better by putting each variable into a separate plot


```python
penguins.plot(kind="kde", subplots=True);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_65_0.png)
    


## Plotting several columns in a DataFrame

Let's put each subplot on its own scale


```python
penguins.plot(kind="kde", subplots=True, sharex=False, layout=(2, 2));
```

    /Users/abhijit/opt/anaconda3/envs/biof440/lib/python3.8/site-packages/pandas/plotting/_matplotlib/tools.py:400: MatplotlibDeprecationWarning: 
    The is_first_col function was deprecated in Matplotlib 3.4 and will be removed two minor releases later. Use ax.get_subplotspec().is_first_col() instead.
      if ax.is_first_col():
    /Users/abhijit/opt/anaconda3/envs/biof440/lib/python3.8/site-packages/pandas/plotting/_matplotlib/tools.py:400: MatplotlibDeprecationWarning: 
    The is_first_col function was deprecated in Matplotlib 3.4 and will be removed two minor releases later. Use ax.get_subplotspec().is_first_col() instead.
      if ax.is_first_col():



    
![png](03_01_data_visualization_files/03_01_data_visualization_67_1.png)
    


## Boxplots of several columns


```python
penguins[["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]].plot(kind="box");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_69_0.png)
    


## Plotting against the index of a Series or DataFrame

With time series, **pandas** stores the time aspect in the index of the `Series` or `DataFrame`. So typically, **pandas** plots each variable against the index for encodings like line plots or bar plots

We saw this in the frequency bar plot, where `value_counts` creates a `Series` with unique values as the index and the values as the frequencies


```python
freqs = penguins["species"].value_counts()

freqs.index
```




    Index(['Adelie', 'Gentoo', 'Chinstrap'], dtype='object')




```python
freqs.values
```




    array([152, 124,  68])




```python
penguins["species"].value_counts().plot(kind="bar")
plt.show()
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_73_0.png)
    


## Another example


```python
import numpy as np

n = np.random.randn(5, 4)
D = pd.DataFrame(n, columns=["A", "B", "C", "D"])
D.head()
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.456751</td>
      <td>0.020078</td>
      <td>-1.110089</td>
      <td>1.511507</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.562469</td>
      <td>0.247687</td>
      <td>0.859611</td>
      <td>-0.651064</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.982073</td>
      <td>-1.917526</td>
      <td>0.173585</td>
      <td>-1.103150</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.105097</td>
      <td>1.599340</td>
      <td>-1.689247</td>
      <td>0.362538</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.408049</td>
      <td>-1.017161</td>
      <td>-1.525200</td>
      <td>1.658364</td>
    </tr>
  </tbody>
</table>
</div>




```python
D.plot(kind="line");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_76_0.png)
    


So we can plot multiple variables on a plot (but does it make sense?)

# seaborn for statistical visualization

## seaborn

Using **pandas**, we see basic encodings, basically just `x` and `y`

**seaborn** gets us a richer set of visual encodings, using relatively straightforward code.

We'll see later how we'd do a similar plot using more granular code from **matplotlib**

## seaborn

The main classes of figures created using **seaborn**: 

![](https://seaborn.pydata.org/_images/function_overview_8_0.png)

## seaborn

**seaborn** allows us to make it easier to create 

- _facets_, i.e., subplots based on unique values of column(s) of the `DataFrame`
- _overlays_, i.e., plots where we can encode unique values of column(s) of a `DataFrame` on the same plot

## seaborn

**seaborn** code follows a general paradigm, where we

- start with a `DataFrame`
- specify the column(s) we want to plot
- specify the column(s) we want to either facet or overlay
- specify the encodings  for the different data elements


```python
sns.set_style("white", {"font.family": "Futura"})
```

## Histograms



```python
sns.displot(
    data=penguins,  # DataFrame
    x="bill_length_mm",  # columns to encode
    kind="hist",  # Type of encoding
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_85_0.png)
    



```python
sns.displot(
    data=penguins,  # DataFrame
    x="bill_length_mm",  # columns to encode
    kind="hist",  # Type of encoding
    hue="species",  # Encode species as colors (hue) and overlay
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_86_0.png)
    


## Histograms


```python
sns.displot(
    data=penguins,  # DataFrame
    x="bill_length_mm",  # columns to encode
    kind="hist",  # Type of encoding
    col="species",  # Encode species as facets, one per column
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_88_0.png)
    



```python
sns.displot(
    data=penguins,  # DataFrame
    x="bill_length_mm",  # columns to encodeS
    kind="hist",  # Type of encoding
    col="species",  # Encode species as facets, one per row
    col_wrap=2,
    height=2.5,
    aspect=1.5,
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_89_0.png)
    


## Density plot


```python
sns.displot(data=penguins, x="bill_length_mm", hue="species", kind="kde");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_91_0.png)
    


## Empirical cumulative distribution plots


```python
sns.displot(data=penguins, x="bill_length_mm", hue="species", kind="ecdf")
plt.show();
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_93_0.png)
    


## Categorical plots


```python
sns.catplot(data=penguins, x="species", kind="count");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_95_0.png)
    


## Relating two continuous variables


```python
sns.relplot(data=penguins, x="bill_length_mm", y="body_mass_g");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_97_0.png)
    



```python
sns.relplot(data=penguins, x="bill_length_mm", y="body_mass_g", hue="species");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_98_0.png)
    



```python
sns.relplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
    hue="species",
    style="species",
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_99_0.png)
    



```python
sns.relplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
    hue="species",
    style="species",
    col="island",
)
```




    <seaborn.axisgrid.FacetGrid at 0x7fc91439feb0>




    
![png](03_01_data_visualization_files/03_01_data_visualization_100_1.png)
    



```python
sns.relplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
    hue="species",
    style="species",
    col="island",
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_101_0.png)
    



```python
sns.relplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
    hue="species",
    style="species",
    col="island",
    col_wrap=2,
    col_order=["Biscoe", "Dream", "Torgersen"],
    height=3,
    aspect=1.5,
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_102_0.png)
    


## Line plots


```python
fmri = sns.load_dataset("fmri")
fmri.head()
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
      <th>subject</th>
      <th>timepoint</th>
      <th>event</th>
      <th>region</th>
      <th>signal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>s13</td>
      <td>18</td>
      <td>stim</td>
      <td>parietal</td>
      <td>-0.017552</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s5</td>
      <td>14</td>
      <td>stim</td>
      <td>parietal</td>
      <td>-0.080883</td>
    </tr>
    <tr>
      <th>2</th>
      <td>s12</td>
      <td>18</td>
      <td>stim</td>
      <td>parietal</td>
      <td>-0.081033</td>
    </tr>
    <tr>
      <th>3</th>
      <td>s11</td>
      <td>18</td>
      <td>stim</td>
      <td>parietal</td>
      <td>-0.046134</td>
    </tr>
    <tr>
      <th>4</th>
      <td>s10</td>
      <td>18</td>
      <td>stim</td>
      <td>parietal</td>
      <td>-0.037970</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.relplot(data=fmri, x="timepoint", y="signal", kind="line");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_105_0.png)
    



```python
sns.relplot(data=fmri, x="timepoint", y="signal", kind="line", hue="event");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_106_0.png)
    



```python
sns.relplot(
    data=fmri, x="timepoint", y="signal", kind="line", hue="event", style="region"
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_107_0.png)
    



```python
sns.relplot(
    data=fmri,
    x="timepoint",
    y="signal",
    kind="line",
    hue="event",
    style="region",
    ci=None,
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_108_0.png)
    



```python
sns.lmplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_109_0.png)
    



```python
sns.lmplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
    lowess=True,
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_110_0.png)
    



```python
sns.lmplot(
    data=penguins,
    x="bill_length_mm",
    y="body_mass_g",
    hue="species",
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_111_0.png)
    


## Categorical plots


```python
diamonds = sns.load_dataset("diamonds")
diamonds.shape
```




    (53940, 10)




```python
sns.catplot(data=diamonds, x="cut", y="price", kind="box");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_114_0.png)
    



```python
cat_order = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
sns.catplot(
    data=diamonds,
    x="cut",
    y="price",
    kind="strip",
    order=cat_order,
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_115_0.png)
    



```python
cat_order = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
sns.catplot(
    data=diamonds,
    x="cut",
    y="price",
    kind="bar",
    order=cat_order,
);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_116_0.png)
    


## Pair plot


```python
sns.pairplot(data=penguins);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_118_0.png)
    



```python
sns.pairplot(data=penguins, hue="species");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_119_0.png)
    



```python
g = sns.PairGrid(penguins, diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=2);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_120_0.png)
    


## Joint plot


```python
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_122_0.png)
    


## Overlaying aesthetics


```python
g = sns.catplot(data=penguins, x="species", y="body_mass_g", kind="violin")
sns.swarmplot(data=penguins, x="species", y="body_mass_g", ax=g.ax, color="black")
g.set_xlabels("Species")
g.set_ylabels("Body mass (g)");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_124_0.png)
    


# Saving your work

## Saving your work

**matplotlib**, and, by extension, **pandas** and **seaborn**, has a large number of backend engines that enables one to save their visualizations in several file formats. 

You can save your work using the `plt.savefig` function


```python
# This will save the last run figure
plt.savefig("penguins.png", transparent=True, dpi=300);
```


    <Figure size 576x432 with 0 Axes>


The type of file will be automatically determined by the last three letters of the file name

+ penguins.png = PNG file
+ penguins.tif = TIFF file
+ penguins.pdf = PDF file
+ penguins.svg = SVG file

See `help(plt.savefig)` or the [online documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) for details.

# matplotlib

## Granular control

**matplotlib** allows us a lot of granular control of a data visualization.

We can build a visualization from the ground up


```python
Image('https://matplotlib.org/stable/_images/anatomy.png',width=400,height=400)
```




    
![png](03_01_data_visualization_files/03_01_data_visualization_131_0.png)
    



## Matplotlib

Both `seaborn` and `pandas` plotting methods actually are creating `matplotlib` plots, so knowing `matplotlib` is useful

+ to add features or annotations to a plot
+ to customize aspects of the plot
+ to easily compose sets of plots
+ to export and save plots
+ to do visualizations that are not "baked in" to `seaborn` or `pandas`

We've seen some of the elements of `matplotlib` syntax already, but we'll take a deeper dive now.

## Matplotlib

+ `seaborn` and `pandas` makes things easier to do quickly
    - Nicer, more expressive code for creating common visualizations (better API)
    - based on `pandas.DataFrame`
    - Less things to learn and remember
    - Nicer for **data visualization**
+ `matplotlib` is getting into the trenches, in some ways
    - powerful visualization tool in its own right
    - based on `numpy.array`
    - can create graphs of functions and other kinds of constructs
    - more involved syntax


## Matplotlib

We'll see the *object-oriented API* of matplotlib

> There is another way to create functions in matplotlib, that mimicks Matlab
> That API is considered outdated in favor of the OO one.



## Matplotlib

Let's start with creating a figure "canvas"


```python
fig, ax = plt.subplots() # default is 1 row and 1 col, so a single plot
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_136_0.png)
    


In the code, `fig` refers to the figure and `ax` refers to the axis or axes (if more than one subplot is created)

## Matplotlib

+ **Figure** refers to the topmost layer of a plot, which can contain axes, titles, labels, subplots
+ **Axes** define a subplot
    - We can write our own x-axis limits, y-axis limits, their labels, the type of graph. 
    - It controls every detail inside the subplot
    
Typically we will control aspects of our data visualization at the **axis** level. 

## Matplotlib

Now lets add some data to this plot


```python
fig, ax = plt.subplots()
ax.scatter(penguins['body_mass_g'], penguins['flipper_length_mm'])
ax.set_xlabel('Body mass (g)')
ax.set_ylabel('Flipper length (mm)')
ax.set_title('Palmer penguins');
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_140_0.png)
    


## Matplotlib

We can easily do subplots in this paradigm


```python
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20,4))
ax[0].scatter(penguins['body_mass_g'], penguins['flipper_length_mm'])
ax[1].scatter(penguins['bill_length_mm'],penguins['flipper_length_mm'])
ax[2].scatter(penguins['body_mass_g'], penguins['bill_depth_mm']);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_142_0.png)
    


Note that there is no labeling or annotation here. This needs to be done explicitly.

## Matplotlib

You can also create a 2-d grid of subplots quite easily


```python
cts = penguins['species'].value_counts()
fig,ax = plt.subplots(nrows=2, ncols=2, figsize = (10,4))
ax[0,0].scatter(penguins['body_mass_g'], penguins['flipper_length_mm'])
ax[0,1].scatter(penguins['bill_length_mm'],penguins['flipper_length_mm'])
ax[1,0].hist(penguins['body_mass_g'], color='orange');
ax[1,1].bar(cts.index, cts, color = ['red','blue','green']);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_145_0.png)
    


Of course you have to label and clean up the figure

## Matplotlib

The part that gets complicated with `matplotlib` are overlays. 

- You will have to layer each overlay on to the canvas using separate commands or loops
- This is where `seaborn`'s API makes things much simpler

## Matplotlib


```python
fig, ax = plt.subplots()
cols = ["red", "blue", "green"]
for i, u in enumerate(penguins["species"].unique()):
    d = penguins[penguins["species"] == u]
    ax.scatter(d["bill_length_mm"], d["body_mass_g"], c=cols[i], label=u)
ax.legend(title="Species", loc="best", labelcolor="black")
plt.show();
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_149_0.png)
    



```python
sns.relplot(
    data=penguins,
    x='bill_length_mm', y='body_mass_g',
    hue='species');
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_150_0.png)
    


## Matplotlib


```python
fig, axs = plt.subplots(nrows=1, ncols=3, 
                        sharey=True,
                        figsize=[15, 5])
cols = ["red", "blue", "green"]
for i, u in enumerate(penguins["species"].unique()):
    d = penguins[penguins["species"] == u]
    axs[i].scatter(d["bill_length_mm"], d["body_mass_g"], c=cols[i], label=u)
    axs[i].set_title(u)
    axs[i].set_xlabel("Bill length(mm)")
    if i == 0:
        axs[i].set_ylabel("Body mass (g)")
fig.legend();
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_152_0.png)
    



```python
g = sns.relplot(
    data=penguins, x="bill_length_mm", 
    y="body_mass_g", col="species", hue="species",
)
g.set_xlabels("Bill length (mm)")
g.set_ylabels("Body mass (g)");
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_153_0.png)
    


## Matplotlib

You can mix-and-match different `matplotlib` and `seaborn` axis-level graphics using the axis commands. 


```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=[15,5])
axs[0].bar(cts.index, cts)
axs[0].set_xlabel('Species')
sns.boxplot(ax = axs[1], data=penguins, 
              x = 'species', y = 'bill_length_mm', hue='species',);
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_155_0.png)
    


## Matplotlib and seaborn compatibility

![:scale 50%](https://seaborn.pydata.org/_images/function_overview_8_0.png)

- The functions at the top (relplot, displot, catplot) are *figure-level* functions and cannot be used with axes
- The functions below them are *axis-level* functions and can be used with axes

## Matplotlib and seaborn compatibility


```python
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=[15,4])
sns.countplot(ax=ax[0], data=penguins, x = 'species')
sns.histplot(ax=ax[1], data=penguins, x = 'body_mass_g');
ax[1].set_xlabel('Body mass(g)');
fig.suptitle('Penguins');
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_160_0.png)
    


## Matplotlib and pandas compatibility


```python
fig, ax=plt.subplots(nrows=1, ncols=2, figsize=[15,4])
penguins['species'].value_counts().plot(kind='bar', ax=ax[0]);
penguins['body_mass_g'].plot(kind='hist', ax = ax[1]);
fig.suptitle('Penguins');
```


    
![png](03_01_data_visualization_files/03_01_data_visualization_162_0.png)
    


# Further reading

## Further reading

+ [An overview of matplotlib plots](https://matplotlib.org/stable/tutorials/introductory/sample_plots.html)
+ [The lifecycle of a matplotlib plot](https://matplotlib.org/stable/tutorials/introductory/lifecycle.html)
+ [The matplotlib usage guide](https://matplotlib.org/stable/tutorials/introductory/usage.html)
