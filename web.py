
from flask import Flask

app = Flask('RSA Scaler')

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print('booom')