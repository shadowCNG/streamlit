import streamlit as st
import os
import shutil
import tempfile
import subprocess

# 设置页面标题
st.title('文件管理系统')

# 页面布局
left_column, middle_column, right_column = st.columns([2, 3, 2])

# 左侧区域：目录选择和上传按钮
with left_column:
    # 获取当前目录
    current_dir = st.text_input('当前目录', os.getcwd())

    # 浏览目录
    if st.button('浏览目录'):
        files = os.listdir(current_dir)
        selected_file = st.selectbox('选择文件或目录', files)
        st.write(f'你选择了: {selected_file}')

        # 如果是目录，切换到该目录
        if os.path.isdir(os.path.join(current_dir, selected_file)):
            current_dir = os.path.join(current_dir, selected_file)
            st.write(f'切换到目录: {current_dir}')

    # 文件上传（不限类型和大小）
    uploaded_file = st.file_uploader('上传文件')
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file.flush()
            shutil.move(tmp_file.name, os.path.join(current_dir, uploaded_file.name))
            st.write(f'文件 {uploaded_file.name} 已上传到 {current_dir}')

# 中部区域：文件选择、查看修改、保存、下载和删除按钮
with middle_column:
    # 文件列表
    files = os.listdir(current_dir)
    selected_file = st.selectbox('选择文件', files)

    # 文件查看和编辑
    if selected_file:
        file_path = os.path.join(current_dir, selected_file)
        if os.path.isfile(file_path):
            # 尝试读取文件内容，处理不同文件类型
            try:
                with open(file_path, 'r') as file:
                    file_content = st.text_area('文件内容', value=file.read(), height=400)
            except UnicodeDecodeError:
                st.write('该文件类型不支持直接编辑')
                file_content = None

            # 按钮水平排列
            button_col1, button_col2, button_col3 = st.columns(3)

            # 保存修改
            with button_col1:
                if file_content is not None and st.button('保存修改'):
                    with open(file_path, 'w') as file:
                        file.write(file_content)
                    st.write(f'文件 {selected_file} 已保存')

            # 文件下载
            with button_col2:
                if st.button('下载文件'):
                    with open(file_path, 'rb') as file:
                        st.download_button('下载', file.read(), file_name=selected_file)

            # 文件删除
            with button_col3:
                if st.button('删除文件'):
                    os.remove(file_path)
                    st.write(f'文件 {selected_file} 已删除')

# 右侧区域：交互式Shell
with right_column:
    with st.expander('交互式Shell'):
        shell_command = st.text_area('输入命令', height=100)
        if st.button('执行命令'):
            try:
                result = subprocess.run(shell_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_dir)
                st.code(result.stdout.decode('utf-8'))
            except subprocess.CalledProcessError as e:
                st.error(f'命令执行失败: {e.stderr.decode("utf-8")}')
