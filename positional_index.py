import pandas as pd
from tqdm import tqdm
from stemmer import PorterStemmer
import time

class PositionalIndex:
    def __init__(self):
        self.df = pd.DataFrame()
        self.positional_index = {}
        self.stem_flag = False

    def pos_index(self, tokens, doc_id):
        if self.stem_flag:
            stemmer = PorterStemmer()
        for pos, term in enumerate(tokens):
            if self.stem_flag:
                term = stemmer.stem(term)
            if term in self.positional_index:
                self.positional_index[term][0] += 1
                if doc_id in self.positional_index[term][1]:
                    self.positional_index[term][1][doc_id].append(pos)
                else:
                    self.positional_index[term][1][doc_id] = [pos]
            else:
                self.positional_index[term] = []
                self.positional_index[term].append(1)
                self.positional_index[term].append({})
                self.positional_index[term][1][doc_id] = [pos]

    def create_index(self, df, flag):
        self.df = df
        self.stem_flag = flag
        tqdm.pandas()
        print("Creating positional index...")
        start = time.time()
        self.df.progress_apply(lambda x: self.pos_index(x['Tokens'], x['ID']), axis=1)
        end = time.time()
        exec_time = round(end-start)
        print("Index created in {} seconds | stem={}".format(exec_time, self.stem_flag))
        return self.positional_index




