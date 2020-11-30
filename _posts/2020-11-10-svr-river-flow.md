---
layout: post
title: Predicting River Flow with Support Vector Machine Regression
subtitle: A case study
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/thumb.png
share-img: /assets/img/path.jpg
tags: [machine learning, support vector machines, regression, sklearn, python]
---


•	Intro
    o   climate change is enhancing uncertainty and posing new risks to every sector of business
    o	Climate tech is booming. As the effects of climate change become more evident, decision-makers are realizing that virtually every sector will be affected in some way. In response to this, machine learning and data science si becoming a crucial tool for addressing many of the problems.
    o	One example is in agriculture. Name some statistics about how agriculture is extremely dependent upon good forecasts and are sensitive to change.
    o	This post will serve as a brief tutorial on how to use machine learning to predict river flow. Specifically, we’ll be using an SVR model. Next well introduce support vector regression. Then we’ll describe the steps needed for building an SVR model, and how SKLEARN can be utilized to streamline this workflow.
•	Support Vector Regression Basics
    o	Optimization problem
    o	Kernel trick
        	Hyperparameters of kernels
    o	Advantages
•	Necessary steps when developing an SVR model
    -   Imports
    First, we need to import the following tools
```python
import scipy
import numpy as np
import pandas as pd
import sklearn
import math
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn import metrics
from datetime import datetime
svg_renderer = pio.renderers['svg']
```

    That's a lot of imports! What do they do?

    EDA
    Next, let's load the data

```python
with open('river_dataset.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')
```

Describe the dataset

```python
    data.keys()
    data['flow'].shape
```

So we can see that this is a dictionary, where each value is a numpy array.
Let's turn it into a pandas dataframe.

```python
what = pd.DataFrame(data={'flow':data['flow']}, index=data['flow_dates']).rename_axis('date')
temp = pd.DataFrame(data['obs_tas'], index=data['obs_dates'], columns=['t_loc1','t_loc2','t_loc3','t_loc4','t_loc5','t_loc6','t_loc7','t_loc8','t_loc9']).rename_axis('date')
precip = pd.DataFrame(data['obs_pr'], index=data['obs_dates'], columns=['p_loc1','p_loc2','p_loc3','p_loc4','p_loc5','p_loc6','p_loc7','p_loc8','p_loc9']).rename_axis('date')
```

Next, we can melt the dataframes for even easier handling.

```python
# melt dataframes of precip. (p) and temp. (t) data
p_melt = pd.melt(precip.reset_index(), id_vars='date', var_name='location', value_name='precip').set_index('date')
t_melt = pd.melt(temp.reset_index(), id_vars='date', var_name='location', value_name='temp').set_index('date')

t_melt
```

Our melted dataframes are now a bit easier to work with. Let's get a view of our datasets before we calculate the annual mean and daily means. I'm using
plotly in this tutorial. One tip for making graphs that are reproducible is to use a helper function. Then we can call this function whenever we want a plot. I'll define that function here:

```python
# define helper function for plotting
def make_plot(plot_type, df=None, x_vals=None, y_vals=None, plot_title=None, x_title=None, y_title=None, color_vals=None, error_vals=None):

    tick_loc='inside'
    tick_width=2
    line_color='black'
    line_width=2

    xticks=7
    x_tick_angle=45
    x_tick_font_size=14
    x_tick_font_color='black'

    x_title_size=18
    x_title_color="black"

    yticks=7
    y_tick_angle = 90
    y_tick_font_size=14
    y_tick_font_color = "black"

    y_title_size=18
    y_title_color="black"
    
    plot_dict = {
        'bar':px.bar(df, x=x_vals, y=y_vals, color=color_vals, error_y=error_vals),
        'go':go.Figure(),
        'box':px.box(df, y=y_vals, color=color_vals),
        'histogram':px.histogram(df, x=x_vals)
    }
    
    fig = plot_dict[plot_type]
    

    fig.update_yaxes(title=y_title, titlefont=dict(size=y_title_size, color=y_title_color),
                     ticks=tick_loc, nticks=yticks, tickwidth=tick_width,
                     tickfont=dict(size=y_tick_font_size, color=y_tick_font_color),
                     showline=True, linecolor=line_color, linewidth=line_width)

    fig.update_xaxes(title=x_title, titlefont=dict(size=x_title_size, color=x_title_color),
                     ticks=tick_loc, nticks=xticks, tickwidth=tick_width,
                     showline=True, linecolor=line_color, linewidth=line_width,
                     tickangle=x_tick_angle, tickfont=dict(size=x_tick_font_size, color=x_tick_font_color))

    fig.update_layout(title=plot_title, margin=dict(t=60), height=620, width=620, showlegend=True, 
                    legend=dict(
                        title='', 
                        bordercolor="Black",
                        borderwidth=2,
                        yanchor="top",
                        y=1,
                        xanchor="left", font=dict(color='black'),
                        x=1))
    return fig
```
        	Plot the variables to look for outliers
        	Plot seasonal averages to gain insight to the problem
    o	Feature selection/engineering
Now let's do some EDA! I like to take a few minutes before diving in to first set some goals for my EDA. While searching for answers to these questions, you are bound to find more interesting things and new ideas, but it
helps to have a direction to start with. Here's a few things we can think about:

These three questions should always be asked first:
1) What does the distribution of my data look like?
2) Are there any massive outliers?
3) How much missing data is there?

Then think about the problem and the goal. Here's some other questions:
1) Do all the locations have similar temp/rain trends?
2) What is the seasonal trend for each location?
3) Is there a time of year when flooding is at its greatest?
4) What is the annual mean like?

```python
fig1 = make_plot(plot_type='histogram', df=t_melt, x_vals='temp', color_vals='location', facet_col_vals='location', facet_col_wrap_num=3, x_title='Temperature (\u00B0C)')
fig1.update_layout(width=700, height=600, showlegend=False)
fig1.for_each_annotation(lambda a: a.update(font=dict(color='black'), text=f'<b>Location {a.text[-1]}</b>'))
```
This plot shows the histograms of temperature for each location across the entire dataset. With histograms, we're looking to get a general idea of the dataset, including the spread, skew, and presence of outliers. We also want to see if it's unimodal, bimodal, or multimodal. These kinds of things are important because they may violate the assumptions of your model.

These distributions look fairly reasonable. No presence of major outliers. They appear to be multimodal, which makes sense given seasonality. We can get a bit more information if we plot the box plots.

Let's look at the annual mean temperature of each location. We see that location 1's mean temperature is right around 0, while the other locations are a bit warmer. We can consider possible reasons for this discrepency, such as elevation changes or bias in our dataset if we have a faulty instrument.

```python
fig2 = make_plot('bar', annual_mean_temp.reset_index(), 'location', 'temp', 'Annual Mean Temperature (\u00B0C)',
                'Location', 'Temperature (\u00B0C)', color_vals='location', error_vals='std')

fig2.update_xaxes(nticks=9)
fig2.update_yaxes(nticks=20)
fig2.show(renderer="svg", scale=1)

```
Now we can shift to precipitation.

```python
fig2 = make_plot(plot_type='histogram', df=p_melt, x_vals='precip', color_vals='location', facet_col_vals='location', facet_col_wrap_num=3, x_title='Precipitation (mm)')
fig2.update_layout(width=700, height=600, showlegend=False)
fig2.update_yaxes(type='log')
fig2.for_each_annotation(lambda a: a.update(font=dict(color='black'), text=f'<b>Location {a.text[-1]}</b>'))
```

Note the use of a lambda function. 

Here we have the distribution of the daily precip for each location. We have a strong right skew, which makes sense (i.e., most days there is no rain and only a few days have extremely high precipitation events). 

```python
annual_mean_precip_total = p_melt.groupby(by=['location', p_melt.index.year]).sum()
true_annual_mean_precip = annual_mean_precip_total.reset_index().groupby('location').mean()
true_annual_mean_precip['std'] = annual_mean_precip_total.reset_index().groupby('location').std()['precip']

fig4 = make_plot('bar', true_annual_mean_precip.reset_index(), 'location', 'precip', 'Yearly Mean Precipitation (mm)',
                'Location', 'Precipitation (mm)', color_vals='location', error_vals='std')

fig4.update_xaxes(nticks=9)
fig4.update_yaxes(nticks=20)
```
Here we see the mean annual (total) precipitation for each location. Each location is fairly similar, although location 8 has the most rainfall. We'll dive a bit deeper into rainfall and precipitation trends, but first let's check the distribution of our target variable, river flow.

```python
fig3 = make_plot(plot_type='histogram', df=river, x_vals='flow', x_title='River Flow')
fig3.update_layout(width=600, height=500, showlegend=False)
fig3.update_yaxes(nticks=10)
```


Finally, we have the target variable. There's lots of disagreement on whether skewed data should be transformed for a more normal distriution of target variables. It's important to realzie that for linear regression, its NOT a requirement that the target data be normal. Rather, only the residuals should be normal.

Now let's look at the data a bit closer. Here beyond just looking at the structure of our data, we want to start to tease out more useful information. For instance, what if we plot the data as a function of month?

```python
river['month'] = river.index.month

fig4 = make_plot(plot_type='box', df=river, y_vals='flow', color_vals='month', x_title='Month', y_title='Daily River Flow')
fig4.show()
```

Here we see that river flow is at a minimum during winter months, at its highest during spring, and elevated during winter/fall. This plot is also useful as it again shows the lack of outliers.

Let's do the same for precipitation:

```python
p_melt['month'] = p_melt.index.month

fig5 = px.box(p_melt, y='precip', color='month')
fig5.update_yaxes(title='Daily Precipitation (mm)')
fig5.show()
```
Next we see seasonality for precipitation. Interestingly, despite river flow being at a maximum in May, precipitation is not at its highest during this time. PLotting the temeprature data will give us a clue as to what's going on.

```python
t_melt['month'] = t_melt.index.month

fig6 = px.box(t_melt, y='temp', color='month')
fig6.show()
```
So it seems that right around April/May is when the daily mean temperature rises above freezing. This means the spring flooding isn't due to necesarily to rain events, but rather is driven by melting of the snowpack.

We can see this all together if we plot the daily mean of temperature/precip and river flow in one plot.

```python
fig5 = make_subplots(rows=2, cols=1, specs=[[{'secondary_y':True}], [{'secondary_y':False}]])

fig5.add_trace(go.Scatter(name='Daily Average of Temperature', x=daily_mean_t.index, y=daily_mean_t['temp']))

fig5.add_trace(go.Scatter(x=daily_mean_t.index, y=daily_mean_t['std']+daily_mean_t['temp'],  
                          mode='lines', showlegend=False, line=dict(width=0)))

fig5.add_trace(go.Scatter(name='Lower Bound', x=daily_mean_t.index, y=daily_mean_t['temp']-daily_mean_t['std'],
                          line=dict(width=0), mode='lines', fill='tonexty', showlegend=False))

fig5.add_trace(go.Scatter(name='Daily Average of Precipitation',
                          x = daily_mean_p.index, y = daily_mean_p['precip']), secondary_y=True)

fig5.add_trace(go.Scatter(x=daily_mean_p.index, y=daily_mean_p['std']+daily_mean_p['precip'], 
                          mode='lines', showlegend=False, line=dict(width=0)),secondary_y=True)

fig5.add_trace(go.Scatter(name='Lower Bound', x=daily_mean_p.index, y=daily_mean_p['precip']-daily_mean_p['std'], 
                          line=dict(width=0), mode='lines', fill='tonexty', showlegend=False), secondary_y=True)


fig5.layout['xaxis'] = fig4.layout['xaxis'].update({'title':{'text':'Day of Year'}})
fig5.layout['yaxis'] = fig3.layout['yaxis'].update({'nticks':10})

fig5.layout['yaxis2'] = fig4.layout['yaxis'].update({'overlaying':'y', 'side':'right'})
fig5.update_layout(width=900, height=500,legend=dict(y = 0.95, x=0.01))

fig6 = go.Figure()

fig6.add_trace(go.Scatter( name='Daily Mean River Flow',
    x = daily_mean_river.index,
    y = daily_mean_river['flow']
))

fig6.add_trace(go.Scatter(
    x=daily_mean_river.index, # x, then x reversed
    y=daily_mean_river['std'] +daily_mean_river['flow'] , # upper, then lower reversed
    mode='lines',
    showlegend=False,
    line=dict(width=0)
    ))
fig6.add_trace(go.Scatter(
    name='Lower Bound',
    x=daily_mean_river.index, # x, then x reversed
    y=daily_mean_river['flow']-daily_mean_river['std'] , # upper, then lower reversed
    line=dict(width=0),
    mode='lines',
    fill='tonexty',
    showlegend=False
))
fig6.layout['xaxis'] = fig4.layout['xaxis'].update({'title':{'text':'Day of Year'}})
fig6.layout['yaxis'] = fig3.layout['yaxis'].update({'nticks':10, 'title':{'text':'River Flow (m<sup>3</sup>/s)'}})
fig6.update_layout(width=900, height=500,legend=dict(y = 0.95, x=0.01))

fig5.show(renderer="svg", scale=1)
fig6.show(renderer="svg", scale=1)

#fig5.write_image('daily_mean_temp_precip.png', scale=2)
#fig6.write_image('daily_mean_river_flow.png', scale=2)
```
Much of the increased river flow occurs during spring (around May). Based on the absence of a large increase in precipitation around that time, along with the long period of sub-zero temperatures in winter, we can assume this increase in river flow is due to yearly snowpack melt.

The river decreases again into summer, but remains elevated relatvie to winter time when precipitation is falling as snow.

## Pre-processing and Feature Engineering



While doing this EDA, we should also be thinking about potential features that we can engineer based on what we learn. 
Once we've done this, we can really begin to brainstorm for features. 

      	Test for correlations

One way of doing this is to test for correlations. For instance, is there a correlation between rainfall and river flow after X amount of days? We can test for this simply using pandas shift feature.
Note that this kind of correlation analysis is only a first guess, and doesn't include feature interactions. For instance, maybe the amount of rainfall is not correlated well, but when non-linearly interacting with
temperatyre in some way, we get a stronger correlation with riverflow. By the way, this is why non-linear SVRs are so powerful. They test for this inplicitly.

```python
# Look for correlation with time lagged precipitation
river_rain = pd.merge(precip, river, left_index=True, right_index=True)

for x in range(1,11):
    river_rain[f'flow-{x}'] = river_rain['flow'].shift(-x)
    
river_rain.corr().loc[:'p_loc9', 'flow':]
```

Are there certain months where the correlations are stronger? For instance, if we look at a total rainfal and river flow, we may mask the impact of one specific month's rainfall-river flow interaction.


Here's an idea of some features:
Le'ts create them:
     	Create rolling windows
  
   
    o	Splitting data
        	Final evaluation set
    o	Feature transformation
        	Choice of scaler
    o	Splitting data again for cross validation with a rolling time window
        	Why a rolling time window is needed
    o	Training and hyperparameter tuning
        	CVgridsearch
    o	Doing all of this with Pipeline 
•	Training/testing the model and comparing it with other methods


