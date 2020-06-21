import pandas as pd
from plotly import express, figure_factory as ff

fnum_df = pd.read_csv('./data/fnum_df.csv')
rnum_df = pd.read_csv('./data/rnum_df.csv')

fnum_corr_matrix = ff.create_annotated_heatmap(
    z=fnum_df.values,
    x=list(fnum_df.columns),
    y=list(fnum_df.index),
    annotation_text=fnum_df.round(2).values,
    showscale=True)
