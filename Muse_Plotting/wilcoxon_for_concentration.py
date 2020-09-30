import os
from mean_blue import get_concentration_mean_session
from scipy import stats

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']

blue_concentration_avg_session = [get_concentration_mean_session(p, 'blue_light') for p in participants]
white_concentration_avg_session = [get_concentration_mean_session(p, 'white_light') for p in participants]


print(stats.ttest_rel(white_concentration_avg_session, blue_concentration_avg_session, ))
print(stats.shapiro(blue_concentration_avg_session))
print(stats.shapiro(white_concentration_avg_session))
print(stats.wilcoxon(blue_concentration_avg_session, white_concentration_avg_session, alternative='greater'))