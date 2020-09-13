import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import os

this_file = os.path.dirname(__file__)
base_folder_plots = this_file
base_folder_white = os.path.join(this_file, '../data/white_light')
base_folder_blue = os.path.join(this_file, '../data/blue_light')
eng_avg_with_interval_file_name = 'engagement_average_{}_minutes_interval.txt'
plot_eng_avg_interval_blue_white_file_name = "engagement_average_blue_white_{}_minutes_interval.png"

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']

def plot_engagement_average_interval_blue_and_white(interval=1):
    for p in participants:
        participant_white_folder = os.path.join(base_folder_white, p)
        eng_avg_white_interval_file_name = os.path.join(participant_white_folder,
                                                        eng_avg_with_interval_file_name.format(interval))
        white_data_frame = pd.read_csv(eng_avg_white_interval_file_name, decimal=".", delimiter=",",
                                       float_precision='high')

        participant_blue_folder = os.path.join(base_folder_blue, p)
        eng_avg_blue_interval_file_name = os.path.join(participant_blue_folder,
                                                       eng_avg_with_interval_file_name.format(interval))
        blue_data_frame = pd.read_csv(eng_avg_blue_interval_file_name, decimal=".", delimiter=",",
                                      float_precision='high')
        fig = go.Figure()

        engagement_average_white = go.Scatter(x=white_data_frame['timestamp'],
                                              y=white_data_frame['value'],
                                              mode="markers",
                                              line_color='white',
                                              name="white light session",
                                              marker=dict(size=10, line=dict(width=2, color='DarkSlateGrey')))
        engagement_average_blue = go.Scatter(x=blue_data_frame['timestamp'],
                                             y=blue_data_frame['value'],
                                             mode="markers",
                                             line_color="blue",
                                             name="blue light session",
                                             marker=dict(size=10, line=dict(width=2, color='DarkSlateGrey')))
        last_timestamp = white_data_frame['timestamp'].iloc[-1] if white_data_frame['timestamp'].iloc[-1] > blue_data_frame['timestamp'].iloc[-1] else blue_data_frame['timestamp'].iloc[-1]
        threshold = go.Scatter(x=[0, last_timestamp+10],
                               y=[0.549, 0.549],
                               mode="lines",
                               line_color="red",
                               name='engagement level threshold')

        fig.add_trace(threshold)
        fig.add_trace(engagement_average_blue)
        fig.add_trace(engagement_average_white)

        fig.update_layout(
         xaxis=dict(
            title="Time (minutes)",
            gridcolor='black',
            tickmode='linear',
              dtick=interval
            ),
         yaxis=dict(
            title="Engagement Level",
            )
        )
        plot_file_name = os.path.join(base_folder_plots, p, plot_eng_avg_interval_blue_white_file_name.format(interval))
        fig.write_image(file=plot_file_name, format='png', engine="kaleido", scale=5.0)
        fig.show()


if __name__ == "__main__":
    plot_engagement_average_interval_blue_and_white(1)
