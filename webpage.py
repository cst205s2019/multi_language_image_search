from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, SelectField
from jinja2 import Template
from language_list import Languages
from functions import *

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', Languages=Languages)

@app.route("/results", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        res = ""
        text = request.form['lang']
        lang1 = request.form['Language']
        for x in Languages:
            if x[0] == lang1:
                res = x[1]
                break
        print(lang1, res)
        if lang1 == 'secret':
            res = 'en'
            lang1 = "English"
        translated = custom_convert(text, res)
    return render_template('results.html', text=text, lang1=lang1, translated=translated, Languages=Languages)




# runs the program wihout doing flask run....
if __name__ == '__main__':
    app.run(debug=True)
