# Analytic results displayed visually

## Visual display of analytic data 

Often times analytic results are better displayed visually to provide a digestible summary of results.

We'll go through some examples to show how this can be done

## Setup

In this section we will use two very common analytic packages in Python, viz., `statsmodels` and `scikit-learn` to develop some examples from 
which visualizations will be created. We will not go through how to develop models for data science using these packages here. BIOF309 provides an introduction to Python and these packages



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import altair as alt

import statsmodels.api as sm
import statsmodels.formula.api as smf
import sklearn as sk

from IPython.display import IFrame, display_html
def show_fig(fig, filename, width="100%", height=500):
    plotly.offline.plot(fig, filename=filename, auto_open=False, auto_play=False)
    display_html(IFrame(filename, height=height, width=width))

def show_fig2(filename, width="100%", height=500):
    display_html(IFrame(filename, width=width, height=height))
```

## Simple linear regression

We'll start with an linear regression (OLS) using the mpg dataset. We first load the data into Python


```python
tips = sns.load_dataset('tips')
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## Simple linear regression

We'll fit a simple linear model using the _formula interface_ available in **statsmodels**


```python
model = smf.ols(formula= 'tip ~ total_bill', data=tips)
results = model.fit()
print(results.summary2())
```

                     Results: Ordinary least squares
    =================================================================
    Model:              OLS              Adj. R-squared:     0.454   
    Dependent Variable: tip              AIC:                705.0762
    Date:               2021-04-26 15:43 BIC:                712.0705
    No. Observations:   244              Log-Likelihood:     -350.54 
    Df Model:           1                F-statistic:        203.4   
    Df Residuals:       242              Prob (F-statistic): 6.69e-34
    R-squared:          0.457            Scale:              1.0446  
    -------------------------------------------------------------------
                 Coef.    Std.Err.      t      P>|t|    [0.025   0.975]
    -------------------------------------------------------------------
    Intercept    0.9203     0.1597    5.7612   0.0000   0.6056   1.2349
    total_bill   0.1050     0.0074   14.2604   0.0000   0.0905   0.1195
    -----------------------------------------------------------------
    Omnibus:              20.185       Durbin-Watson:          2.151 
    Prob(Omnibus):        0.000        Jarque-Bera (JB):       37.750
    Skew:                 0.443        Prob(JB):               0.000 
    Kurtosis:             4.711        Condition No.:          53    
    =================================================================
    


## Simple linear regression

We can extract model information from the model into a _DataFrame_



```python
t1 = results.summary().tables[1]
```


```python
bl = t1.as_html()
d = pd.read_html(bl, header=0, index_col=0)[0]
```


```python
d.reset_index().rename(columns={'index':'variables'})
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
      <th>variables</th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>[0.025</th>
      <th>0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Intercept</td>
      <td>0.9203</td>
      <td>0.160</td>
      <td>5.761</td>
      <td>0.0</td>
      <td>0.606</td>
      <td>1.235</td>
    </tr>
    <tr>
      <th>1</th>
      <td>total_bill</td>
      <td>0.1050</td>
      <td>0.007</td>
      <td>14.260</td>
      <td>0.0</td>
      <td>0.091</td>
      <td>0.120</td>
    </tr>
  </tbody>
</table>
</div>



## Multiple linear regression

We'll expand the regression model to include multipe predictors, where some are categorical and some are continuous. 

We'll use a data set of housing prices in Windsor, Canada in 1987


```python
housing = sm.datasets.get_rdataset('HousePrices','AER').data # Housing prices in Windsor, Canada in summer, 1987
housing.head()
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
      <th>price</th>
      <th>lotsize</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>stories</th>
      <th>driveway</th>
      <th>recreation</th>
      <th>fullbase</th>
      <th>gasheat</th>
      <th>aircon</th>
      <th>garage</th>
      <th>prefer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42000.0</td>
      <td>5850</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
      <td>1</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38500.0</td>
      <td>4000</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>2</th>
      <td>49500.0</td>
      <td>3060</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60500.0</td>
      <td>6650</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>yes</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>61000.0</td>
      <td>6360</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>0</td>
      <td>no</td>
    </tr>
  </tbody>
</table>
</div>



## Multiple linear regression


```python
housing['lotsize1'] = housing.lotsize/100 # Coefficient will now be change in price per 100 sq.ft. change in lot size
model = smf.ols('price ~ lotsize1 + bedrooms + bathrooms + stories + driveway + recreation + fullbase + gasheat + aircon + garage + prefer', data = housing).fit()
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  price   R-squared:                       0.673
    Model:                            OLS   Adj. R-squared:                  0.666
    Method:                 Least Squares   F-statistic:                     99.97
    Date:                Tue, 27 Apr 2021   Prob (F-statistic):          6.18e-122
    Time:                        13:18:07   Log-Likelihood:                -6034.1
    No. Observations:                 546   AIC:                         1.209e+04
    Df Residuals:                     534   BIC:                         1.214e+04
    Df Model:                          11                                         
    Covariance Type:            nonrobust                                         
    =====================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
    -------------------------------------------------------------------------------------
    Intercept         -4038.3504   3409.471     -1.184      0.237   -1.07e+04    2659.271
    driveway[T.yes]    6687.7789   2045.246      3.270      0.001    2670.065    1.07e+04
    recreation[T.yes]  4511.2838   1899.958      2.374      0.018     778.976    8243.592
    fullbase[T.yes]    5452.3855   1588.024      3.433      0.001    2332.845    8571.926
    gasheat[T.yes]     1.283e+04   3217.597      3.988      0.000    6510.706    1.92e+04
    aircon[T.yes]      1.263e+04   1555.021      8.124      0.000    9578.182    1.57e+04
    prefer[T.yes]      9369.5132   1669.091      5.614      0.000    6090.724    1.26e+04
    lotsize1            354.6303     35.030     10.124      0.000     285.817     423.444
    bedrooms           1832.0035   1047.000      1.750      0.081    -224.741    3888.748
    bathrooms          1.434e+04   1489.921      9.622      0.000    1.14e+04    1.73e+04
    stories            6556.9457    925.290      7.086      0.000    4739.291    8374.600
    garage             4244.8290    840.544      5.050      0.000    2593.650    5896.008
    ==============================================================================
    Omnibus:                       93.454   Durbin-Watson:                   1.604
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              247.620
    Skew:                           0.853   Prob(JB):                     1.70e-54
    Kurtosis:                       5.824   Cond. No.                         308.
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


## Multiple linear regression

We can look at the distribution of the outcome (_price_) to see if it's close to the Gaussian distribution


```python
sns.displot(data=housing, x = 'price');
```


    
![svg](week6_analytic_results_files/week6_analytic_results_15_0.svg)
    


## Multiple linear regression

We will extract some results of the model into a _DataFrame_, which will help us visualize the model fit.


```python
D = pd.DataFrame({
    'fitted': model.fittedvalues,
    'actual' : housing['price'],
    'resid': model.resid
})
fig, ax=plt.subplots(figsize=(4,3))
sns.regplot(data=D, x = 'actual',y='fitted', lowess=True, ax=ax, line_kws={'color':'red'});
sm.graphics.abline_plot(0,1, ax=ax, color='green');
```


    
![svg](week6_analytic_results_files/week6_analytic_results_17_0.svg)
    


We see that the predicted values don't match the actual values well (red line), especially for higher prices

## Multiple linear regression

We can also look at a residual plot, i.e., the relationship between residuals and fitted values. We expect, for a well-fit model, there to be no relationship between the two


```python
fig,ax = plt.subplots(figsize=(4,3))
sns.regplot(data=D, x = 'fitted', y = 'resid', lowess=True, ax=ax, line_kws={'color':'red'}, scatter_kws={'alpha': 0.6});
sm.graphics.abline_plot(0,0, ax=ax, color='red', linestyle='--');
```


    
![svg](week6_analytic_results_files/week6_analytic_results_19_0.svg)
    


It looks like there is a bit of curvature (red solid line) compared to what we would have expected (red dashed line)

## Multiple linear regression

We can extract the parameter estimates and display them in a figure for better understanding


```python
tmp = model.summary().tables[1].as_html()
coefs = pd.read_html(tmp, index_col=0, header=0)[0].reset_index().rename(columns={'index':'variables'}).query('variables != "Intercept"')
coefs

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
      <th>variables</th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>[0.025</th>
      <th>0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>driveway[T.yes]</td>
      <td>6687.7789</td>
      <td>2045.246</td>
      <td>3.270</td>
      <td>0.001</td>
      <td>2670.065</td>
      <td>10700.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>recreation[T.yes]</td>
      <td>4511.2838</td>
      <td>1899.958</td>
      <td>2.374</td>
      <td>0.018</td>
      <td>778.976</td>
      <td>8243.592</td>
    </tr>
    <tr>
      <th>3</th>
      <td>fullbase[T.yes]</td>
      <td>5452.3855</td>
      <td>1588.024</td>
      <td>3.433</td>
      <td>0.001</td>
      <td>2332.845</td>
      <td>8571.926</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gasheat[T.yes]</td>
      <td>12830.0000</td>
      <td>3217.597</td>
      <td>3.988</td>
      <td>0.000</td>
      <td>6510.706</td>
      <td>19200.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>aircon[T.yes]</td>
      <td>12630.0000</td>
      <td>1555.021</td>
      <td>8.124</td>
      <td>0.000</td>
      <td>9578.182</td>
      <td>15700.000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>prefer[T.yes]</td>
      <td>9369.5132</td>
      <td>1669.091</td>
      <td>5.614</td>
      <td>0.000</td>
      <td>6090.724</td>
      <td>12600.000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>lotsize1</td>
      <td>354.6303</td>
      <td>35.030</td>
      <td>10.124</td>
      <td>0.000</td>
      <td>285.817</td>
      <td>423.444</td>
    </tr>
    <tr>
      <th>8</th>
      <td>bedrooms</td>
      <td>1832.0035</td>
      <td>1047.000</td>
      <td>1.750</td>
      <td>0.081</td>
      <td>-224.741</td>
      <td>3888.748</td>
    </tr>
    <tr>
      <th>9</th>
      <td>bathrooms</td>
      <td>14340.0000</td>
      <td>1489.921</td>
      <td>9.622</td>
      <td>0.000</td>
      <td>11400.000</td>
      <td>17300.000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>stories</td>
      <td>6556.9457</td>
      <td>925.290</td>
      <td>7.086</td>
      <td>0.000</td>
      <td>4739.291</td>
      <td>8374.600</td>
    </tr>
    <tr>
      <th>11</th>
      <td>garage</td>
      <td>4244.8290</td>
      <td>840.544</td>
      <td>5.050</td>
      <td>0.000</td>
      <td>2593.650</td>
      <td>5896.008</td>
    </tr>
  </tbody>
</table>
</div>



## Multiple linear regression

For each predictor we're plotting the point estimate and confidence interval, with color determining statistical significance at 5% significance level (red)


```python
coefs['indic'] = np.where(coefs['P>|t|'] <= 0.05, 'red','blue') # Find which predictors are "significant"
fig, ax = plt.subplots()
sns.scatterplot(data=coefs, x = 'coef', y = 'variables', palette = ['red','blue'], hue = 'indic',ax=ax, legend=None);
ax.hlines(y = coefs.variables, xmin = coefs['[0.025'], xmax = coefs['0.975]'], colors=coefs.indic);
ax.set_ylabel('predictors'); ax.set_xlabel('Change in price for unit change in predictor')
ax.axvline(0, linestyle=':', color = 'green');
```


    
![svg](week6_analytic_results_files/week6_analytic_results_23_0.svg)
    


## Multiple linear regression

We can also look at how well the residuals follow a theoretical Gaussian distribution using a Q-Q plot. For this, we will use functions from the **scipy** package


```python
import statsmodels
from sklearn import preprocessing
statsmodels.graphics.gofplots.qqplot(preprocessing.scale(D['resid']), line = '45');
```

    /Users/abhijit/opt/anaconda3/envs/biof440/lib/python3.8/site-packages/statsmodels/graphics/gofplots.py:993: UserWarning: marker is redundantly defined by the 'marker' keyword argument and the fmt string "bo" (-> marker='o'). The keyword argument will take precedence.
      ax.plot(x, y, fmt, **plot_style)



    
![svg](week6_analytic_results_files/week6_analytic_results_25_1.svg)
    


We see that there is quite a bit of deviation from the Gaussian distribution on the right (high) side of the distribution, but it's pretty good otherwise

## Variable importance plots

Variable importance plots are often used in machine learning to see the degree to which a predictor is truly predictive. It does this by comparing model performance of the model to one where the variable is replaced by a random permutation of that variable's data. 

We will use a random forest model on the housing data to demonstrate this


```python
y = housing.pop('price').values
X = pd.get_dummies(housing) # This creates numeric dummy variables for each level of each categorical variable
```


```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
import shap
```


```python
X_train,X_test,  y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12 )
rf = RandomForestRegressor(n_estimators=500)
rf.fit(X_train, y_train);
```




    RandomForestRegressor(n_estimators=500)



## Variable importance plots

We can now plot the variable importances extracted from the model object as a bar plot


```python
imps = pd.DataFrame({'variables': X.columns, 'importance': rf.feature_importances_})
sns.barplot(data=imps, x = 'importance', y = 'variables', );
```


    
![svg](week6_analytic_results_files/week6_analytic_results_32_0.svg)
    


## Variable importance plots

It's better if we sort the variables in increasing order for visualization


```python
sorted_indx = rf.feature_importances_.argsort()
sns.barplot(data = imps.iloc[sorted_indx,:], x = 'importance', y = 'variables');
```


    
![svg](week6_analytic_results_files/week6_analytic_results_34_0.svg)
    


## Shapley values for explainable ML

Shapley values are a method for understanding how outcome depends on each predictor in a machine learning model. It is based on game theoretic considerations and allows us to see how different values of a predictor impacts the outcome. 


```python
ex = shap.TreeExplainer(rf, X_train)
shap_values = ex(X_train)
```

    100%|===================| 407/409 [00:36<00:00]       


```python
shap.plots.bar(shap_values);
```


    
![svg](week6_analytic_results_files/week6_analytic_results_37_0.svg)
    


We see that, much like variable importance plots, the Shapley values indicate that lotsize and number of bathrooms have the most predictive power for house price.

## Shapley values

We can also look at the Shapley values in a heatmap, where each row is a predictor, each column is an observation, and we see how different predictors _together_ contribute to changes in house price.


```python
shap.plots.heatmap(shap_values)
```


    
![svg](week6_analytic_results_files/week6_analytic_results_39_0.svg)
    


## Shapley values

Finally we can look at how the Shapley values for a predictor change with the value of the predictor, giving indications of potentially non-linear relationships between predictor and outcome.


```python
shap.plots.scatter(shap_values[:,'lotsize'])
```


    
![svg](week6_analytic_results_files/week6_analytic_results_41_0.svg)
    


## Prediction accuracy

For the random forest model, we see that the predictive accuracy is much higher than the linear regression model.


```python
fig,ax = plt.subplots()
sns.regplot(rf.predict(X_test), y_test, ax=ax);
sm.graphics.abline_plot(0,1, ax=ax, color='red', linestyle='--')
fig.savefig('img/rf_predict.png')
show_fig2('img/rf_predict.png')
```

    Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.




<iframe
    width="100%"
    height="500"
    src="img/rf_predict.png"
    frameborder="0"
    allowfullscreen
></iframe>




    
![svg](week6_analytic_results_files/week6_analytic_results_43_2.svg)
    


# Using altair

## Prediction plot

We'll first look at the prediction accuracy of the linear regression model. We remind ourselves what we had captured from the model fit


```python
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
      <th>fitted</th>
      <th>actual</th>
      <th>resid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>66037.975672</td>
      <td>42000.0</td>
      <td>-24037.975672</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41391.151457</td>
      <td>38500.0</td>
      <td>-2891.151457</td>
    </tr>
    <tr>
      <th>2</th>
      <td>39889.630131</td>
      <td>49500.0</td>
      <td>9610.369869</td>
    </tr>
    <tr>
      <th>3</th>
      <td>63689.087331</td>
      <td>60500.0</td>
      <td>-3189.087331</td>
    </tr>
    <tr>
      <th>4</th>
      <td>49760.426466</td>
      <td>61000.0</td>
      <td>11239.573534</td>
    </tr>
  </tbody>
</table>
</div>



## Prediction plot: altair

We can plot the actual vs the fitted values, with a lowess line showing the observed pattern in the data (red) to compare to the 45 degree line (green) that we would like.


```python
chart = alt.Chart(D).mark_point().encode(
    x = 'actual',
    y = 'fitted',
    tooltip = ['actual','fitted'],
)
abline = alt.Chart(pd.DataFrame({'x': [0,160000], 'y':[0,160000]})).mark_line(color='green').encode(x='x', y='y')
(chart + abline + chart.transform_loess('actual','fitted').mark_line(color='red')).save('img/predict_alt1.html')
show_fig2('img/predict_alt1.html')
#chart + chart.transform_loess('actual', 'predicted').mark_line(color='red') + chart.transform_regression('actual','predicted').mark_line(color='green')
```



<iframe
    width="100%"
    height="500"
    src="img/predict_alt1.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Prediction plot: plotly


```python
fig = px.scatter(data_frame=D, x = 'actual', y='fitted', trendline='lowess', trendline_color_override='red', template='simple_white')
fig.add_shape(type='line',
    x0=0, y0=0, x1=160000, y1=160000, line = dict(color='green',width=3))
show_fig(fig, 'img/prediction_plotly.html')
```



<iframe
    width="100%"
    height="500"
    src="img/prediction_plotly.html"
    frameborder="0"
    allowfullscreen
></iframe>



## Coefficient plot: altair


```python
coefs = coefs.rename(columns={'[0.025' : 'lcb', '0.975]':'ucb'})
lines = alt.Chart(coefs).mark_errorbar().encode(y = 'variables', x = 'lcb', x2 = 'ucb',
    color = alt.condition(
        alt.datum['P>|t|'] <0.05,
        alt.value('red'),
        alt.value('blue'),
    ))
ref = pd.DataFrame([{'threshold':0}])
points = alt.Chart(coefs).mark_point().encode(x = 'coef', y = 'variables')
(points + lines + alt.Chart(ref).mark_rule(color = 'green', strokeDash=[5,5]).encode(x = 'threshold')).save('img/coef_alt.html')
show_fig2('img/coef_alt.html')
```



<iframe
    width="100%"
    height="500"
    src="img/coef_alt.html"
    frameborder="0"
    allowfullscreen
></iframe>




```python
coefs.head()
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
      <th>variables</th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>lcb</th>
      <th>ucb</th>
      <th>indic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>driveway[T.yes]</td>
      <td>6687.7789</td>
      <td>2045.246</td>
      <td>3.270</td>
      <td>0.001</td>
      <td>2670.065</td>
      <td>10700.000</td>
      <td>red</td>
    </tr>
    <tr>
      <th>2</th>
      <td>recreation[T.yes]</td>
      <td>4511.2838</td>
      <td>1899.958</td>
      <td>2.374</td>
      <td>0.018</td>
      <td>778.976</td>
      <td>8243.592</td>
      <td>red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>fullbase[T.yes]</td>
      <td>5452.3855</td>
      <td>1588.024</td>
      <td>3.433</td>
      <td>0.001</td>
      <td>2332.845</td>
      <td>8571.926</td>
      <td>red</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gasheat[T.yes]</td>
      <td>12830.0000</td>
      <td>3217.597</td>
      <td>3.988</td>
      <td>0.000</td>
      <td>6510.706</td>
      <td>19200.000</td>
      <td>red</td>
    </tr>
    <tr>
      <th>5</th>
      <td>aircon[T.yes]</td>
      <td>12630.0000</td>
      <td>1555.021</td>
      <td>8.124</td>
      <td>0.000</td>
      <td>9578.182</td>
      <td>15700.000</td>
      <td>red</td>
    </tr>
  </tbody>
</table>
</div>



## Coefficient plot: plotly


```python
coefs['e'] = 1.96*coefs['std err']
fig = px.scatter(coefs, x = 'coef', y = 'variables', error_x = 'e', error_x_minus='e', template='simple_white',
    color = np.where(coefs['P>|t|'] < 0.05, 'signif','not signif'),
    color_discrete_map = {'signif': 'red', 'not signif': 'blue'},)
fig.update_layout(showlegend=False)
fig.add_vline(x = 0.0, line=dict(color='green', width=3, dash='dash'))

show_fig(fig, 'img/coef_plotly.html')
```



<iframe
    width="100%"
    height="500"
    src="img/coef_plotly.html"
    frameborder="0"
    allowfullscreen
></iframe>


