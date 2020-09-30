import plotly.graph_objs as go
import pandas as pd
import os
from plotly.subplots import make_subplots

this_file = os.path.dirname(__file__)
base_folder_plots = this_file
base_folder_white = os.path.join(this_file, '../data/white_light')
base_folder_blue = os.path.join(this_file, '../data/blue_light')
questionnaire_file_name = 'after_and_before_questionnaire.txt'
plot_questionnaire_blue_file_name = "questionnaire_before_and_after_blue_light_session.png"
plot_questionnaire_white_file_name = "questionnaire_before_and_after_white_light_session.png"
plot_question_file_name = "question_{}.png"


def generate_plot_questionnaire(question):
    blue_questionnaire_file_name = os.path.join(base_folder_blue, questionnaire_file_name)
    blue_data_frame = pd.read_csv(blue_questionnaire_file_name, decimal=".", delimiter=",", float_precision='high')

    white_questionnaire_file_name = os.path.join(base_folder_white, questionnaire_file_name)
    white_data_frame = pd.read_csv(white_questionnaire_file_name, decimal=".", delimiter=",", float_precision='high')

    score = [1, 2, 3, 4, 5]
    count_blue = []
    count_white = []
    for s in score:
        count_blue.append((blue_data_frame[blue_data_frame[question] == s])[question].count())
        count_white.append((white_data_frame[white_data_frame[question] == s])[question].count())
    fig = go.Figure()

    bar_white = go.Bar(x=score,
                       y=count_white,
                       name='white light session',
                       marker_color='white',
                       marker_line_color='black',
                       marker_line_width=0.5)

    bar_blue = go.Bar(x=score,
                      y=count_blue,
                      name='blue light session',
                      marker_color='blue',
                      marker_line_color='black',
                      marker_line_width=0.5)
    fig.add_trace(bar_blue)
    fig.add_trace(bar_white)
    fig.update_layout(barmode='group',
                      xaxis_title_text='Score',
                      yaxis_title_text='Number of Participants')
    return fig


def subplot_questions():
    fig_phy_b = generate_plot_questionnaire('physically_exhausted_before')
    fig_phy_a = generate_plot_questionnaire('physically_exhausted_after')
    fig_men_b = generate_plot_questionnaire('mentally_exhausted_before')
    fig_men_a = generate_plot_questionnaire('mentally_exhausted_after')

    fig = make_subplots(rows=2,
                        cols=2,
                        horizontal_spacing=0.2,
                        vertical_spacing=0.2,
                        x_title="Score",
                        y_title="Number of Participants",
                        subplot_titles=('Physcial Exhaustion before the Session', 'Physcial Exhaustion after the Session',
                                        'Mental Exhaustion before the Session', 'Mental Exhaustion after the Session'))

    for d in fig_phy_b.data:
        fig.add_trace(d, row=1, col=1)

    for d in fig_phy_a.data:
        d.update(showlegend=False)
        fig.add_trace(d, row=1, col=2)

    for d in fig_men_b.data:
        d.update(showlegend=False)
        fig.add_trace(d, row=2, col=1)

    for d in fig_men_a.data:
        d.update(showlegend=False)
        fig.add_trace(d, row=2, col=2)
    return fig


if __name__ == "__main__":
    question = 'mentally_exhausted_before'
    plot = generate_plot_questionnaire(question)
    plot_file_name = os.path.join(base_folder_plots, plot_question_file_name.format(question))
    plot.write_image(file=plot_file_name, format='png', engine="kaleido")
    plot.show()

    plot = subplot_questions()
    plot_file_name = os.path.join(base_folder_plots, plot_question_file_name.format('physical_and_mental_exhaustion'))
    plot.write_image(file=plot_file_name, format='png', engine="kaleido")
    plot.show()
