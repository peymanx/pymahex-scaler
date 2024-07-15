from flask import Flask
app = Flask('RSA Scaler')

@app.route('/')
def root():
   return 'Hello'

if __name__ == '__main__':
   app.run()
