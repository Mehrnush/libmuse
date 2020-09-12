import plotly.express as px
import pandas as pd

df = pd.read_csv('to_plot/white_light/matthias_schmitt_white_light_experiment/Matthias_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "beta_relative"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
#df_mean = df_eeg_raw["EEG1"].mean()
#print(df_mean)
df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000000
df_sorted['timestamp'] /= 60
#fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
df_melted = df_sorted.melt(id_vars='timestamp', value_vars=['EEG1', 'EEG2', 'EEG3', 'EEG4'])
fig = px.line(df_melted, x='timestamp', y='value', color='variable')
fig.show()

df_eeg_raw = df.loc[df['data_type'] == "alpha_relative"]
df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000000
#fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
df_melted = df_sorted.melt(id_vars='timestamp', value_vars=['EEG1', 'EEG2', 'EEG3', 'EEG4'])
fig = px.line(df_melted, x='timestamp', y='value', color='variable')
fig.show()

df_eeg_raw = df.loc[df['data_type'] == "theta_relative"]
df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000000
#fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
df_melted = df_sorted.melt(id_vars='timestamp', value_vars=['EEG1', 'EEG2', 'EEG3', 'EEG4'])
fig = px.line(df_melted, x='timestamp', y='value', color='variable')
fig.show()

df_eeg_raw = df.loc[df['data_type'] == "quality"]
df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000000
#fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
df_melted = df_sorted.melt(id_vars='timestamp', value_vars=['EEG1', 'EEG2', 'EEG3', 'EEG4'])
fig = px.line(df_melted, x='timestamp', y='value', color='variable')
fig.show()

# df_eeg_raw = df.loc[df['data_type'] == "beta_relative"]
# df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
# df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
# df_sorted['timestamp'] /= 1000000
# #fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
# df_melted = df_sorted.melt(id_vars='timestamp', value_vars=['EEG1', 'EEG2', 'EEG3', 'EEG4'])
# fig = px.line(df_melted, x='timestamp', y='value', color='variable')
# fig.show()
# df = pd.read_csv('muse_data.txt')
# df_eeg_raw = df.loc[df['data_type'] == "eeg_raw"]
# df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
# df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
# df_sorted['timestamp'] /= 1000000
# fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
# fig.show()

# df = pd.read_csv('muse_data.txt')
# df_eeg_raw = df.loc[df['data_type'] == "eeg_raw"]
# df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
# df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
# df_sorted['timestamp'] /= 1000000
# fig = px.line(df_sorted, x= 'timestamp',y ='EEG3')
# fig.show()




# df_eeg_raw = df.loc[df['data_type'] == "alpha_absolute"]
# df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
# fig = px.line(df_sorted, x= 'timestamp',y ='EEG2')
# fig.show()


# df = pd.read_csv('muse_data.txt')
# df_eeg_raw = df.loc[df['data_type'] == "theta_relative"]
# df_sorted = df_eeg_raw.sort_values(by=["timestamp"])
# fig = px.line(df_sorted, x= 'timestamp',y ='EEG4')
# fig.show()


