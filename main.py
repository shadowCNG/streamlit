import psutil
import requests
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
import requests

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
    print(info())
    # 示例调用
    print(get_public_ip())
