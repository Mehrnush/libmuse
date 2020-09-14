import plotly.graph_objs as go
import pandas as pd
import os

this_file = os.path.dirname(__file__)
base_folder_plots = this_file
base_folder_white = os.path.join(this_file, '../data/white_light')
base_folder_blue = os.path.join(this_file, '../data/blue_light')
interval_concentration_file_name = 'interval_concentration_questionary.txt'
plot_interval_concentration_file_name = "interval_concentration_questionary.png"

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']


def generate_plot_histogram_concentration(participant):
    participant_white_folder = os.path.join(base_folder_white, participant)
    white_interval_concentration_file_name = os.path.join(participant_white_folder,
                                                          interval_concentration_file_name)
    white_data_frame = pd.read_csv(white_interval_concentration_file_name, decimal=".", delimiter=",",
                                   float_precision='high')

    participant_blue_folder = os.path.join(base_folder_blue, participant)
    blue_interval_concentration_file_name = os.path.join(participant_blue_folder,
                                                         interval_concentration_file_name)
    blue_data_frame = pd.read_csv(blue_interval_concentration_file_name, decimal=".", delimiter=",",
                                  float_precision='high')
    fig = go.Figure()
    bar_white = go.Bar(x=white_data_frame['timestamp'],
                       y=white_data_frame['value'],
                       name='while light session',
                       marker_color='white',
                       marker_line_color='black',
                       marker_line_width=0.5)
    bar_blue = go.Bar(x=blue_data_frame['timestamp'],
                      y=blue_data_frame['value'],
                      name='blue light session',
                      marker_color='blue',
                      marker_line_color='black',
                      marker_line_width=0.5)
    fig.add_trace(bar_blue)
    fig.add_trace(bar_white)
    fig.update_layout(barmode='group',
                      xaxis_title_text='Time (minutes)',
                      yaxis_title_text='Concentration Level')
    return fig


if __name__ == "__main__":
    for p in participants:
        plot = generate_plot_histogram_concentration(p)
        plot_file_name = os.path.join(base_folder_plots, p, plot_interval_concentration_file_name)
        plot.write_image(file=plot_file_name, format='png', engine="kaleido")
        plot.show()
