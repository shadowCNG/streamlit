import streamlit as st
import subprocess

def get_system_info():
    system_info = {}

    # CPU 型号
    try:
        cpu_info = subprocess.run(['lscpu'], stdout=subprocess.PIPE, text=True, check=True)
        cpu_model = [line for line in cpu_info.stdout.split('\n') if 'Model name' in line]
        system_info['cpu_model'] = cpu_model[0].split(':')[-1].strip() if cpu_model else "N/A"
    except Exception as e:
        system_info['cpu_model'] = f"Error: {e}"

    # 显卡型号
    try:
        gpu_info = subprocess.run(['glxinfo'], stdout=subprocess.PIPE, text=True, check=True)
        gpu_model = [line.split(':')[-1].strip() for line in gpu_info.stdout.split('\n') if 'Device' in line]
        system_info['gpu_model'] = gpu_model[0] if gpu_model else "N/A"
    except Exception as e:
        system_info['gpu_model'] = f"Error: {e}"

    # 内存容量
    try:
        memory_info = subprocess.run(['cat', '/proc/meminfo'], stdout=subprocess.PIPE, text=True, check=True)
        memory_capacity = [line.split()[1] for line in memory_info.stdout.split('\n') if 'MemTotal' in line]
        if memory_capacity:
            memory_capacity_kb = int(memory_capacity[0])
            memory_capacity_gb = memory_capacity_kb / (1024 * 1024)
            system_info['memory_capacity'] = f"{memory_capacity_gb:.2f} GB"
        else:
            system_info['memory_capacity'] = "N/A"
    except Exception as e:
        system_info['memory_capacity'] = f"Error: {e}"

    # 硬盘容量
    try:
        disk_info = subprocess.run(['df', '-h', '/'], stdout=subprocess.PIPE, text=True, check=True)
        disk_capacity = [line.split()[1] for line in disk_info.stdout.split('\n') if '/' in line]
        system_info['disk_capacity'] = disk_capacity[0] if disk_capacity else "N/A"
    except Exception as e:
        system_info['disk_capacity'] = f"Error: {e}"

    # 操作系统
    try:
        os_info = subprocess.run(['uname', '-sr'], stdout=subprocess.PIPE, text=True, check=True)
        system_info['os'] = os_info.stdout.strip()
    except Exception as e:
        system_info['os'] = f"Error: {e}"

    # 其他软硬件相关信息
    try:
        other_info = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE, text=True, check=True)
        system_info['other_info'] = other_info.stdout.strip()
    except Exception as e:
        system_info['other_info'] = f"Error: {e}"

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
