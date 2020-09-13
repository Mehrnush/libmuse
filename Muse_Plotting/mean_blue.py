import plotly.express as px
import pandas as pd

df = pd.read_csv('data/blue_light/matthias/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('matthias_white_light', df_mean)

df = pd.read_csv('data/blue_light/daniel/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('daniel_white_light', df_mean)

df = pd.read_csv('data/blue_light/kora/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('kora_white_light', df_mean)

df = pd.read_csv('data/blue_light/marc/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('marc_white_light', df_mean)

df = pd.read_csv('data/blue_light/moritz/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('moritz_white_light', df_mean)

df = pd.read_csv('data/blue_light/neuman/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('Neuman_white_light', df_mean)

df = pd.read_csv('data/blue_light/solveig/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('solveig_white_light', df_mean)

df = pd.read_csv('data/blue_light/tobias/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('tobias_white_light', df_mean)

df = pd.read_csv('data/blue_light/xenia/quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('xenia_white_light', df_mean)

