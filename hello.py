from flask import Flask

app = Flask(__name__)

@app.route('/')

def el_que_me_de_la_gana():
    return "Hola, mundo"

@app.route('/bye')
def otro():
    return "Adiós, mundo cruel!"