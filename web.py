
from flask import Flask
from flask import send_file, send_from_directory
from pathlib import Path 
app = Flask('RSA Scaler')

@app.route('/')
def index():
    return 'Hello world'



@app.route('/download')
def downloadFile():
    path = "/home/peyman/pymahex-scaler"
    return send_from_directory(path, "log.csv", as_attachment=True)


@app.route('/clear')
def clear():
    log_file = Path(__file__).with_name('log.csv')
    record = 'barcode,datetime,weight,result'
    with open(log_file, "w") as logger:
        logger.write(record)
    return 'Cleared'


@app.route('/buzzer')
def buzzer():
    import buzzer
    buzzer.click()
    return 'buuuuuuuuuuuuz'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print('booom')
    