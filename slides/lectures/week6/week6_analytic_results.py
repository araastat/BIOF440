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
# # Analytic results displayed visually
#
# ## Visual display of analytic data 
#
# Often times analytic results are better displayed visually to provide a digestible summary of results.
#
# We'll go through some examples to show how this can be done
#
# ## Setup
#
# In this section we will use two very common analytic packages in Python, viz., `statsmodels` and `scikit-learn` to develop some examples from 
# which visualizations will be created. We will not go through how to develop models for data science using these packages here. BIOF309 provides an introduction to Python and these packages
#

# %%
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


# %% [markdown]
# ## Simple linear regression
#
# We'll start with an linear regression (OLS) using the mpg dataset. We first load the data into Python

# %%
tips = sns.load_dataset('tips')
tips.head()

# %% [markdown]
# ## Simple linear regression
#
# We'll fit a simple linear model using the _formula interface_ available in **statsmodels**

# %%
model = smf.ols(formula= 'tip ~ total_bill', data=tips)
results = model.fit()
print(results.summary2())

# %% [markdown]
# ## Simple linear regression
#
# We can extract model information from the model into a _DataFrame_
#

# %%
t1 = results.summary().tables[1]

# %%
bl = t1.as_html()
d = pd.read_html(bl, header=0, index_col=0)[0]

# %%
d.reset_index().rename(columns={'index':'variables'})

# %% [markdown]
# ## Multiple linear regression
#
# We'll expand the regression model to include multipe predictors, where some are categorical and some are continuous. 
#
# We'll use a data set of housing prices in Windsor, Canada in 1987

# %%
housing = sm.datasets.get_rdataset('HousePrices','AER').data # Housing prices in Windsor, Canada in summer, 1987
housing.head()

# %% [markdown]
# ## Multiple linear regression

# %%
housing['lotsize1'] = housing.lotsize/100 # Coefficient will now be change in price per 100 sq.ft. change in lot size
model = smf.ols('price ~ lotsize1 + bedrooms + bathrooms + stories + driveway + recreation + fullbase + gasheat + aircon + garage + prefer', data = housing).fit()
print(model.summary())

# %% [markdown]
# ## Multiple linear regression
#
# We can look at the distribution of the outcome (_price_) to see if it's close to the Gaussian distribution

# %%
sns.displot(data=housing, x = 'price');

# %% [markdown]
# ## Multiple linear regression
#
# We will extract some results of the model into a _DataFrame_, which will help us visualize the model fit.

# %%
D = pd.DataFrame({
    'fitted': model.fittedvalues,
    'actual' : housing['price'],
    'resid': model.resid
})
fig, ax=plt.subplots(figsize=(4,3))
sns.regplot(data=D, x = 'actual',y='fitted', lowess=True, ax=ax, line_kws={'color':'red'});
sm.graphics.abline_plot(0,1, ax=ax, color='green');

# %% [markdown]
# We see that the predicted values don't match the actual values well (red line), especially for higher prices
#
# ## Multiple linear regression
#
# We can also look at a residual plot, i.e., the relationship between residuals and fitted values. We expect, for a well-fit model, there to be no relationship between the two

# %%
fig,ax = plt.subplots(figsize=(4,3))
sns.regplot(data=D, x = 'fitted', y = 'resid', lowess=True, ax=ax, line_kws={'color':'red'}, scatter_kws={'alpha': 0.6});
sm.graphics.abline_plot(0,0, ax=ax, color='red', linestyle='--');

# %% [markdown]
# It looks like there is a bit of curvature (red solid line) compared to what we would have expected (red dashed line)
#
# ## Multiple linear regression
#
# We can extract the parameter estimates and display them in a figure for better understanding

# %%
tmp = model.summary().tables[1].as_html()
coefs = pd.read_html(tmp, index_col=0, header=0)[0].reset_index().rename(columns={'index':'variables'}).query('variables != "Intercept"')
coefs


# %% [markdown]
# ## Multiple linear regression
#
# For each predictor we're plotting the point estimate and confidence interval, with color determining statistical significance at 5% significance level (red)

# %%
coefs['indic'] = np.where(coefs['P>|t|'] <= 0.05, 'red','blue') # Find which predictors are "significant"
fig, ax = plt.subplots()
sns.scatterplot(data=coefs, x = 'coef', y = 'variables', palette = ['red','blue'], hue = 'indic',ax=ax, legend=None);
ax.hlines(y = coefs.variables, xmin = coefs['[0.025'], xmax = coefs['0.975]'], colors=coefs.indic);
ax.set_ylabel('predictors'); ax.set_xlabel('Change in price for unit change in predictor')
ax.axvline(0, linestyle=':', color = 'green');

# %% [markdown]
# ## Multiple linear regression
#
# We can also look at how well the residuals follow a theoretical Gaussian distribution using a Q-Q plot. For this, we will use functions from the **scipy** package

# %%
import statsmodels
from sklearn import preprocessing
statsmodels.graphics.gofplots.qqplot(preprocessing.scale(D['resid']), line = '45');

# %% [markdown]
# We see that there is quite a bit of deviation from the Gaussian distribution on the right (high) side of the distribution, but it's pretty good otherwise

# %% [markdown]
# ## Variable importance plots
#
# Variable importance plots are often used in machine learning to see the degree to which a predictor is truly predictive. It does this by comparing model performance of the model to one where the variable is replaced by a random permutation of that variable's data. 
#
# We will use a random forest model on the housing data to demonstrate this

# %%
y = housing.pop('price').values
X = pd.get_dummies(housing) # This creates numeric dummy variables for each level of each categorical variable

# %%
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
import shap

# %%
X_train,X_test,  y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12 )
rf = RandomForestRegressor(n_estimators=500)
rf.fit(X_train, y_train);

# %% [markdown]
# ## Variable importance plots
#
# We can now plot the variable importances extracted from the model object as a bar plot

# %%
imps = pd.DataFrame({'variables': X.columns, 'importance': rf.feature_importances_})
sns.barplot(data=imps, x = 'importance', y = 'variables', );

# %% [markdown]
# ## Variable importance plots
#
# It's better if we sort the variables in increasing order for visualization

# %%
sorted_indx = rf.feature_importances_.argsort()
sns.barplot(data = imps.iloc[sorted_indx,:], x = 'importance', y = 'variables');

# %% [markdown]
# ## Shapley values for explainable ML
#
# Shapley values are a method for understanding how outcome depends on each predictor in a machine learning model. It is based on game theoretic considerations and allows us to see how different values of a predictor impacts the outcome. 

# %%
ex = shap.TreeExplainer(rf, X_train)
shap_values = ex(X_train)

# %%
shap.plots.bar(shap_values);

# %% [markdown]
# We see that, much like variable importance plots, the Shapley values indicate that lotsize and number of bathrooms have the most predictive power for house price.
#
# ## Shapley values
#
# We can also look at the Shapley values in a heatmap, where each row is a predictor, each column is an observation, and we see how different predictors _together_ contribute to changes in house price.

# %%
shap.plots.heatmap(shap_values)

# %% [markdown]
# ## Shapley values
#
# Finally we can look at how the Shapley values for a predictor change with the value of the predictor, giving indications of potentially non-linear relationships between predictor and outcome.

# %%
shap.plots.scatter(shap_values[:,'lotsize'])

# %% [markdown]
# ## Prediction accuracy
#
# For the random forest model, we see that the predictive accuracy is much higher than the linear regression model.

# %%
fig,ax = plt.subplots()
sns.regplot(rf.predict(X_test), y_test, ax=ax);
sm.graphics.abline_plot(0,1, ax=ax, color='red', linestyle='--')
fig.savefig('img/rf_predict.png')
show_fig2('img/rf_predict.png')

# %% [markdown]
# # Using altair
#
# ## Prediction plot
#
# We'll first look at the prediction accuracy of the linear regression model. We remind ourselves what we had captured from the model fit

# %%
D.head()

# %% [markdown]
# ## Prediction plot: altair
#
# We can plot the actual vs the fitted values, with a lowess line showing the observed pattern in the data (red) to compare to the 45 degree line (green) that we would like.

# %%
chart = alt.Chart(D).mark_point().encode(
    x = 'actual',
    y = 'fitted',
    tooltip = ['actual','fitted'],
)
abline = alt.Chart(pd.DataFrame({'x': [0,160000], 'y':[0,160000]})).mark_line(color='green').encode(x='x', y='y')
(chart + abline + chart.transform_loess('actual','fitted').mark_line(color='red')).save('img/predict_alt1.html')
show_fig2('img/predict_alt1.html')
#chart + chart.transform_loess('actual', 'predicted').mark_line(color='red') + chart.transform_regression('actual','predicted').mark_line(color='green')

# %% [markdown]
# ## Prediction plot: plotly

# %%
fig = px.scatter(data_frame=D, x = 'actual', y='fitted', trendline='lowess', trendline_color_override='red', template='simple_white')
fig.add_shape(type='line',
    x0=0, y0=0, x1=160000, y1=160000, line = dict(color='green',width=3))
show_fig(fig, 'img/prediction_plotly.html')

# %% [markdown]
# ## Coefficient plot: altair

# %%
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

# %%
coefs.head()

# %% [markdown]
# ## Coefficient plot: plotly

# %%
coefs['e'] = 1.96*coefs['std err']
fig = px.scatter(coefs, x = 'coef', y = 'variables', error_x = 'e', error_x_minus='e', template='simple_white',
    color = np.where(coefs['P>|t|'] < 0.05, 'signif','not signif'),
    color_discrete_map = {'signif': 'red', 'not signif': 'blue'},)
fig.update_layout(showlegend=False)
fig.add_vline(x = 0.0, line=dict(color='green', width=3, dash='dash'))

show_fig(fig, 'img/coef_plotly.html')
