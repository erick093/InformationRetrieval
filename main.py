import sys
from preprocessing import Preprocessing
from reader import Reader
from positional_index import PositionalIndex
import os

class Main:
    def __init__(self):
        print("Information Retrieval System ")

    @staticmethod
    def execute(file):
        df = Reader(file).read_file()
        prep_df = Preprocessing(df).preprocessing()
        index = PositionalIndex(prep_df).create_index()
        index_size = (sys.getsizeof(index)/1024)/1024
        print("Size of Positional Index  w/o steeming (MB): ", index_size)
        if len(sys.argv) > 1:
            word = sys.argv[1]
            print(word)
            print(index[word])


if __name__ == '__main__':
    file = 'dataset/wiki_movie_plots_deduped.csv'
    Main.execute(file)
