import plotly.graph_objs as go
import pandas as pd
import os

this_file = os.path.dirname(__file__)
base_folder_plots = this_file
base_folder_white = os.path.join(this_file, '../data/white_light')
base_folder_blue = os.path.join(this_file, '../data/blue_light')
test_score_file_name = 'test_score.txt'
plot_test_score_file_name = "test_score.png"

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']

white_test_score_file_name = os.path.join(base_folder_white, test_score_file_name)
white_data_frame = pd.read_csv(white_test_score_file_name, decimal=".", delimiter=",",
                               float_precision='high')

blue_test_score_file_name = os.path.join(base_folder_blue, test_score_file_name)
blue_data_frame = pd.read_csv(blue_test_score_file_name, decimal=".", delimiter=",",
                              float_precision='high')

white_data_frame.loc[:, 'Total'] = white_data_frame.sum(axis=1)
blue_data_frame.loc[:, 'Total'] = blue_data_frame.sum(axis=1)


def generate_plot_test_score(participant):
    p_score_white = white_data_frame.loc[white_data_frame['name'] == participant]['Total']
    p_score_blue = blue_data_frame.loc[blue_data_frame['name'] == participant]['Total']
    fig = go.Figure()
    bar_white = go.Bar(x=['Reading Task'],
                       y=p_score_white,
                       name='while light session',
                       marker_color='white',
                       marker_line_color='black',
                       marker_line_width=0.5)
    bar_blue = go.Bar(x=['Reading Task'],
                      y=p_score_blue,
                      name='blue light session',
                      marker_color='blue',
                      marker_line_color='black',
                      marker_line_width=0.5)

    fig.add_trace(bar_blue)
    fig.add_trace(bar_white)
    fig.update_layout(barmode='group',
                      yaxis_title_text='Score')
    return fig


if __name__ == "__main__":
    for p in participants:
        plot = generate_plot_test_score(p)
        plot_file_name = os.path.join(base_folder_plots, p, plot_test_score_file_name)
        plot.write_image(file=plot_file_name, format='png', engine="kaleido")
        plot.show()
