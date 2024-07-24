from flask import Flask
from gdata import getData
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/info')
def info():
    system_info = getData()
    return system_info

if __name__ == '__main__':
    app.run(port=8831, debug=True, use_reloader=False)
