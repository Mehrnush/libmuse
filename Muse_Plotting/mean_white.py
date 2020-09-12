import plotly.express as px
import pandas as pd

df = pd.read_csv('to_plot/white_light/matthias_schmitt_white_light_experiment/Matthias_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('matthias_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/daniel_white/daniel_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('daniel_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/kora_white/kora_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('kora_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/marc_white/marc_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('marc_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/moritz_white/moritz_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('moritz_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/Neuman_Fakhar_white/Nuamn_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('Neuman_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/solveig_white/solveig_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('solveig_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/tobias_white/Tobias_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('tobias_white_light', df_mean)

df = pd.read_csv('to_plot/white_light/xenia_white/xenia_white_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('xenia_white_light', df_mean)

