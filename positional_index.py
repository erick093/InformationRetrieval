import pandas as pd
from tqdm import tqdm


class PositionalIndex:
    def __init__(self, df):
        self.df = df
        self.positional_index = {}

    def pos_index(self, tokens, doc_id):
        for pos, term in enumerate(tokens):
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

    def create_index(self):
        tqdm.pandas()
        print("Creating positional index...")
        self.df.progress_apply(lambda x: self.pos_index(x['Tokens'], x['ID']), axis=1)
        return self.positional_index




