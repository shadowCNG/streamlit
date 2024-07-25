import streamlit as st
import subprocess

# 设置页面标题
st.title("Interactive Shell")

# 创建一个文本输入框，用于输入命令
command = st.text_input("Enter command:", "ls")

# 创建一个按钮，用于执行命令
if st.button("Execute"):
    # 使用 subprocess 模块执行命令
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # 显示命令的输出
    st.subheader("Output:")
    st.text(result.stdout)
    
    # 显示命令的错误信息（如果有）
    if result.stderr:
        st.subheader("Error:")
        st.text(result.stderr)

# 显示当前目录
st.subheader("Current Directory:")
current_dir = subprocess.run("pwd", shell=True, capture_output=True, text=True)
st.text(current_dir.stdout)
