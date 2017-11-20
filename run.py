from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
from stki_scripts.main import findSim
from stki_scripts.main import findBow
from stki_scripts.main import findHoax

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='12345'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword')
    search = SubmitField('Search')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text files/"
    res = findSim(keyword, path_corpus)
    # res = {"title 1":0.3, "title 2":0.5, "title 3":1.3} # change the value here
    return res

def searchBow(form):
    keyword = form.keyword.data
    path_corpus = "./text files/"
    res = findBow(keyword, path_corpus)
    # res = {"title 1":0.3, "title 2":0.5, "title 3":1.3} # change the value here
    return res

def searchHoax(form):
    keyword = form.keyword.data
    path_corpus = "./text files/"
    res = findHoax(keyword, path_corpus)
    # res = {"title 1":0.3, "title 2":0.5, "title 3":1.3} # change the value here
    return res

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')
    
    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchHoax(sform)

    total = 0
    number = 0
    for key, value in data:
        total += key[1]
        number += 1 

    if number==0:
        prosentase = 0
    else:
        prosentase = round(total/number, 2)

    # render HTML
    return render_template('index.html', sform = sform, data = data, prosentase = prosentase)

@app.route('/represent', methods=['GET','POST'])
def represent():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)
    
    # render HTML
    return render_template('home.html', sform = sform, data = data)

@app.route('/bow', methods=['GET','POST'])
def tampil():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchBow(sform)
    
    # render HTML
    return render_template('bow.html', sform = sform, data = data)

@app.route('/cekHoax', methods=['GET','POST'])
def cek():
    # create form
    sform = SearchTask(prefix='sform')
    
    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchHoax(sform)

    # render HTML
    return render_template('hoax.html', sform = sform, data = data)

if __name__=='__main__':
    app.run(debug=True)