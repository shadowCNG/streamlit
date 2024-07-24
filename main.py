import streamlit as st
import subprocess

def get_system_info():
    system_info = {}

    # CPU 型号
    cpu_info = subprocess.run(['lscpu'], stdout=subprocess.PIPE, text=True)
    cpu_model = [line for line in cpu_info.stdout.split('\n') if 'Model name' in line]
    system_info['cpu_model'] = cpu_model[0].split(':')[-1].strip() if cpu_model else "N/A"

    # 显卡型号
    gpu_info = subprocess.run(['lspci', '|', 'grep', 'VGA'], stdout=subprocess.PIPE, shell=True, text=True)
    gpu_model = gpu_info.stdout.strip().split(':')[-1].strip() if gpu_info.stdout else "N/A"
    system_info['gpu_model'] = gpu_model

    # 内存容量
    memory_info = subprocess.run(['free', '-h'], stdout=subprocess.PIPE, text=True)
    memory_capacity = [line.split()[1] for line in memory_info.stdout.split('\n') if 'Mem' in line]
    system_info['memory_capacity'] = memory_capacity[0] if memory_capacity else "N/A"

    # 硬盘容量
    disk_info = subprocess.run(['df', '-h', '/'], stdout=subprocess.PIPE, text=True)
    disk_capacity = [line.split()[1] for line in disk_info.stdout.split('\n') if '/' in line]
    system_info['disk_capacity'] = disk_capacity[0] if disk_capacity else "N/A"

    # 操作系统
    os_info = subprocess.run(['uname', '-sr'], stdout=subprocess.PIPE, text=True)
    system_info['os'] = os_info.stdout.strip()

    # 其他软硬件相关信息
    other_info = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE, text=True)
    system_info['other_info'] = other_info.stdout.strip()

    return system_info

def main():
    st.title("系统信息展示")

    system_info = get_system_info()

    st.write(f"**CPU 型号:** {system_info['cpu_model']}")
    st.write(f"**显卡型号:** {system_info['gpu_model']}")
    st.write(f"**内存容量:** {system_info['memory_capacity']}")
    st.write(f"**硬盘容量:** {system_info['disk_capacity']}")
    st.write(f"**操作系统:** {system_info['os']}")

    st.subheader("其他软硬件相关信息")
    st.write(f"**详细信息:** {system_info['other_info']}")

if __name__ == "__main__":
    main()
