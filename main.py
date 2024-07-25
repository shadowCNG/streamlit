import streamlit as st
import subprocess
import time

# 设置页面标题
st.title("Interactive Shell")

# 创建一个文本输入框，用于输入命令
command = st.text_input("Enter command:", "ls")

# 创建一个密码输入框，用于输入 sudo 密码
sudo_password = st.text_input("Enter sudo password:", type="password")

# 创建一个按钮，用于执行命令
if st.button("Execute"):
    # 使用 subprocess 模块执行命令
    full_command = f"echo {sudo_password} | sudo -S {command}"
    process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # 创建占位符用于动态显示输出
    output_placeholder = st.empty()
    
    # 循环读取命令的输出并动态更新页面
    stdout_lines = []
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            stdout_lines.append(output.strip())
            output_placeholder.code('\n'.join(stdout_lines))
        time.sleep(0.1)
    
    # 获取命令的最终输出和错误信息
    stdout, stderr = process.communicate()
    
    # 显示命令的最终输出
    st.subheader("Final Output:")
    st.code(stdout)
    
    # 显示命令的错误信息（如果有）
    if stderr:
        st.subheader("Error:")
        st.code(stderr)

# 显示当前目录
st.subheader("Current Directory:")
current_dir = subprocess.run("pwd", shell=True, capture_output=True, text=True)
st.text(current_dir.stdout)
