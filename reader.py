import pandas as pd
import sys

class Reader:
    def __init__(self, file):
        self.file = file

    def read_file(self):
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

