import requests
import PySimpleGUI as sg
import os
import json
from flask import Flask, render_template

class Noticias():

    def __init__(self):

        if not os.path.isfile('API.txt'):

            layout = [
                        [sg.Text('Obten una API key en:'), sg.Input('https://newsapi.org/register')],
                        [sg.Text('API KEY'), sg.Input(key='api')],
                        [sg.OK()]
                    ]

            window = sg.Window('API REGISTER', layout)

            while True:
                event, values = window.read()
                if event is None or event == 'Exit' or values['api'] != '':
                    file = open('API.txt','w')
                    file.write(values['api'])
                    file.close()
                    window.close()
                    break

        file = open('API.txt', 'r')
        self.api = file.read()
        file.close()

    def get_news(self, busqueda):

        url = ('http://newsapi.org/v2/everything?'
               f'q={busqueda}&'
               'sortBy=popularity&'
               f'apiKey={self.api}')

        response = requests.get(url).text
        return json.loads(response)['articles']


