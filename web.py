
from flask import Flask
from flask import send_file

app = Flask('RSA Scaler')

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print('booom')
    

@app.route('/download')
def downloadFile ():
    path = "~/peyman/pymahex-scaler/log.csv"
    return send_file(path, as_attachment=True)