import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from graphs import *


nav = dbc.Nav([
    html.A(dbc.NavItem(dbc.NavLink(
        "Home", active=False, style={'color': 'grey'})), href='/', style={'text-decoration': 'none'}),
    dbc.NavItem(dbc.NavLink(
        "Dashboard", active=True, href="/dashboard/", style={
            'textAlign': 'center',
            'marginLeft': '-16px',
            'color': 'white'
        }))
], style={'textAlign': 'left', 'marginTop': '3px'}
)

navbar = dbc.Navbar(
    [
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row(
            [
                dbc.Col(nav, align="start", width=3),
                dbc.Col(dbc.NavbarBrand(
                    "Welcome To The News Analyzer",
                    className="", style={'marginLeft': '174px', 'font-size': 'x-large'}),
                    align="left", width=9
                )
            ], style={
                'width': '100%'
            }

        ),

        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    color="#344675",
    dark=True,
    className="navbar navbar-dark navbar-expand-md justify-content-between",
    style={
        'box-shadow': 'inset 0px 2px 0px rgb(255, 65, 128)'
    }
)

DESELECTED_STYLE = {
    'borderTop': 'none',
    'borderLeft': '2px solid #344675',
    'borderRight': '2px solid #344675',
    'borderBottom': 'none',
    'borderTopLeftRadius': '25px',
    'borderTopRightRadius': '25px',
    'background': '#1d2842',
    'color': 'white',
    'box-shadow': 'inset 0px 2px 0px rgba(255, 65, 128,0.2)',
    'transform': 'scaleY(0.9)',
    'marginBottom': '-3px',
    'font-size': '24px',
    'color': 'rgba(255,255,255,0.7)'

}

SELECTED_STYLE = {
    'borderTop': 'none',
    'borderLeft': '2px solid #344675',
    'borderRight': '2px solid #344675',
    'borderTopLeftRadius': '25px',
    'borderTopRightRadius': '25px',
    'box-shadow': 'inset 0px 2px 0px rgb(255, 65, 128)',
    'font-size': '24px',
    'color': 'rgba(0,0,0,0.7)'
}

GRAPH_STYLE = {
    'width': '48%',
    'textAlign': 'center',
    'float': 'left',
    'marginTop': '30px'
}


graph_tabs = dcc.Tabs(id="tabs", value='tab-1', children=[
    # CORRELATION MATRIX TAB
    dcc.Tab(label='Correlation Matrices', children=[
        html.Div(children=[
            html.Div(children=[
                html.H2('Fake News Feature Correlations',
                        style={'marginBottom': '-5px'}),
                dcc.Graph(
                    figure=fnum_corr_matrix
                ),
            ], style=GRAPH_STYLE),
            html.Div(children=[
                html.H2('Real News Feature Correlations',
                        style={'marginBottom': '-5px'}),
                dcc.Graph(
                    figure=rnum_corr_matrix
                ),
            ], style=GRAPH_STYLE),
        ], style={'marginLeft': '3%'})
    ], value='tab-1', style=DESELECTED_STYLE, selected_style=SELECTED_STYLE),
    # BAR GRAPHS TAB
    dcc.Tab(label='Bar Graphs', children=[
        html.Div(children=[
            html.Div(children=[
                dcc.Graph(
                    figure=fake_common_bar
                ),
            ], style=GRAPH_STYLE),
            html.Div(children=[
                dcc.Graph(
                    figure=real_common_bar
                ),
            ], style=GRAPH_STYLE)
        ], style={'marginLeft': '3%'})
    ],
        value='tab-3', style=DESELECTED_STYLE, selected_style=SELECTED_STYLE),
    # SCATTERPLOT TAB
    dcc.Tab(label='Scatter Plots', children=[
        html.Div(children=[
            html.Div(children=[
                dcc.Graph(
                    figure=overlayed_scatter_unique
                ),
            ], style=GRAPH_STYLE),
            html.Div(children=[
                dcc.Graph(
                    figure=overlayed_scatter_len
                ),
            ], style=GRAPH_STYLE)
        ], style={'marginLeft': '3%'})
    ], value='tab-2', style=DESELECTED_STYLE, selected_style=SELECTED_STYLE),
], style={'background': '#344675'}
)


# # add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open
