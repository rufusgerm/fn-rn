from flask import Flask, render_template, request
import pickle
from text_cleaning import clean_string
from sklearn.ensemble import VotingClassifier
from os import listdir


app = Flask(__name__)


@app.route('/')
def index():
    image_names = listdir('./static/images')
    return render_template('home.html', image_names=image_names)


@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        with open('./data/model_combo.pkl', 'rb') as file:
            combo_model = pickle.load(file)
        title = form['title']
        text = form['text']
        full_text = title + ' ' + text
        # input above returned data into model.predict AND model.predict_proba
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
