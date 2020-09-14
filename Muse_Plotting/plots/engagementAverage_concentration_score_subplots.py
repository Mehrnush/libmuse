from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
from plots.plot_test_score import generate_plot_test_score
from plots.plot_histogram_concentration import generate_plot_histogram_concentration
from plots.plot_engagement_average_interval_white_and_blue import generate_plot_engagement_average_interval_blue_and_white


this_file = os.path.dirname(__file__)
base_folder_plots = this_file
eng_avg_concentration_score_file_name = "eng_avg_concentration_score_subplots.png"

participants = ['daniel', 'kora', 'marc', 'matthias', 'moritz', 'neuman', 'solveig', 'tobias', 'xenia']

interval = 10
for p in participants:
    fig = make_subplots(rows=2,
                        cols=2,
                        specs=[[{"colspan": 2}, None],
                               [{}, {}], ],
                        horizontal_spacing=0.2,
                        vertical_spacing=0.2)

    fig_eng_avg_interval = generate_plot_engagement_average_interval_blue_and_white(participant=p, interval=interval)
    for d in fig_eng_avg_interval.data:
        fig.add_trace(d, row=1, col=1)


    fig_hist_concentration = generate_plot_histogram_concentration(p)
    for d in fig_hist_concentration.data:
        d.update(showlegend=False)
        fig.add_trace(d, row=2, col=1)

    fig_test_score = generate_plot_test_score(p)
    for d in fig_test_score.data:
        d.update(showlegend=False)
        fig.add_trace(d, row=2, col=2)

    fig.update_layout(
        xaxis=dict(
            title="Time (minutes)",
            gridcolor='black',
            tickmode='linear',
            dtick=interval
        ),
        yaxis=dict(
            title="Engagement Level",
        ),
        xaxis2=dict(
            title="Time (minutes)",
        ),
        yaxis2=dict(
            title="Concentration Level",
        ),
        yaxis3=dict(
            title='Score',
        ),)

    plot_file_name = os.path.join(base_folder_plots, p, eng_avg_concentration_score_file_name)
    fig.write_image(file=plot_file_name, format='png', engine="kaleido")
    fig.show()