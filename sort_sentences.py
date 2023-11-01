import os
from hanziconv import HanziConv
from operator import itemgetter
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取配置信息
file_dir = config.get('file', 'output_dir')
file_path = os.path.join(file_dir, 'new_merged.txt')

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 将所有的中文汉字转换为简体中文
simplified_lines = [HanziConv.toSimplified(line) for line in lines]

# 按照每行汉字的数量排序
sorted_lines = sorted(simplified_lines, key=len, reverse=True)

# 将排序后的结果保存到新的txt文件中
with open(os.path.join(file_dir, 'sorted_new_merged.txt'), 'w', encoding='utf-8') as f:
    f.writelines(sorted_lines)
