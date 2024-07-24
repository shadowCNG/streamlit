from flask import Flask
from gdata import getData
import requests
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/info')
def info():
    system_info = getData()
    return system_info
    
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        public_ip = response.json()['ip']
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        public_ip = None
    return public_ip

if __name__ == '__main__':
    # os.write(1, f"{get_public_ip()}\n".encode())
    app.run(port=8145, debug=True, use_reloader=False)
