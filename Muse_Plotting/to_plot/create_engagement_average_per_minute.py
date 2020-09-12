import pandas as pd
import math
import statistics


df = pd.read_csv('white_light/tobias_white/Tobias_white_quality_report.txt',
                 decimal=".", delimiter=",", float_precision='high')
elevel = df.loc[df['data_type'] == 'engagementAverage']
df_sorted = elevel.sort_values(by=["timestamp"])
df_sorted['timestamp'] -= df_sorted['timestamp'].iloc[0]
df_sorted['timestamp'] /= 1000
df_sorted['timestamp'] /= 60
df_sorted = df_sorted.dropna()



with open('white_light/tobias_white/tobias_engagementAverage_per_10minutes.txt', mode='w') as file:
    file.writelines('timestamp,value\n')
    time_previous = 0
    time = 0
    values = []
    print(len(df_sorted))
    for index, row in df_sorted.iterrows():
        print(row['timestamp'])
        time += row['timestamp'] - time_previous
        if time < 10.0:
            values.append(row['value'])
        else:
            time = math.floor(time_previous)
            if len(values) >0:
                mean = statistics.mean(values)
            else:
                mean = -1
            file.writelines('{},{}\n'.format(time, mean))
            time_previous = time
            time = 0
            values = []
        time_previous = row['timestamp']