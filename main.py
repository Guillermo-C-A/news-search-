from noticias import Noticias
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def main_path():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   
    search = request.form['search']
    return render_template("plantilla.html",items = Noticias().get_news(search), busqueda=search)


if __name__ == '__main__':
    app.run(debug=True)


