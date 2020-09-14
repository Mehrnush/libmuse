import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objs as go
import os

this_file = os.path.dirname(__file__)
base_folder_plots = this_file
base_folder_white = os.path.join(this_file, '../data/white_light')
base_folder_blue = os.path.join(this_file, '../data/blue_light')
eng_avg_with_interval_file_name = 'engagement_average_{}_minutes_interval.txt'
saturation_file_name = 'saturation.txt'
plot_eng_avg_and_sat_file_name = "engagement_average_{}_minutes_interval_and_saturation.png"

participants = ['moritz', 'tobias']


def generate_plot_engagement_average_and_saturation(participant, interval=1):
    participant_blue_folder = os.path.join(base_folder_blue, participant)
    eng_avg_blue_interval_file_name = os.path.join(participant_blue_folder,
                                                   eng_avg_with_interval_file_name.format(interval))
    eng_avg_data_frame = pd.read_csv(eng_avg_blue_interval_file_name, decimal=".", delimiter=",",
                                     float_precision='high')

    saturation_blue_file_name = os.path.join(participant_blue_folder,saturation_file_name)
    sat_data_frame = pd.read_csv(saturation_blue_file_name, decimal=".", delimiter=",", float_precision='high')

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    engagement_average = go.Scatter(x=eng_avg_data_frame['timestamp'],
                                    y=eng_avg_data_frame['value'],
                                    mode="lines",
                                    line_color='blue',
                                    name="engagement level",
                                    marker=dict(size=10, line=dict(width=2, color='DarkSlateGrey')))
    saturation = go.Scatter(x=sat_data_frame['timestamp'],
                            y=sat_data_frame['value'],
                            mode="lines",
                            line_color="black",
                            name="blue light saturation",
                            marker=dict(size=10, line=dict(width=2, color='DarkSlateGrey')))

    #fig_sat = px.line(df, x='timestamp', y='value')
    #fig_sat.update_traces(yaxis="y2")

    #fig.add_traces(fig_ea.data + fig_sat.data)
    #fig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))

    last_timestamp = \
        eng_avg_data_frame['timestamp'].iloc[-1] \
        if eng_avg_data_frame['timestamp'].iloc[-1] > sat_data_frame['timestamp'].iloc[-1] \
        else sat_data_frame['timestamp'].iloc[-1]
    threshold = go.Scatter(x=[0, last_timestamp+10],
                           y=[0.549, 0.549],
                           mode="lines",
                           line_color="red",
                           name='engagement level threshold')

    fig.add_trace(threshold)
    fig.add_trace(engagement_average)
    fig.add_trace(saturation, secondary_y=True)

    fig.update_layout(
        xaxis=dict(
            title="Time (minutes)",
        ),
        yaxis=dict(
            title="Engagement Level",
        ),
        yaxis2=dict(
            title='Saturation'
        )
    )
    return fig


if __name__ == "__main__":
    interval = 1
    for p in participants:
        plot = generate_plot_engagement_average_and_saturation(participant=p, interval=interval)
        plot_file_name = os.path.join(base_folder_plots, p, plot_eng_avg_and_sat_file_name.format(interval))
        plot.write_image(file=plot_file_name, format='png', engine="kaleido")
        plot.show()
