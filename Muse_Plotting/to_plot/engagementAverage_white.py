import plotly.express as px
import pandas as pd

#Mathias
df = pd.read_csv('white_light/matthias_schmitt_white_light_experiment/Matthias_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()

#daniel
df = pd.read_csv('white_light/daniel_white/daniel_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()

#kora
df = pd.read_csv('white_light/kora_white/kora_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()

#marc
df = pd.read_csv('white_light/marc_white/marc_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()

#moritz
df = pd.read_csv('white_light/moritz_white/moritz_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()


#neuman
df = pd.read_csv('white_light/moritz_white/moritz_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()

#solveig
df = pd.read_csv('white_light/solveig_white/solveig_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()

#Tobias
df = pd.read_csv('white_light/tobias_white/Tobias_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()


#xenia
df = pd.read_csv('white_light/xenia_white/xenia_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()
#df_sorted['value'] /= 10
#df_melted = df_sorted.melt(id_vars=' timestamp', value_vars=['value'])
fig = px.line(df_sorted, x='timestamp', y='value')
fig.show()