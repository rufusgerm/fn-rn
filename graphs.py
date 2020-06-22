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
# ###################################### #
# END OF CORRELATION MATRIX CONSTRUCTION
# ###################################### #


# ###################################### #
# START OF SCATTERPLOT CONSTRUCTION
# ###################################### #

# Gathering a subset of the data because the plots load too
# slow when we get too many data points
fnum_subset = fnum_df[8000:10000]
rnum_subset = rnum_df[8000:10000]

# ###################################### #
# START OF TITLE LEN VS TITLE UNIQUE PLOT
# ###################################### #
overlayed_scatter_unique = make_subplots(rows=1, cols=1)

overlayed_scatter_unique.add_trace(
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

overlayed_scatter_unique.add_trace(
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

overlayed_scatter_unique.update_layout(
    height=480,
    width=630,
    title={
        'text': 'Unique Title Words vs. Average Sentence Length',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
                'size': 23
        }
    },
    xaxis_title={'text': "Quantity of Unique Words in the Title",
                 'standoff': 50
                 },
    yaxis_title="Average Length of Sentences in Articles",
    legend_orientation="h",
)
# ###################################### #
# END OF TITLE LENGTH VS TITLE UNIQUE PLOT
# ###################################### #
# ###################################### #
# START OF AVERAGE LENGTH VS TITLE LEN PLOT
# ###################################### #
overlayed_scatter_len = make_subplots(rows=1, cols=1)

overlayed_scatter_len.add_trace(
    go.Scatter(
        x=fnum_subset['avg_sentence_len'],
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

overlayed_scatter_len.add_trace(
    go.Scatter(
        x=rnum_subset['avg_sentence_len'],
        y=rnum_subset['title_len'],
        mode='markers',
        marker=dict(
            color='blueviolet',
            size=5.5
        ),
        name='Real'
    ),
    row=1, col=1
)

overlayed_scatter_len.update_layout(
    height=480,
    width=630,
    title={
        'text': 'Average Sentence Length vs Title Length',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
                'size': 23
        }
    },
    xaxis={
        'title': {
            'text': "Quantity of Unique Words in the Title",
            'standoff': 50
        },
    },
    yaxis={
        'title': {
            'text': "Average Length of Sentences in Articles",
        },
    },
    legend_orientation="h",

)
# ###################################### #
# END OF SCATTERPLOT CONSTRUCTION
# ###################################### #

# Import the common words DFs
fn_common_df = pd.read_csv('./data/fn_common_df.csv')
rn_common_df = pd.read_csv('./data/rn_common_df.csv')

# Convert DFs to  lists
fn_common_list = fn_common_df.values.tolist()
rn_common_list = rn_common_df.values.tolist()

# Create two separate lists for the words and corresponding counts
x_fake, y_fake = [], []
for word, count in fn_common_list:
    x_fake.append(word)
    y_fake.append(count)

x_real, y_real = [], []
for word, count in rn_common_list:
    x_real.append(word)
    y_real.append(count)

fake_common_bar = {
    'data': [
        go.Bar(
            x=y_fake,
            y=x_fake,
            orientation='h',
            marker={'color': y_fake,
                    'colorscale': 'Rainbow'}
        )
    ],
    'layout': go.Layout(
        title={
            'text': '30 Most Common Words In Fake News',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 26
            }
        },
        xaxis={
            'title': {
                'text': "Quantity",
            }
        },
        yaxis={
            'title': {
                'text': "Word",
                'standoff': 30
            },
            'autorange': "reversed",
            'dtick': 1
        },
        bargap=0.33,
        autosize=True

    )
}

real_common_bar = {
    'data': [
        go.Bar(
            x=y_real,
            y=x_real,
            orientation='h',
            marker={'color': y_fake,
                    'colorscale': 'Rainbow'}
        )
    ],
    'layout': go.Layout(
        title={
            'text': '30 Most Common Words In Real News',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 26
            }
        },
        xaxis={
            'title': {
                'text': "Quantity",
            }
        },
        yaxis={
            'title': {
                'text': "Word",
                'standoff': 30
            },
            'autorange': "reversed",
            'dtick': 1
        },
        bargap=0.33,
        autosize=True

    )
}
