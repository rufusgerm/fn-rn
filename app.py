from flask import Flask, render_template, request
import pickle
from text_cleaning import clean_string
from sklearn.ensemble import VotingClassifier
from os import listdir
import json


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
        with open('./data/model_combo.pkl', 'rb') as file:
            combo_model = pickle.load(file)
        title = form['title']
        text = form['text']
        full_text = title + ' ' + text

        pred = combo_model.predict([full_text])
        pred = pred[0]
        pred_proba = combo_model.predict_proba([full_text])*100
        pred_proba = max(pred_proba[0])
    return render_template('results.html', pred=pred, pred_proba=pred_proba)


@ app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True)
