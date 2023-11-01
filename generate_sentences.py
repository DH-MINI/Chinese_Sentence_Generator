import os
import openai
import random
import logging
import re
import time
from datetime import datetime
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取配置信息
openai.api_key = config.get('openai', 'api_key')
file_path = config.get('file', 'word_list_path')
big_rounds = config.getint('loop', 'big_rounds')
small_rounds = config.getint('loop', 'small_rounds')

# 创建 log 文件夹
if not os.path.exists("log"):
    os.makedirs("log")

prompt_word = None

# 读取分词表
def read_word_list_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 提取每行的分词
    word_list = [line.split()[0] for line in lines]
    return word_list

# 生成句子
def generate_sentence(word_list):
    global prompt_word
    # 从分词表中随机选择一个词作为提示词
    prompt_word = random.choice(word_list)
    prompt = f"生成包含\"{prompt_word}\"的10句每句约55字最多80字避免句首用此词"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=800
        )
        return response.choices[0].text.strip()
    
    except Exception as e:
        logging.error(f"Error: {e}")
        time.sleep(5)
        return None

# 读分词表
word_list = read_word_list_from_txt(file_path)
current_time = datetime.now().strftime("%Y%m%d%H%M%S")

# 创建 output_text 文件夹
if not os.path.exists("output_text"):
    os.makedirs("output_text")

for big_round in range(1, big_rounds + 1):
    
    for small_round in range(1, small_rounds + 1):        
        sentence = generate_sentence(word_list)

        if sentence is not None:
            print(f'\n---\n')
            print(sentence)
            print(f'\n---\n')
            
            with open(
                f"output_text/{current_time}_{big_round}.txt", "a", encoding="utf-8"
            ) as output_file:
                output_file.write(sentence + "\n")

            progress_bar_length = 50
            progress = (big_round - 1) * 100 + small_round
            filled_length = int(progress_bar_length * progress // (big_rounds * small_rounds))
            bar = '█' * filled_length + '-' * (progress_bar_length - filled_length)
            
            print(f'\n---\n')
            print(f'\r当前进度: [{bar}] {progress}/{big_rounds * small_rounds} 大轮次: {big_round} 小轮次: {small_round} \n 用{prompt_word}生成的句子: \n{sentence}', end = '\r')
            print(f'\n---\n')
        time.sleep(3)
