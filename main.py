import streamlit as st
import psutil
import platform
import GPUtil
import subprocess

def get_system_info():
    system_info = {}

    # CPU 型号
    system_info['cpu_model'] = platform.processor()

    # 显卡型号
    gpus = GPUtil.getGPUs()
    if gpus:
        system_info['gpu_model'] = gpus[0].name
    else:
        system_info['gpu_model'] = "N/A"

    # 内存容量
    memory = psutil.virtual_memory()
    system_info['memory_capacity'] = f"{memory.total / (1024 ** 3):.2f} GB"

    # 硬盘容量
    disk = psutil.disk_usage('/')
    system_info['disk_capacity'] = f"{disk.total / (1024 ** 3):.2f} GB"

    # 操作系统
    system_info['os'] = platform.system() + " " + platform.release()

    # 其他软硬件相关信息
    system_info['other_info'] = platform.uname()._asdict()

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
    for key, value in system_info['other_info'].items():
        st.write(f"**{key}:** {value}")

if __name__ == "__main__":
    main()
