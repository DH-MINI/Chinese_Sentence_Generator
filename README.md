# Chinese sentence generator and organizer

## Project description
This project contains three main Python scripts that use thesaurus and gpt to generate Chinese sentences, merge and clean the generated sentences, and sort the sentences for easy processing.

## File structure
```
- README.md
- generate_sentences.py
- merge_and_clean.py
- sort_sentences.py
- config.ini
- requirements.txt
```

## How to use
1. Clone or download the project to your local machine.
```
git clone https://github.com/DH-MINI/Chinese_Sentence_Generator
```
2. Install the necessary Python libraries.
```
pip install -r requirements.txt
```
3. Set your OpenAI API key, thesaurus path, sentence save path, and the number of loops for large and small rounds in the 'config.ini' file.
4. Run 'generate_sentences.py' to generate sentences.
5. Run 'merge_and_clean.py' to merge and clean up sentences.
6. Run 'sort_sentences.py' to sort the sentences.

## Precautions
Make sure you have all the necessary Python libraries installed before running these scripts and that you have set the correct OpenAI API key.
