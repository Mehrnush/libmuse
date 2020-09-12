import plotly.express as px
import pandas as pd
import numpy as np


#Daniel
df = pd.read_csv('white_light/daniel_white/daniel_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
#df['index'] = df.reset_index().index
#df = df.set_index('data_type')

#df.index = range(571685)
#print(df)
#df = df.T.plot()
#df = df.drop(['betaAverage', 'alphaAverage', 'thetaAverage', 'fatigureRatio1', 'fatigueRatio2'])
print(df)

elevel = df.loc[df['data_type'] == ['sat', 'hue']]
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted['value'] /= 10

#df_sorted = df.drop('alphaAverage', axis=0)
#df_sorted = df.drop('thetaAverage', axis=0)
#df_sorted = df.drop('fatigueRatio1', axis=0)
#df_sorted = df.drop('fatigueRatio2', axis=0)

#df_melted = df_sorted.melt(id_vars='timestamp', value_vars=['hue,sat,engagementLevel'])
#fig = px.line(df_melted, x='timestamp', y='value', color='variable')
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value', color='variable')
fig.show()

#df2 = df.T
#print(df2)


