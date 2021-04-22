```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import lifelines as lfl
import kaplanmeier as km
```


```

df = km.example_data()
time_event = df['time']
censoring = df['Died']
labx = df['group']

out = km.fit(time_event, censoring, labx) # Direct grouped lines
```


```

km.plot(out)
```


```

from lifelines import KaplanMeierFitter 
from lifelines.statistics import (logrank_test, 
                                  pairwise_logrank_test, 
                                  multivariate_logrank_test, 
                                  survival_difference_at_fixed_point_in_time_test)

kmf = KaplanMeierFitter()
kmf.fit(time_event, event_observed=censoring)

kmf.plot(at_risk_counts=True)
plt.title('Kaplan-Meier Curve');


```


```
ax = kmf.plot()
ax.set_xlabel('days')
ax.set_ylabel('Probability of survival')
ax.get_legend().remove()
ax.set_title('Kaplan-Meier estimates')
```


```

ax = lfl.plotting.plot_lifetimes(time_event, censoring,
    event_observed_color='red', event_censored_color='blue',
    sort_by_duration=True)
ax.set_xlabel('Time')
ax.vlines(1000, 0,200,linestyles='--');
```


```

ax = kmf.plot( at_risk_counts=True)
ax.set_label('days')
ax.set_ylabel('Probability of survival')
ax.get_legend().remove()
```


```
import matplotlib.ticker as mtick

T1 = df.query('group==1')['time']
T2 = df.query('group==2')['time']

C1 = df.query('group==1')['Died']
C2 = df.query('group==2')['Died']

fig, ax = plt.subplots()
kmf1 = KaplanMeierFitter()
kmf1.fit(T1, C1)
kmf2 = KaplanMeierFitter()
kmf2.fit(T2, C2)

kmf1.plot(ax = ax, label='Group 1', ci_show=False)
kmf2.plot(ax = ax, label = 'Group 2', ci_show=False)
fmt = "%0.0f%%"
ticks = mtick.PercentFormatter(xmax=1, symbol='%', decimals=None) # formats axis as percents
ax.yaxis.set_major_formatter(ticks)
ax.set_ylabel('Percent survived');
```


```

```
