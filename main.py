import sys
from preprocessing import Preprocessing
from filemanager import FileManager
from positional_index import PositionalIndex
from proximity_query import ProximityQuery
from permuterm import Permuterm
from stemmer import PorterStemmer


class Main:
    def __init__(self):
        print("Information Retrieval System ")

    @staticmethod
    def execute(file):
        if len(sys.argv) > 1:
            query = sys.argv[1]  # query
            query_type = sys.argv[2]  # query type: positional or permuterm
            norm = sys.argv[3]  # stem normalization flag
            dict_mode = sys.argv[4]  # mode: --save to create the dictionary or --load to load it.
            df = FileManager().read_file(file)
            if dict_mode == '--save':
                prep_df = Preprocessing().preprocessing(df)
                if norm == '--stem':
                    index = PositionalIndex().create_index(prep_df, True)
                elif norm == '--nostem':
                    index = PositionalIndex().create_index(prep_df, False)
                else:
                    print("ERROR: Third argument has to be --stem or --nostem")
                    sys.exit(1)

                FileManager.save_dict(index, norm)
                print("Index saved, length: {}, normalization: {} ".format(len(index), norm))
            elif dict_mode == '--load':
                index = FileManager.load_dict(norm)
                print("Index loaded, length: {}, normalization: {} ".format(len(index), norm))
            else:
                print(
                    "ERROR: Forth argument has to be --save or --load ")
                sys.exit(1)
            index_size = round((sys.getsizeof(index) / 1024) / 1024)
            print("Size of Positional Index {} (MB): {}".format(norm, index_size))
            if query_type == '--proximity':
                stemmer = PorterStemmer()
                re1 = query.find('/')
                re2 = query.find('%')
                word_1 = query[:re1] if norm == '--nostem' else stemmer.stem(query[:re1])
                word_2 = query[re2+1:] if norm == '--nostem' else stemmer.stem(query[re2+1:])
                #word_1 = query[:re1]
                #word_2 = query[re2+1:]
                k = int(query[re1 + 1:re2])
                print("Proximity Query - word_1='{}', word_2='{}', k={} -norm:{} ".format(word_1, word_2, k, norm))
                prox_query = ProximityQuery(index, word_1, word_2, k)
                result = prox_query.query()
                print(result)
                for item in result:
                    print(df[df.ID == item['docID']])

            elif query_type == '--permuterm':
                print("Permuterm Query: {}".format(query))
                permuterm = Permuterm(index)
                permuterm.construct_index()
                result = permuterm.query(query)
                print("words matched: ", list(result.keys()))
                # print("--------------------------------------------------------------------------------------")
                # print("words matched: ", result)

            else:
                print(
                    "ERROR: Second argument has to be --proximity or --permuterm ")
                sys.exit(1)


if __name__ == '__main__':
    print("\n")
    print("------------------------Information Retrieval System------------------------")
    print("******** Project by : Erick Escobar & Faiza Tasnia")
    print("******** IRDM VUB Course - 2021")
    print("\n")
    file = 'dataset/wiki_movie_plots_deduped.csv'
    Main.execute(file)
