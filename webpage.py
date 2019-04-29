from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, SelectField
from jinja2 import Template
from language_list import Languages
app = Flask(__name__)


## List of Languages

@app.route("/")
def hello():
    return render_template('index.html', Languages=Languages)

@app.route("/results", methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		text = request.form['lang']
		lang1 = request.form['Language']

		print(text, lang1) 

	return render_template('results.html', text=text, lang1=lang1, Languages=Languages)




# runs the program wihout doing flask run....
if __name__ == '__main__':
    	app.run(debug=True)
