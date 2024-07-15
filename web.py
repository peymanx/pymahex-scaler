
from flask import Flask,send_file, send_from_directory, render_template, jsonify
from pathlib import Path 
import os


app_name = 'RSA Scaler'
app = Flask(app_name)

@app.route('/')
def index():
    return render_template('index.html')


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
    weight = os.environ.get('global_weight', -1)
    barcode = os.environ.get('global_barcode', 'not set')
    return jsonify(weight=weight, barcode = barcode)

@app.route('/buzzer')
def buzzer():
    import buzzer
    buzzer.play(0.3)
    return 'buuuuuuuuuuuuz'

@app.route('/intro')
def introduction():
    import intro
    intro.run(12)
    return 'intro done'




app.run(debug=True, host='0.0.0.0')

    