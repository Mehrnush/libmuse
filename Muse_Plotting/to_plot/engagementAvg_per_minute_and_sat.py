import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import math
import statistics


fig = make_subplots(specs=[[{"secondary_y": True}]])

df = pd.read_csv('blue_light/Tobias_blue/tobias_engagementAverage_per_minute.txt',
                 decimal=".", delimiter=",", float_precision='high')
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig_ea = px.line(df, x='timestamp', y='value')

df = pd.read_csv('blue_light/Tobias_blue/tobias_sat_real.txt',
                 decimal=".", delimiter=",", float_precision='high')

fig_sat = px.line(df, x='timestamp', y='value')
fig_sat.update_traces(yaxis="y2")

fig.add_traces(fig_ea.data + fig_sat.data)
fig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))


fig.layout.xaxis.title = "Time (minutes)"
fig.layout.yaxis.title = "Engagement Level"
fig.layout.yaxis2.title = "Saturation"
#fig.update_layout(
 #   xaxis=dict(
        #gridcolor='gray',
 #       tickmode='linear',
  #      dtick=1.0
 #   )
#)
fig.show()