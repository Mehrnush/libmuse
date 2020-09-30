from scipy.stats import pearsonr
from mean_blue import get_eng_avg_mean_session, get_concentration_mean_session
import os
import pandas as pd

this_file = os.path.dirname(__file__)
base_folder_plots = os.path.join('plots')
base_folder_blue = os.path.join(this_file, 'data/blue_light')
base_folder_white = os.path.join(this_file, 'data/white_light')
eng_avg_with_interval_file_name = 'engagement_average_10_minutes_interval.txt'
interval_concentration_file_name = 'interval_concentration_questionary.txt'

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']

blue_eng_avg_session = [get_eng_avg_mean_session(p, 'blue_light') for p in participants]
white_eng_avg_session = [get_eng_avg_mean_session(p, 'white_light') for p in participants]
blue_concentration_avg_session = [get_concentration_mean_session(p, 'blue_light') for p in participants]
white_concentration_avg_session = [get_concentration_mean_session(p, 'white_light') for p in participants]

blue_eng_avg_interval_10 = [[] for i in range(6)]
white_eng_avg_interval_10 = [[] for i in range(6)]
blue_concentration_10 = [[] for i in range(6)]
white_concentration_10 = [[] for i in range(6)]

for p in participants:
    df = pd.read_csv('data/{}/{}/{}'.format('blue_light', p, eng_avg_with_interval_file_name))
    for i in range(len(df['value'])):
        if i > 5:
            break
        blue_eng_avg_interval_10[i].append(df['value'][i])
    df = pd.read_csv('data/{}/{}/{}'.format('white_light', p, eng_avg_with_interval_file_name))
    for i in range(len(df['value'])):
        if i > 5:
            break
        white_eng_avg_interval_10[i].append(df['value'][i])

    df = pd.read_csv('data/{}/{}/{}'.format('blue_light', p, interval_concentration_file_name))
    for i in range(len(df['value'])):
        if df['value'][i] == 0:
            break
        blue_concentration_10[i].append(df['value'][i])
    df = pd.read_csv('data/{}/{}/{}'.format('white_light', p, interval_concentration_file_name))
    for i in range(len(df['value'])):
        if df['value'][i] == 0:
            break
        white_concentration_10[i].append(df['value'][i])



print("Whole Session")
print("Blue {}".format(pearsonr(blue_eng_avg_session, blue_concentration_avg_session)))
print("White {}".format(pearsonr(white_eng_avg_session, white_concentration_avg_session)))

print("Interval 1-10")
print("n=" + str(len(blue_eng_avg_interval_10[0])))
print("Blue {}".format(pearsonr(blue_eng_avg_interval_10[0], blue_concentration_10[0])))
print("White {}".format(pearsonr(white_eng_avg_interval_10[0], white_concentration_10[0])))
print("Interval 11-20")
print("n=" + str(len(blue_eng_avg_interval_10[1])))
print("Blue {}".format(pearsonr(blue_eng_avg_interval_10[1], blue_concentration_10[1])))
print("White {}".format(pearsonr(white_eng_avg_interval_10[1], white_concentration_10[1])))

print("Interval 21-30")
print("n=" + str(len(blue_eng_avg_interval_10[2])))
print("Blue {}".format(pearsonr(blue_eng_avg_interval_10[2], blue_concentration_10[2])))
print("White {}".format(pearsonr(white_eng_avg_interval_10[2], white_concentration_10[2])))


print("Interval 31-40")
print("n=" + str(len(blue_eng_avg_interval_10[3])))
print("Blue {}".format(pearsonr(blue_eng_avg_interval_10[3], blue_concentration_10[3])))
print("White {}".format(pearsonr(white_eng_avg_interval_10[3], white_concentration_10[3])))

print("Interval 41-50")
print("n=" + str(len(blue_eng_avg_interval_10[4])))
print("Blue {}".format(pearsonr(blue_eng_avg_interval_10[4], blue_concentration_10[4])))
print("White {}".format(pearsonr(white_eng_avg_interval_10[4], white_concentration_10[4])))

print("Interval 51-60")
print("n=" + str(len(blue_eng_avg_interval_10[5])))
print("Blue {}".format(pearsonr(blue_eng_avg_interval_10[5], blue_concentration_10[5])))
print("White {}".format(pearsonr(white_eng_avg_interval_10[5], white_concentration_10[5])))

