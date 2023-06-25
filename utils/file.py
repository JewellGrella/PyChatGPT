# Desc: 文件操作工具类
import os
import shutil
import docx
import pandas as pd


# 判断路径下的文件是否存在,如果存在则移除所有子目录的文件并重新创建文件夹，如果不存在则创建文件夹
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)


# 判断路径是否存在
def is_dir_exists(path):
    return os.path.exists(path)


# 删除文件夹和文件
def delete_dir_and_files(path):
    if os.path.exists(path):
        shutil.rmtree(path)


# 返回目录下sufix后缀的文件名
def read_file(cur_dir, suffix):
    file_names = []
    for sub_file in os.listdir(cur_dir):
        # 遍历该文件夹下所有内容，可能有各自文件或者文件夹
        sub_file_abs_path = os.path.join(cur_dir, sub_file)  # 拼为完整路径，方便后面使用
        if os.path.isfile(sub_file_abs_path):
            # 判断是否为文件, 如果是文件，拼接完整path
            file_path = os.path.join(cur_dir, sub_file)
            if file_path.rsplit('.')[-1] == suffix:
                file_names.append(sub_file.split('.' + suffix)[0])
        else:
            sub_folder_path = os.path.join(cur_dir, sub_file)
            read_file(sub_folder_path, suffix)
    if file_names:
        return file_names
    else:
        return None


# 创建docx文件
def is_file_exists_or_create(file_path):
    if not os.path.exists(file_path):
        docx.Document().save(file_path)


if __name__ == '__main__':
    print(is_file_exists_or_create('D:\\GPT\\稿子.docx'))
