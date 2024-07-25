import streamlit as st
import os
import shutil
import tempfile

# 设置页面标题
st.title('文件管理系统')

# 初始化当前目录
if 'current_dir' not in st.session_state:
    st.session_state.current_dir = os.getcwd()

# 侧边栏显示目录结构
st.sidebar.title('目录结构')

def list_files_and_dirs(directory):
    items = os.listdir(directory)
    files = []
    dirs = []
    for item in items:
        if os.path.isdir(os.path.join(directory, item)):
            dirs.append(item)
        else:
            files.append(item)
    return dirs, files

dirs, files = list_files_and_dirs(st.session_state.current_dir)

# 显示目录
selected_dir = st.sidebar.selectbox('选择目录', ['/'] + dirs)
if selected_dir != '/':
    st.session_state.current_dir = os.path.join(st.session_state.current_dir, selected_dir)
    st.sidebar.write(f'当前目录: {st.session_state.current_dir}')

# 显示文件
selected_file = st.sidebar.selectbox('选择文件', files)

# 主页面显示文件内容和操作选项
if selected_file:
    file_path = os.path.join(st.session_state.current_dir, selected_file)

    # 文件内容
    file_content = open(file_path, 'r').read()
    st.text_area('文件内容', value=file_content, height=300)

    # 文件操作
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('编辑文件'):
            new_content = st.text_area('编辑文件内容', value=file_content, height=300)
            if st.button('保存'):
                with open(file_path, 'w') as file:
                    file.write(new_content)
                st.write('文件已保存')

    with col2:
        if st.button('下载文件'):
            with open(file_path, 'rb') as file:
                st.download_button('下载', file.read(), file_name=selected_file)

    with col3:
        if st.button('删除文件'):
            os.remove(file_path)
            st.write(f'文件 {selected_file} 已删除')
            st.sidebar.success('文件已删除')

# 文件上传
uploaded_file = st.file_uploader('上传文件', type=['txt', 'py', 'md', 'jpg', 'png'])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file.flush()
        shutil.move(tmp_file.name, os.path.join(st.session_state.current_dir, uploaded_file.name))
        st.write(f'文件 {uploaded_file.name} 已上传到 {st.session_state.current_dir}')
        st.sidebar.success('文件已上传')
