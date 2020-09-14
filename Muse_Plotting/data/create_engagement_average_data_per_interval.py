import pandas as pd
import math
import statistics
import os

this_file = os.path.dirname(__file__)
base_folder_white = os.path.join(this_file, 'white_light')
base_folder_blue = os.path.join(this_file, 'blue_light')
blue_session_data_file_name = 'quality_report.txt'
white_session_data_file_name = 'quality_report.txt'
eng_avg_with_interval_file_name = 'engagement_average_{}_minutes_interval.txt'

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']


def to_minutes(data_frame):
    data_frame['timestamp'] -= data_frame['timestamp'].iloc[0]
    data_frame['timestamp'] /= 1000
    data_frame['timestamp'] /= 60
    return data_frame

def preprocess_data(data_frame):
    data_frame = data_frame.sort_values(by=["timestamp"])
    data_frame = to_minutes(data_frame)
    data_frame = data_frame.dropna()
    return data_frame


def calculate_engagement_averages(data_frame, interval=1):
    data = []
    time_window = interval
    values = []
    for index, row in data_frame.iterrows():
        if row['timestamp'] < time_window:
            values.append(row['value'])
        else:
            if len(values) > 0:
                mean = statistics.mean(values)
            else:
                mean = -1
            data.append((time_window, mean))
            time_window += interval
            values = [row['value']]

    if len(values) > 0:
        mean = statistics.mean(values)
    else:
        mean = -1
    data.append((math.ceil(row['timestamp']), mean))
    return data


def create_engagement_average_data(interval=1):
    for p in participants:
        participant_white_folder = os.path.join(base_folder_white, p)
        data_file_white_session = os.path.join(participant_white_folder, white_session_data_file_name)
        white_data_frame = pd.read_csv(data_file_white_session, decimal=".", delimiter=",", float_precision='high')
        eng_avg_white = preprocess_data(white_data_frame.loc[white_data_frame['data_type'] == 'engagementAverage'])
        eng_avg_white_with_interval = calculate_engagement_averages(eng_avg_white, interval)
        eng_avg_white_interval_file_name = os.path.join(participant_white_folder,
                                                        eng_avg_with_interval_file_name.format(interval))
        with open(eng_avg_white_interval_file_name, mode='w') as file:
            file.writelines('timestamp,value\n')
            for data in eng_avg_white_with_interval:
                file.writelines('{},{}\n'.format(*data))

        participant_blue_folder = os.path.join(base_folder_blue, p)
        data_file_blue_session = os.path.join(participant_blue_folder, blue_session_data_file_name)
        blue_data_frame = pd.read_csv(data_file_blue_session, decimal=".", delimiter=",", float_precision='high')
        eng_avg_blue = preprocess_data(blue_data_frame.loc[blue_data_frame['data_type'] == 'engagementAverage'])
        eng_avg_blue_with_interval = calculate_engagement_averages(eng_avg_blue, interval)
        eng_avg_blue_interval_file_name = os.path.join(participant_blue_folder,
                                                       eng_avg_with_interval_file_name.format(interval))
        with open(eng_avg_blue_interval_file_name, mode='w') as file:
            file.writelines('timestamp,value\n')
            for data in eng_avg_blue_with_interval:
                file.writelines('{},{}\n'.format(*data))


if __name__ == "__main__":
    create_engagement_average_data(1)
    create_engagement_average_data(5)
    create_engagement_average_data(10)
