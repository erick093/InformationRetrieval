import pandas as pd
import sys
import pickle


class FileManager:

    def __init__(self):
        self.file = ""

    def read_file(self, file):
        self.file = file
        try:
            df = pd.read_csv(self.file)
        except:
            print("ERROR: file not found!")
            sys.exit(1)

        df["ID"] = df.index + 1
        df.drop(columns=["Release Year", "Director", "Cast", "Genre", "Wiki Page",
                         "Origin/Ethnicity"])  # Drop unused columns
        df["Tokens"] = df["Plot"]  # Creating a duplicate column to store Plot tokens.
        df = df[["ID", "Title", "Tokens", "Plot"]]  # Re-ordering columns.
        return df

    @staticmethod
    def save_dict(obj, flag):
        print("Saving dictionary...")
        if flag == "--stem":
            with open('dict_stem' + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        else:
            with open('dict_nostem' + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_dict(flag):
        print("Loading dictionary...")
        if flag == "--stem":
            try:
                with open('dict_stem.pkl', 'rb') as f:
                    return pickle.load(f)
            except:
                print("ERROR: dictionary not found!")
                sys.exit(1)
        else:
            try:
                with open('dict_nostem.pkl', 'rb') as f:
                    return pickle.load(f)
            except:
                print("ERROR: dictionary not found!")
                sys.exit(1)



