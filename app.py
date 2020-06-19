from flask import Flask, render_template, request
import pickle
from data_frame_creation import create_num_df
from sklearn.ensemble import VotingClassifier
from os import listdir
import json
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)


@app.route('/')
def index():
    image_names = listdir('./static/images')

    with open('./data/article_examples.json', 'r') as f:
        json_content = f.read()
    json_content = json_content.rstrip(",")
    art_str = json_content
    articles = json.loads(art_str)

    return render_template('home.html', image_names=image_names, articles=articles)


@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        with open('./data/lrfc_model.pkl', 'rb') as file:
            num_model = pickle.load(file)
        title = form['title']
        text = form['text']

        num_df = create_num_df((title, text))

        pred = num_model.predict(num_df)
        pred = pred[0]
        pred_proba = num_model.predict_proba(num_df)*100
        pred_proba = max(pred_proba[0])
    return render_template('results.html', pred=pred, pred_proba=pred_proba)


@ app.route('/dashboard')
def about():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True)
