import plotly.express as px
import pandas as pd



def get_eng_avg_mean_session(participant, session):
    df = pd.read_csv('data/{}/{}/quality_report.txt'.format(session, participant))
    df_eeg_raw = df.loc[df['data_type'] == "engagementLevel"]
    return df_eeg_raw["value"].mean()


def get_concentration_mean_session(participant, session):
    df = pd.read_csv('data/{}/{}/interval_concentration_questionary.txt'.format(session, participant))
    return df["value"].mean()
