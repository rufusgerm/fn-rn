import pandas as pd
from plotly.subplots import make_subplots
from plotly import figure_factory as ff
import plotly.graph_objects as go

fnum_df = pd.read_csv('./data/fnum_df.csv')
rnum_df = pd.read_csv('./data/rnum_df.csv')


# START OF CORRELATION MATRIX CONSTRUCTION
fnum_corrs = fnum_df[fnum_df.columns[0:-1]].corr()  # data[data.columns[1:]]
rnum_corrs = rnum_df[rnum_df.columns[0:-1]].corr()

fnum_corr_matrix = ff.create_annotated_heatmap(
    z=fnum_corrs.values,
    x=list(fnum_corrs.columns),
    y=list(fnum_corrs.index),
    annotation_text=fnum_corrs.round(2).values,
    showscale=True, colorscale='Viridis')

fnum_corr_matrix['layout']['yaxis']['autorange'] = "reversed"

rnum_corr_matrix = ff.create_annotated_heatmap(
    z=rnum_corrs.values,
    x=list(rnum_corrs.columns),
    y=list(rnum_corrs.index),
    annotation_text=rnum_corrs.round(2).values,
    showscale=True, colorscale='Viridis')

rnum_corr_matrix['layout']['yaxis']['autorange'] = "reversed"
# END OF CORRELATION MATRIX CONSTRUCTION


# START OF SCATTERPLOT CONSTRUCTION
fnum_subset = fnum_df[8000:10000]
rnum_subset = rnum_df[8000:10000]

overlayed_scatter = make_subplots(rows=1, cols=1)

overlayed_scatter.add_trace(
    go.Scatter(
        x=fnum_subset['title_unique'],
        y=fnum_subset['title_len'],
        mode='markers',
        marker=dict(
            color='tomato',
            size=5.5
        ),
        name='Fake'
    ),
    row=1, col=1
)

overlayed_scatter.add_trace(
    go.Scatter(
        x=rnum_subset['title_unique'],
        y=rnum_subset['title_len'],
        mode='markers',
        marker=dict(
            color='MediumPurple',
            size=5.5
        ),
        name='Real'
    ),
    row=1, col=1
)

overlayed_scatter.update_layout(
    height=480, width=630, title={
        'text': 'Unique Title Words vs. Average Sentence Length',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title={'text': "Quantity of Unique Words in the Title",
                 'standoff': 50
                 },
    yaxis_title="Average Length of Sentences in Articles",
    legend_orientation="h",

)
# END OF SCATTERPLOT CONSTRUCTION
