from flask import Flask, render_template, request, redirect
from wtforms import Form, StringField, SelectField
from jinja2 import Template
from language_list import Languages
from functions import *
import urllib, os, requests
import imageSearchEnhanced as imageSearch

app = Flask(__name__)

"""
The homepage route, which renders the template defined in index.html
and passes a list of tuples to that template. Each tuple consists of a 
language and a 2 letter abbreviation. The full length name populates a 
drop down menu, and the 2 letter abbreviation is used by the translate
API.
"""

@app.route("/")
def hello():
    return render_template('index.html', Languages=Languages)

"""
The results page function is called on home page button click,
as the home page method is POST. Upon running, the entered text 
is stored as 'text' and the chosen language is 'lang1'. The 
list of tuples is then searched for 'lang1' to find the matching
abbreviation. The string and destination language are then passed 
to the custom convert function, returning a translated string. 
An object of the imageSearch class is instantiated with the 
translated string, generating a list of urls for the first 100 images.
The results page is then rendered with the above information.
"""

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
        images = imageSearch.imageSearch(translated, '', 0, 100)
        imageList = images.getLinkList()
    return render_template('results.html', text=text, lang1=lang1, translated=translated, Languages=Languages, imageList=imageList)

"""
Currently not working page to display single image at full size
when a user clicks one from the results page.
"""
@app.route("/<search>")
def single_image(search, url):
    image=urllib.URLopener()
    image.retrieve(url, 'static/single_image')
    #generate the image path for url_for later
    filename = url
    #the file is stored in a static folder, as id.jpg
    img = Image.open(filename)
    #open the file to use pillow methods for properties
    imgFormat = img.format
    mode = img.mode
    width, height = img.size
    title = search

    return render_template('single.html', url=url, mode=mode, imgFormat=imgFormat, width=width, height=height,title=title)

# runs the program wihout doing flask run....
if __name__ == '__main__':
    app.run(debug=True)
