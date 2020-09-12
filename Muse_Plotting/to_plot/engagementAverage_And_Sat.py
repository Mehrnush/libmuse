import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import math
import statistics


fig = make_subplots(specs=[[{"secondary_y": True}]])

df = pd.read_csv('blue_light/Tobias_blue/tobias_blue_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])


fig_ea = px.line(df_sorted, x='timestamp', y='value')

sat = df.loc[df['data_type'] == 'sat']
df_sorted = sat.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])

fig_sat = px.line(df_sorted, x='timestamp', y='value')
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

