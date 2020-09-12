import plotly.express as px
import pandas as pd
import math
import statistics


df = pd.read_csv('blue_light/Tobias_blue/tobias_engagementAverage_per_10minutes.txt',
                 decimal=".", delimiter=",", float_precision='high')
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig_ea = px.scatter(df, x='timestamp', y='value')

df = pd.read_csv('white_light/tobias_white/tobias_engagementAverage_per_10minutes.txt',
                 decimal=".", delimiter=",", float_precision='high')

fig_sat = px.scatter(df, x='timestamp', y='value')



fig_sat.update_traces(marker=dict(color="white"))
fig_sat.add_traces(fig_ea.data)
fig_sat.update_traces(marker=dict(size=40,line=dict(width=2,
                                        color='DarkSlateGrey')))
fig_sat.update_layout(
 xaxis=dict(
    gridcolor='gray',
    tickmode='linear',
      dtick=10.0
    )
)
fig_sat.show()