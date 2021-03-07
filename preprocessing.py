import re
import nltk
from tqdm import tqdm
import pandas as pd
import sys


class Preprocessing:
    def __init__(self):
        self.df = pd.DataFrame()

    @staticmethod
    def generate_tokens(input_text):
        no_citation = re.sub(r'\[\d+\]', ' ', input_text)
        no_nonalpha = re.sub(r'([^\s\w]|)+', '', no_citation)
        no_numbers = re.sub(r'\b[0-9]+\b\s*', '', no_nonalpha)
        #no_numbers = ' '.join(word.lower() for word in no_nonalpha.split() if not word.isdigit())
        tokens = nltk.word_tokenize(no_numbers)
        return tokens

    def preprocessing(self, df):
        self.df = df
        tqdm.pandas()
        nltk.download('punkt')
        print("Preprocessing & Generating tokens...")
        self.df["Tokens"] = self.df["Tokens"].progress_apply(self.generate_tokens)
        return self.df

