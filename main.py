import sys
from preprocessing import Preprocessing
from filemanager import FileManager
from positional_index import PositionalIndex
import os


class Main:
    def __init__(self):
        print("Information Retrieval System ")

    @staticmethod
    def execute(file):

        if len(sys.argv) > 1:
            word = sys.argv[1]  # word to be processed
            mode = sys.argv[2]  # mode: --save to create the dictionary or --load to load it.
            if mode == '--save':
                df = FileManager().read_file(file)
                prep_df = Preprocessing().preprocessing(df)
                index = PositionalIndex().create_index(prep_df)
                # index_size = (sys.getsizeof(index) / 1024) / 1024
                # print("Size of Positional Index  w/o steeming (MB): ", index_size)
                FileManager.save_dict(index)
            elif mode == '--load':
                index = FileManager.load_dict()
            print("Length of dictionary: ", len(index))
            print(word)
            print(index[word])


if __name__ == '__main__':
    file = 'dataset/wiki_movie_plots_deduped.csv'
    Main.execute(file)
