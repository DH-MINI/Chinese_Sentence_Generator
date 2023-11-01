# 中文句子生成器和整理器

## 项目描述
这个项目包含三个主要的Python脚本，用于利用分词表和gpt来进行生成中文句子，合并和清理生成的句子，以及对句子进行排序方便进行处理。

## 文件结构
```
- README.md
- generate_sentences.py
- merge_and_clean.py
- sort_sentences.py
- config.ini
- requirements.txt
```

## 使用方法
1. 克隆或下载此项目到你的本地机器上。
```
git clone https://github.com/DH-MINI/Chinese_Sentence_Generator
```
2. 安装必要的Python库。
```
pip install -r requirements.txt
```
3. 在 `config.ini` 文件中设置你的OpenAI API密钥，分词表路径，句子保存路径，以及大轮次和小轮次的循环次数。
4. 运行 `generate_sentences.py` 生成句子。
5. 运行 `merge_and_clean.py` 合并和清理句子。
6. 运行 `sort_sentences.py` 对句子进行排序。

## 注意事项
请确保在运行这些脚本之前已经安装了所有必要的Python库，并且已经设置了正确的OpenAI API密钥。
