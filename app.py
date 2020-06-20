from flask import Flask, render_template, request, redirect
import pickle
from data_frame_creation import create_num_df
from os import listdir
import json
from dash import Dash
import dash_bootstrap_components as dbc

import dash_html_components as html
from dash_comps import navbar, graph_tabs

server = Flask(__name__)

app = Dash(__name__, server=server, url_base_pathname='/dashboard/',
           external_stylesheets=[dbc.themes.BOOTSTRAP])


@server.route('/')
def index():
    image_names = listdir('./static/images')

    with open('./data/article_examples.json', 'r') as f:
        json_content = f.read()
    json_content = json_content.rstrip(",")
    art_str = json_content
    articles = json.loads(art_str)

    return render_template('home.html', image_names=image_names, articles=articles)


@server.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        with open('./data/lrfc_model.pkl', 'rb') as file:
            num_model = pickle.load(file)
        title = form['title']
        text = form['text']

        num_df = create_num_df((title, text))

        pred = num_model.predict(num_df)
        pred = "True" if pred[0] == 1 else "False"
        pred_proba = num_model.predict_proba(num_df)*100
        pred_proba = max(pred_proba[0])
    return render_template('results.html', pred=pred, pred_proba=pred_proba)


app.layout = html.Div(children=[
    navbar,
    graph_tabs
])


if __name__ == '__main__':
    app.run_server(host="localhost", port=8080, debug=True)
