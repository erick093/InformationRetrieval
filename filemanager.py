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
    def save_dict(obj):
        print("Saving dictionary...")
        with open('dict' + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_dict():
        print("Loading dictionary...")
        try:
            with open('dict.pkl', 'rb') as f:
                return pickle.load(f)
        except:
            print("ERROR: dictionary not found!")
            sys.exit(1)


