import psutil
import platform
import subprocess

def get_system_info():
    system_info = {}

    # 获取CPU型号
    cpu_info = subprocess.check_output("wmic cpu get name", shell=True).decode().strip().split("\n")[1]
    system_info['cpu_model'] = cpu_info.strip()

    # 获取显卡型号
    try:
        gpu_info = subprocess.check_output("wmic path win32_VideoController get name", shell=True).decode().strip().split("\n")[1]
        system_info['gpu_model'] = gpu_info.strip()
    except Exception as e:
        system_info['gpu_model'] = "Unknown"

    # 获取内存容量
    memory_info = psutil.virtual_memory()
    system_info['memory_capacity'] = f"{memory_info.total / (1024 ** 3):.2f} GB"

    # 获取硬盘容量
    disk_info = psutil.disk_usage('/')
    system_info['disk_capacity'] = f"{disk_info.total / (1024 ** 3):.2f} GB"

    # 获取操作系统
    system_info['os'] = platform.system() + " " + platform.release()

    # 其他软硬件相关信息
    system_info['platform'] = platform.platform()
    system_info['architecture'] = platform.machine()

    return system_info

if __name__ == "__main__":
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")
