import streamlit as st
import os
import shutil
import tempfile

# 设置页面标题
st.title('文件管理系统')

# 左侧区域布局
left_column, right_column = st.columns([1, 3])

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

    # 文件上传
    uploaded_file = st.file_uploader('上传文件', type=['txt', 'py', 'md', 'jpg', 'png'])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file.flush()
            shutil.move(tmp_file.name, os.path.join(current_dir, uploaded_file.name))
            st.write(f'文件 {uploaded_file.name} 已上传到 {current_dir}')

# 右侧区域：文件操作
with right_column:
    # 文件列表
    files = os.listdir(current_dir)
    selected_file = st.selectbox('选择文件', files)

    # 文件查看和编辑
    if selected_file:
        file_path = os.path.join(current_dir, selected_file)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = st.text_area('文件内容', value=file.read(), height=400)

            # 保存修改
            if st.button('保存修改'):
                with open(file_path, 'w') as file:
                    file.write(file_content)
                st.write(f'文件 {selected_file} 已保存')

            # 文件下载
            if st.button('下载文件'):
                with open(file_path, 'rb') as file:
                    st.download_button('下载', file.read(), file_name=selected_file)

            # 文件删除
            if st.button('删除文件'):
                os.remove(file_path)
                st.write(f'文件 {selected_file} 已删除')
