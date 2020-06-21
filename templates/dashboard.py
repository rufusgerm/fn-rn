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

TAB_STYLE = {
    'border': 'none',
    'background': '#1d2842',
    'color': 'white'
}

SELECTED_TAB_STYLE = {
    'border': 'none',
    'box-shadow': 'inset 0px 2px 0px rgb(255, 65, 128)'
}

graph_tabs = dcc.Tabs(id="tabs", value='tab-1', children=[
    dcc.Tab(label='Correlation Matrices', children=[fnum_corr_matrix], value='tab-1',
            style=TAB_STYLE, selected_style=SELECTED_TAB_STYLE),
    dcc.Tab(label='Scatter Plots', value='tab-2',
            style=TAB_STYLE, selected_style=SELECTED_TAB_STYLE),
    dcc.Tab(label='Bar Graphs', value='tab-3',
            style=TAB_STYLE, selected_style=SELECTED_TAB_STYLE)
], )


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
