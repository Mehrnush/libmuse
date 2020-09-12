import plotly.express as px
import pandas as pd



df = pd.read_csv('to_plot/white_light/matthias_schmitt_white_light_experiment/Matthias_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementLevel']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()