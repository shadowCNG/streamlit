from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/info')
def info():
    # 获取CPU信息
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # 获取内存信息
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    
    # 获取硬盘信息
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    
    # 构建返回的JSON信息
    system_info = {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent
    }
    
    return system_info

if __name__ == '__main__':
    app.run(port=8171, debug=True,use_reloader=False)
