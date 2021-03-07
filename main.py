import sys
from preprocessing import Preprocessing
from filemanager import FileManager
from positional_index import PositionalIndex
from stemmer import PorterStemmer


class Main:
    def __init__(self):
        print("Information Retrieval System ")

    @staticmethod
    def execute(file):

        if len(sys.argv) > 1:
            word = sys.argv[1]  # word to be processed
            stem = sys.argv[2]  # flag if true -> stem
            mode = sys.argv[3]  # mode: --save to create the dictionary or --load to load it.
            if mode == '--save':
                df = FileManager().read_file(file)
                prep_df = Preprocessing().preprocessing(df)
                if stem == '--stem':
                    index = PositionalIndex().create_index(prep_df, True)
                elif stem == '--nostem':
                    index = PositionalIndex().create_index(prep_df, False)
                else:
                    print("ERROR: Second argument has to be stem or nostem, depending if you want to stemm or not")
                    sys.exit(1)
                # index_size = (sys.getsizeof(index) / 1024) / 1024
                # print("Size of Positional Index  w/o steeming (MB): ", index_size)
                FileManager.save_dict(index, stem)
            elif mode == '--load':
                index = FileManager.load_dict(stem)
            print("Length of dictionary: {}, stem:{} ".format(len(index), stem))
            print(word)
            stemmer = PorterStemmer()
            print(stemmer.stem(word))
            print(index[stemmer.stem(word)])


if __name__ == '__main__':
    file = 'dataset/wiki_movie_plots_deduped.csv'
    Main.execute(file)
