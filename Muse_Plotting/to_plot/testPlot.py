import plotly.express as px
import pandas as pd
import numpy as np


#Daniel
df = pd.read_csv('white_light/daniel_white/daniel_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
df = df.set_index('data_type')
#df = df.drop(['betaAverage', 'alphaAverage', 'thetaAverage', 'fatigureRatio1', 'fatigueRatio2'])
print(df)
elevel = df.loc[['sat', 'hue']]
print(elevel)
#elevel = df.loc[(df['data_type'] == 'sat') | (df['data_type'] == 'hue')]
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted['value'] /= 10
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()


