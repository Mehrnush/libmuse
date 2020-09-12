import plotly.express as px
import pandas as pd

df = pd.read_csv('to_plot/blue_light/matthias_Schmitt_Blue/matthias_schmitt_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('matthias_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/daniel_tabellion_blue/daniel_tabellion_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('daniel_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/kora_blue/kora_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('kora_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/marc_blue/marc_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('marc_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/moritz_blue/moritz_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('moritz_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/neuman_blue/neuman_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('Neuman_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/solveig_andres_blue/solveig_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('solveig_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/Tobias_blue/tobias_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('tobias_white_light', df_mean)

df = pd.read_csv('to_plot/blue_light/xenia_blue/xenia_blue_quality_report.txt')
#calcualte the mean
df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
#df_mean = df['timestamp'].resample('10Min', how='mean')
df_mean = df_eeg_raw["value"].mean()
print('xenia_white_light', df_mean)

