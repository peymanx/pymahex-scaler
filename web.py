
from flask import Flask
from flask import send_file, send_from_directory

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
    path = "/home/peyman/pymahex-scaler/log.csv"
    return send_file(path, as_attachment=True)


@app.route('/buzzer')
def buzzer():
    import buzzer
    buzzer.click()
    return 'buuuuuuuuuuuuz'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print('booom')
    