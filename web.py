
from flask import Flask,send_file, send_from_directory, render_template, jsonify
from pathlib import Path 
import os


app_name = 'RSA Scaler'


app = Flask(app_name,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/barcode')
def barcode():
    return render_template('barcode.html')

@app.route('/troubleshoots')
def troubleshoots():
    return render_template('troubleshoots.html')



@app.route('/download')
def downloadFile():
    path = "/home/peyman/pymahex-scaler"
    return send_from_directory(path, "log.csv", as_attachment=True)


@app.route('/clear')
def clear():
    log_file = Path(__file__).with_name('log.csv')
    record = 'barcode,datetime,weight,result\r\n'
    with open(log_file, "w") as logger:
        logger.write(record)
    return 'Cleared'



@app.route('/getdata')
def get_data():
    barcode = 'not set'
    weight = -2
    last_barcode = Path(__file__).with_name('barcode.txt')
    with open(last_barcode, "r") as file:
        barcode = file.readline()
        
    last_weight = Path(__file__).with_name('weight.txt')
    with open(last_weight, "r") as file:
        weight = file.readline()

    return jsonify(weight=weight, barcode = barcode)

@app.route('/buzzer')
def buzzer():
    import buzzer
    buzzer.play(0.03)
    return 'buuuuuuuuuuuuz'

@app.route('/intro')
def introduction():
    import intro
    intro.run(4)
    return 'intro done'

@app.route('/led/<name>')
def leds(name):
    import leds
    match name:
        case 'tehran':
            leds.tehran.invert()
        case 'providence':
            leds.providence.invert()
        case 'reject':
            leds.reject.invert()
        case 'error':
            leds.error.invert()
            
            
    return 'intro done'



app.run(debug=True, host='0.0.0.0')

    