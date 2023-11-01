import os
import re
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取配置信息
file_dir = config.get('file', 'output_dir')

# 获取当前目录下output_text文件夹中的所有txt文件
files = [f for f in os.listdir(file_dir) if f.endswith('.txt')]

# 创建一个新的txt文件，用于存储所有文件的内容
with open(os.path.join(file_dir, 'merged.txt'), 'w', encoding='utf-8') as merged_file:
    for file in files:
        with open(os.path.join(file_dir, file), 'r', encoding='utf-8') as f:
            content = f.read()
            # 在每个文件内容的末尾添加换行符，以便在合并时保留原始文件的结构
            merged_file.write(content + '\n')

# 读取合并后的文件内容
with open(os.path.join(file_dir, 'merged.txt'), 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式匹配中文字符和换行符，替换非中文字符为空字符
chinese_only = re.sub(r'[^\u4e00-\u9fa5\n]', '', content)

# 将处理后的结果保存到新的txt文件中
with open(os.path.join(file_dir, 'new_merged.txt'), 'w', encoding='utf-8') as f:
    f.write(chinese_only)
