from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, SelectField
from jinja2 import Template
app = Flask(__name__)


## List of Languages
Languages = [('Afrikaans', 'af'), ('Albanian', 'sq'), ('Amharic', 'am'), ('Arabic', 'ar'), ('Armenian', 'hy'), 
('Azerbaijani', 'az'), ('Basque', 'eu'), ('Belarusian', 'be'), ('Bengali', 'bn'), ('Bosnian', 'bs'), ('Bulgarian', 'bg'), 
('Catalan', 'ca'), ('Cebuano', 'ceb'), ('Chichewa', 'ny'), ('Chinese (Simplified)', 'zh'), ('Chinese (Traditional)', 'zh-TW'),
('Corsican', 'co'), ('Croatian', 'hr'), ('Czech', 'cs'), ('Danish', 'da'), ('Dutch', 'nl'), ('English', 'en'), ('Esperanto', 'eo'), 
('Estonian', 'et'), ('Filipino', 'tl'), ('Finnish', 'fi'), ('French', 'fr'), ('Frisian', 'fy'), ('Galician', 'gl'), ('Georgian', 'ka'), 
('German', 'de'), ('Greek', 'el'), ('Gujarati', 'gu'), ('Haitian Creole', 'ht'), ('Hausa', 'ha'), ('Hawaiian', 'haw'), ('Hebrew', 'iw'), 
('Hindi', 'hi'), ('Hmong', 'hmn'), ('Hungarian', 'hu'), ('Icelandic', 'is'), ('Igbo', 'ig'), ('Indonesian', 'id'), ('Irish', 'ga'), ('Italian', 'it'), 
('Japanese', 'ja'), ('Javanese', 'jw'), ('Kannada', 'kn'), ('Kazakh', 'kk'), ('Khmer', 'km'), ('Korean', 'ko'), ('Kurdish (Kurmanji)', 'ku'), ('Kyrgyz', 'ky'), 
('Lao', 'lo'), ('Latin', 'la'), ('Latvian', 'lv'), ('Lithuanian', 'lt'), ('Luxembourgish', 'lb'), ('Macedonian', 'mk'), ('Malagasy', 'mg'), ('Malay', 'ms'),
('Malayalam', 'ml'), ('Maltese', 'mt'), ('Maori', 'mi'), ('Marathi', 'mr'), ('Mongolian', 'mn'), ('Myanmar (Burmese)', 'my'), ('Nepali', 'ne'), ('Norwegian', 'no'),
('Pashto', 'ps'), ('Persian', 'fa'), ('Polish', 'pl'), ('Portuguese', 'pt'), ('Punjabi', 'pa'), ('Romanian', 'ro'), ('Russian', 'ru'), ('Samoan', 'sm'), 
('Scots Gaelic', 'gd'), ('Serbian', 'sr'), ('Sesotho', 'st'), ('Shona', 'sn'), ('Sindhi', 'sd'), ('Sinhala', 'si'), ('Slovak', 'sk'), ('Slovenian', 'sl'), ('Somali', 'so'),
('Spanish', 'es'), ('Sundanese', 'su'), ('Swahili', 'sw'), ('Swedish', 'sv'), ('Tajik', 'tg'), ('Tamil', 'ta'), ('Telugu', 'te'), ('Thai', 'th'), ('Turkish', 'tr'), 
('Ukrainian', 'uk'), ('Urdu', 'ur'), ('Uzbek', 'uz'), ('Vietnamese', 'vi'), ('Welsh', 'cy'), ('Xhosa', 'xh'), ('Yiddish', 'yi'), ('Yoruba', 'yo'), ('Zulu', 'zu')]



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